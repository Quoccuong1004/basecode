from openai import OpenAI
from core.config import settings
from fastapi import HTTPException

def chat_llm(messages: list[dict], provider: str = "openai", model: str = "gpt-4o-mini", response_format: dict = None):
    
    if provider == "openai":
        if not settings.openai_api_key:
            raise HTTPException(status_code=400, detail="OpenAI API key not configured")
        
        client = OpenAI(api_key=settings.openai_api_key)
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message
    
    elif provider == "google":
        if not settings.gemini_api_key:
            raise HTTPException(status_code=400, detail="Gemini API key not configured")
            
        client = OpenAI(
            api_key=settings.gemini_api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
            )
        if response_format:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                response_format=response_format
            )
        else:
            response = client.chat.completions.create(
                model=model,
                messages=messages
            )
        return response.choices[0].message
    
    else:
        raise HTTPException(status_code=400, detail=f"Unsupported provider: {provider}")