from google import genai
from core.config import settings
from core.logging import get_logger
import traceback
from google.genai import types
logger = get_logger(__name__)

def gemini_embedding(text: str):
    try:
        client = genai.Client(api_key=settings.gemini_api_key)
        
        logger.info(f"Calling embed_content for text: {text[:100]}...")
        
        result = client.models.embed_content(
            model="gemini-embedding-exp-03-07",
            contents=[text],
            config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
            )
        return result.embeddings[0].values
        
    except Exception as e:
        logger.error(f"Embedding failed: {str(e)}")
        logger.error(f"Full stacktrace:\n{traceback.format_exc()}")
        raise e