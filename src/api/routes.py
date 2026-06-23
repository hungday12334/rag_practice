from fastapi import APIRouter
from pydantic import BaseModel

from src.chains import ask_rag


router = APIRouter()


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str


@router.post("/ai/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    answer = ask_rag(request.question)
    return ChatResponse(answer=answer)