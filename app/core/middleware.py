import string
import random
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from contextvars import ContextVar
from core.logging import get_logger

# Context variable để store request ID
request_id_var: ContextVar[str] = ContextVar('request_id', default='')
logger = get_logger("middleware")

def generate_request_id(length: int = 4) -> str:
    """Generate random request ID với 3-4 ký tự"""
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

def get_request_id() -> str:
    """Lấy request ID hiện tại"""
    return request_id_var.get()

class RequestIDMiddleware(BaseHTTPMiddleware):
    """Middleware thêm request ID vào mỗi request"""
    
    async def dispatch(self, request: Request, call_next):
        # Generate request ID
        req_id = generate_request_id()
        
        # Set into context variable
        request_id_var.set(req_id)
        
        # Add to request state
        request.state.request_id = req_id
        
        # Log request start
        logger.info(f"{request.method} {request.url.path}") 
        
        # Process request
        response: Response = await call_next(request)
        
        # Add request ID to response headers
        response.headers["X-Request-ID"] = req_id
        
        # Log response
        logger.info(f"Response: {response.status_code}")
        
        return response 