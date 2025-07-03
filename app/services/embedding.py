from google import genai
from google.genai import types
from core.config import settings

def gemini_embedding(text: str):

    client = genai.Client(api_key=settings.gemini_api_key)

    result = client.model.embed_content(
        model = "gemini-embedding-exp-03-07",
        content = text,
        config = types.EmbeddingConfig(
            task_type = types.EmbedContentConfig(task_type = "SEMANTIC_SIMILARITY")
        )
    )

    return result.embeddings[0].values