from fastapi import APIRouter
from schemas.chat import ChatMessage

router = APIRouter()

@router.post("/chat")
async def chat(message: ChatMessage):
    return {"message": message}
