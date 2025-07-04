from fastapi import APIRouter
from services.embedding import gemini_embedding
from core.logging import get_logger

router = APIRouter()
logger = get_logger(__name__)

@router.post("/embed")
async def embed(text: str):
    try:
        embedding = gemini_embedding(text)
        return {
            "status": "success",
            "embedding": embedding
        }
    except Exception as e:
        logger.error(f"Embedding failed with error: {str(e)}")
        
        return {
            "status": "error",
            "error": str(e)
        }