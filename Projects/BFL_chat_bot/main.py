from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from llm_engine import run_chat_turn
from pydantic import BaseModel
app = FastAPI(
    name="BFL Chat Bot",
    description="This is a chat bot for BFL",
    version="1.0.0"
)

class ChatRequest(BaseModel):
    message: str


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
    seesion_id = "Testing123"
    reply,tool_called = run_chat_turn(req.message)
    return ChatResponse(reply=reply,session_id=seesion_id,tools_called=tool_called)