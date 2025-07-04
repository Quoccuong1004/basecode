from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from contextlib import asynccontextmanager
from core.config import settings
from core.logging import get_logger
from core.middleware import RequestIDMiddleware, get_request_id
from routers.chat import router as chat_router
from routers.embed import router as embed_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Setup logger
    logger = get_logger("main")
    
    # Startup
    logger.info("🚀 Starting LLM API server...")    
    yield
    
    # Shutdown
    logger.info("🛑 Shutting down LLM API server...")


app = FastAPI(
    title=settings.project_name,
    version=settings.version,
    description="LLM API Base Code với FastAPI và Logging",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Request ID middleware (phải thêm đầu tiên)
app.add_middleware(RequestIDMiddleware)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_hosts,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Logger cho requests
logger = get_logger("api")


# Routers
app.include_router(chat_router, prefix="/api", tags=["Chat"])
app.include_router(embed_router, prefix="/api", tags=["Embedding"])

@app.get("/", tags=["Health"])
async def root():
    req_id = get_request_id()
    logger.info(f"Root endpoint processing")
    return {"message": "LLM API đang hoạt động!", "status": "healthy", "request_id": req_id}


@app.get("/health", tags=["Health"])
async def health_check():
    logger.info(f"Health check processing")
    return {"status": "healthy", "version": settings.version, "request_id": get_request_id()}


if __name__ == "__main__":
    # Logger cho main
    main_logger = get_logger("main")
    main_logger.info("Starting server from main...")
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
        log_level=settings.log_level.lower()
    ) 