from fastapi import FastAPI
from pydantic import BaseModel
from app.infrastructure.llm.llm_factory import get_llm

app = FastAPI(title="Real LLM Chatbot")

llm = get_llm()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    reply = llm.generate(req.message)
    return {"reply": reply}

@app.get("/")
def health():
    return {"status": "Chatbot running with real LLM"}
