from fastapi import APIRouter
from pydantic import BaseModel
from src.chains import ask_rag
from src.chains import ingestion
router = APIRouter()
class ChatRequest(BaseModel):
    question: str
class ChatResponse(BaseModel):
    answer: str

@router.post("/ai/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    answer = ask_rag(request.question)
    return ChatResponse(answer=answer)

@router.post("/ai/ingestion_data", response_model=ChatResponse)
async def ingestion_data() -> ChatResponse:
    await ingestion()
    return ChatResponse(answer="Nap thanh cong")