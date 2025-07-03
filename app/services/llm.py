from openai import OpenAI
from core.config import settings

def chat_llm(messages: list[dict], provider: str = "openai", model: str = "gpt-4o-mini", response_format: dict = None):
    
    if provider == "openai":
        client = OpenAI(api_key=settings.openai_api_key)
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message
    
    elif provider == "google":
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