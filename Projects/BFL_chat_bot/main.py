from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from llm_engine import run_chat_turn,run_policy_run,run_general_turn,classify_query
from pydantic import BaseModel
from langchain_core.chat_history import InMemoryChatMessageHistory
app = FastAPI(
    name="BFL Chat Bot",
    description="This is a chat bot for BFL",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    message: str
    session_id: str


class ChatResponse(BaseModel):
    reply: str
    session_id: str
    query_type: str
    tools_called: list[str] = []



@app.get("/")
def ui():
    return HTMLResponse(open("home.html", "r").read())



@app.post('/chat',response_model=ChatResponse)
def chat(req : ChatRequest):
    session_id = req.session_id
    query_type = classify_query(req.message)
    print(f"Query type: {query_type}")

    if query_type == "tool":
        reply, tool_called = run_chat_turn(req.message,req.session_id)
        return ChatResponse(reply=reply, session_id=session_id, tools_called=tool_called,
                            query_type=query_type)
    elif query_type == "policy":
        reply = run_policy_run(req.message,req.session_id)
        return ChatResponse(reply=reply, session_id=session_id, query_type=query_type)
    
    else:
        reply = run_general_turn(req.message,req.session_id)
        return ChatResponse(reply=reply, session_id=session_id, query_type=query_type)

    