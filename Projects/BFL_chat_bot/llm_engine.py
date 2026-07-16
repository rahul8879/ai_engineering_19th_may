from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from pathlib import Path
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage

from bfl_tools import get_loan_status, get_emi_schedule, calculate_prepayment,process_refund_request
tools = [
    get_emi_schedule,
    calculate_prepayment,get_loan_status,process_refund_request
]
load_dotenv()
print(load_dotenv())

SYSTEM_PROMPT = """You are a professional Bajaj Finance customer support agent.

You have access to:
1. TOOLS  — for live loan data (status, EMI, prepayment, refund)
             Use when customer provides a Loan ID (BFL + digits)

RULES:
- Loan ID present → use tools
- Format all amounts with Rs and commas (e.g., Rs 8,450)
- Be warm, concise, and professional
- If a loan is not found, ask customer to double-check the Loan ID
"""

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
llm_with_tools = llm.bind_tools(tools)

tool_map = {
    "get_loan_status":        get_loan_status,
    "get_emi_schedule":       get_emi_schedule,
    "calculate_prepayment":   calculate_prepayment,
    "process_refund_request": process_refund_request,
}


def run_chat_turn(user_message:str):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}]
    messages.append(HumanMessage(content=user_message))
    tool_used = []
    response = llm_with_tools.invoke(messages)
    while response.tool_calls:
        messages.append(response)
        for tool_call in response.tool_calls:
            tool_name = tool_call['name']
            tool_args = tool_call['args']
            tool_used.append(tool_name)
            tool_fn = tool_map.get(tool_name)
            if tool_fn:
                result = tool_fn.invoke(tool_args)
            else:
                result = {"error": f"Tool {tool_name} not found"}
            messages.append(ToolMessage(content=str(result), tool_call_id=tool_call['id']))

        response = llm_with_tools.invoke(messages)

    return response.content, tool_used



