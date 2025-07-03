# 🚀 LLM API Base Code

FastAPI-based LLM API with logging system, request tracing, and multi-provider support.

## ✨ Features

- 🔥 **FastAPI** - Modern, fast web framework
- 📝 **Advanced Logging** - Request ID tracing, file rotation
- 🌐 **CORS Support** - Cross-origin resource sharing
- 🔌 **Multi-LLM Providers** - OpenAI, Anthropic, Gemini
- 🛡️ **Type Safety** - Pydantic models
- 📊 **Request Tracing** - Unique ID for each request

## 🏗️ Project Structure

```
app/
├── core/
│   ├── __init__.py
│   ├── config.py          # Application settings
│   ├── logging.py         # Logging configuration
│   └── middleware.py      # Request ID middleware
├── routers/
│   ├── __init__.py
│   └── chat.py           # Chat endpoints
├── schemas/
│   ├── __init__.py
│   └── chat.py           # Pydantic models
├── services/
│   └── __init__.py       # Business logic services
├── logs/
│   └── app.log           # Application logs
└── main.py               # FastAPI application
requirements.txt          # Python dependencies
README.md                 # Project documentation
.gitignore               # Git ignore rules
```

## 🚀 Quick Start

### 1. Clone repository
```bash
git clone https://github.com/Quoccuong1004/basecode.git
cd new-basecode
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment setup
```bash
cp .env.example .env
# Edit .env with your API keys
```

### 4. Run application
```bash
# Development
cd app
python3 -m main.py

# Or with uvicorn
cd app
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Access API
- **API Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## 📊 Logging Features

### Request Tracing
Each request gets a unique ID (3-4 characters) for log tracing:
```
2025-07-02 15:08:48 [ABC1] - LLM API Base.middleware - INFO - GET /health
2025-07-02 15:08:48 [ABC1] - LLM API Base.api - INFO - Health check processing
```

### Log Outputs
- **Console**: Real-time logs with colors
- **File**: `logs/app.log` with rotation (10MB max, 3 backups)
- **Headers**: Request ID in response headers

## 🛠️ Development

### Run in development mode
```bash
python3 -m app.main
```

### Testing endpoints
```bash
# Health check
curl http://localhost:8000/health

# Root endpoint
curl http://localhost:8000/
```

## 📁 API Endpoints

### Health
- `GET /` - Root endpoint
- `GET /health` - Health check

### Chat (Coming Soon)
- `POST /api/chat` - Chat completion
- `POST /api/completion` - Text completion
- `POST /api/embedding` - Text embedding

## 🔄 Request Flow

1. **Request** → RequestIDMiddleware generates unique ID
2. **Context** → Request ID stored in context variable
3. **Processing** → Endpoints process with logging
4. **Response** → Request ID in headers
5. **Logs** → All logs include request ID for tracing

## 🏆 Best Practices

- ✅ Request ID tracing for debugging
- ✅ Structured logging with timestamps
- ✅ Environment-based configuration
- ✅ Type hints everywhere
- ✅ Error handling with proper status codes
- ✅ CORS configuration
- ✅ Hot reload for development

## 📝 License

MIT License - feel free to use for your projects!

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

---

Built with ❤️ using FastAPI and Python
