from fastapi import APIRouter
from services.embedding import gemini_embedding

router = APIRouter()

@router.post("/embed")
async def embed(text: str):
    try:
        embedding = gemini_embedding(text)
        return {
            "status": "success",
            "embedding": embedding
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }