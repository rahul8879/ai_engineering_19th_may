from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from llm_engine import run_chat_turn
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
    tools_called: list[str] = []



@app.get("/")
def ui():
    return HTMLResponse(open("home.html", "r").read())

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post('/chat',response_model=ChatResponse)
def chat(req : ChatRequest):
    session_id = req.session_id
    reply,tool_called = run_chat_turn(req.message,session_id)
    return ChatResponse(reply=reply,session_id=session_id,tools_called=tool_called)