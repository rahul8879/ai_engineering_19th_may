import re
import asyncio
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from mcp_tools import get_client, tools_session, parse_tool_result
from state import SchedulingState

POLL_INTERVAL_SECONDS = 15
MAX_POLL_ATTEMPTS = 30


def _parse_search_results(text: str) -> list[dict]:
    entries = []
    for block in text.strip().split("\n\n"):
        entry = {}
        for line in block.splitlines():
            if ": " in line:
                key, _, value = line.partition(": ")
                entry[key.strip().lower()] = value.strip()
        if "id" in entry:
            entries.append(entry)
    return entries


def _extract_latest_reply_only(full_email_text: str) -> str:
    body = full_email_text.split("\n\n", 1)[-1]
    body = body.replace("\r\n", "\n")
    match = re.search(r"\nOn .+?wrote:\n", body, re.DOTALL)
    if match:
        body = body[: match.start()]
    return body.strip()


def _parse_email_date(date_str: str):
    """Returns a naive UTC datetime, or None if it can't be parsed --
    isolated here so the scan loop below can just skip anything unparseable
    instead of crashing the whole poll."""
    try:
        return parsedate_to_datetime(date_str).astimezone(timezone.utc).replace(tzinfo=None)
    except (ValueError, TypeError):
        return None


async def check_for_reply(state: SchedulingState) -> dict:
    attempts = state.get("poll_attempts", 0)
    already_processed_id = state.get("last_processed_reply_id")
    proposal_sent_at_str = state.get("proposal_sent_at")
    proposal_time = datetime.fromisoformat(proposal_sent_at_str) if proposal_sent_at_str else None

    if attempts > 0:
        await asyncio.sleep(POLL_INTERVAL_SECONDS)

    client = get_client()
    candidate_email = state["candidate"]["email"]

    async with tools_session(client, "email") as tools:
        tools_by_name = {tool.name: tool for tool in tools}

        # `after:` narrows the search server-side to day granularity --
        # it can't replace the precise timestamp check below (Gmail's
        # after: only knows about dates, not times), but it does stop
        # months of repeated test-run history from ever coming back at
        # all, which matters once search results are capped: a genuinely
        # new reply can get crowded out of a limited result set by dozens
        # of old matching test emails if there's no date filter at all.
        query = f'from:{candidate_email} subject:"Interview Scheduling"'
        if proposal_time:
            query += f' after:{proposal_time.strftime("%Y/%m/%d")}'

        search_result_raw = await tools_by_name["search_emails"].ainvoke({"query": query})
        search_result = parse_tool_result(search_result_raw)
        entries = _parse_search_results(search_result[0])
        print(f"    [debug] {len(entries)} matching email(s): "
              f"{[(e.get('id'), e.get('date')) for e in entries]}")

        # NOTE: entries[0] used to be trusted blindly as "the latest reply".
        # That's wrong whenever Gmail's search order isn't strictly
        # newest-first -- which happens easily once a test candidate has
        # sent several emails with a matching subject across earlier runs.
        # This scans every match instead, and picks the first one that's
        # both unprocessed AND newer than the proposal -- genuinely the
        # newest qualifying reply, regardless of search order.
        latest = None
        for entry in entries:
            if entry["id"] == already_processed_id:
                continue
            if proposal_time and "date" in entry:
                reply_time = _parse_email_date(entry["date"])
                if reply_time and reply_time <= proposal_time:
                    continue  # genuinely old -- keep scanning, don't give up on this poll yet
            latest = entry
            break

        if latest is None:
            return {"candidate_reply_text": None, "poll_attempts": attempts + 1}

        read_result_raw = await tools_by_name["read_email"].ainvoke(
            {"messageId": latest["id"]}
        )
        read_result = parse_tool_result(read_result_raw)

    full_text = read_result[0] if read_result else ""
    reply_only = _extract_latest_reply_only(full_text)

    return {
        "candidate_reply_text": reply_only,
        "last_processed_reply_id": latest["id"],
        "poll_attempts": attempts + 1,
    }