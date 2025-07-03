from pydantic import BaseModel


class ChatMessage(BaseModel):
    messages: list[dict]
    provider: str = "google"
    model: str = "gemini-2.5-flash"
    response_format: dict = None
