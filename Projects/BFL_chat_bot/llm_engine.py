from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from pathlib import Path
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage,SystemMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
from memory import WindowChatMessageHistory
from rag_chain import rag_answer
from bfl_tools import get_loan_status, get_emi_schedule, calculate_prepayment,process_refund_request
tools = [
    get_emi_schedule,
    calculate_prepayment,get_loan_status,process_refund_request
]
load_dotenv()
print(load_dotenv())

SYSTEM_PROMPT = """
You are a query classifier for Bajaj Finance helpdesk.

Classify the customer query into ONE of these categories:
- "tool"   : query requires live loan data (needs Loan ID like BFL001)
              Examples: loan status, EMI schedule, prepayment, refund,
              foreclose my loan, close my loan, settle my account
- "policy" : query is about rules, eligibility, charges, documents
              AND follow-up questions about a previous policy answer
              Examples: CIBIL score, foreclosure charges, interest rates,
              documents needed, what happens if I miss EMI,
              "how do you know this", "where did you get this",
              "is this from your policy", "what is your source"
- "general": greeting, thank you, out of scope

Reply with ONLY one word: tool / policy / general
"""

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
llm_with_tools = llm.bind_tools(tools)

tool_map = {
    "get_loan_status":        get_loan_status,
    "get_emi_schedule":       get_emi_schedule,
    "calculate_prepayment":   calculate_prepayment,
    "process_refund_request": process_refund_request,
}

store = {}

def get_session_history(session_id:str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]



def run_chat_turn(user_message:str,session_id):
    history = get_session_history(session_id)
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(history.messages)
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

    history.add_user_message(user_message)
    history.add_ai_message(response.content)
     

    return response.content, tool_used


def run_policy_run(user_message:str,session_id):
    history = get_session_history(session_id)
    policy_history = []
    reply = rag_answer(user_message,policy_history)
    history.add_user_message(user_message)
    history.add_ai_message(reply)
    return reply


def run_general_turn(user_message:str,session_id):
    history = get_session_history(session_id)
    message = [{'role':"system","content":SYSTEM_PROMPT}]
    message.extend(history.messages)
    message.append(HumanMessage(content=user_message))
    response = llm.invoke(message)
    history.add_user_message(user_message)
    history.add_ai_message(response.content)
    return response.content


def classify_query(query):
    response = llm.invoke([
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=query),
    ])
    category = response.content.strip()
    if category not in ["tool", "policy", "general"]:
        raise ValueError(f"Invalid category: {category}")
    return category





# print(run_chat_turn("What is the status of my loan BFL2024001?", "rahul123"))

# print(run_chat_turn("what was my last questions", "rahul123"))
# print('current value in store',store)



