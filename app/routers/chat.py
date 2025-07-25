from fastapi import APIRouter
from schemas.chat import ChatMessage
from services.chat import chat_llm
router = APIRouter()

@router.post("/chat")
async def chat(input_request: ChatMessage):
    response = chat_llm(input_request.messages, input_request.provider, input_request.model, input_request.response_format)
    return response
