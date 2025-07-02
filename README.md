# 🚀 LLM API Base Code

FastAPI-based LLM API với logging system, request tracing, và multi-provider support.

## ✨ Features

- 🔥 **FastAPI** - Modern, fast web framework
- 📝 **Advanced Logging** - Request ID tracing, file rotation
- 🌐 **CORS Support** - Cross-origin resource sharing
- 🔌 **Multi-LLM Providers** - OpenAI, Anthropic, Gemini
- ⚡ **Hot Reload** - Development-friendly
- 🛡️ **Type Safety** - Pydantic models
- 📊 **Request Tracing** - Unique ID cho mỗi request

## 🏗️ Project Structure

```
app/
├── core/
│   ├── config.py          # Application settings
│   ├── logging.py         # Logging configuration
│   └── middleware.py      # Request ID middleware
├── routers/
│   └── chat.py           # Chat endpoints
└── main.py               # FastAPI application
```

## 🚀 Quick Start

### 1. Clone repository
```bash
git clone <your-repo-url>
cd new-basecode
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment setup
```bash
cp .env.example .env
# Edit .env với API keys của bạn
```

### 4. Run application
```bash
# Development
python3 -m app.main

# Or with uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Access API
- **API Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## 🔧 Configuration

### Environment Variables
```bash
# Application
PROJECT_NAME="LLM API Base"
VERSION="1.0.0"
DEBUG=true

# API Keys
OPENAI_API_KEY="your-openai-key"
GEMINI_API_KEY="your-gemini-key"

# Logging
LOG_LEVEL="INFO"
LOG_TO_CONSOLE=true
LOG_TO_FILE=true
LOG_FILE="logs/app.log"
```

## 📊 Logging Features

### Request Tracing
Mỗi request có unique ID (3-4 ký tự) để trace logs:
```
2025-07-02 15:08:48 [ABC1] - LLM API Base.middleware - INFO - GET /health
2025-07-02 15:08:48 [ABC1] - LLM API Base.api - INFO - Health check processing
```

### Log Outputs
- **Console**: Real-time logs với colors
- **File**: `logs/app.log` với rotation (10MB max, 3 backups)
- **Headers**: Request ID trong response headers

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

1. **Request** → RequestIDMiddleware tạo unique ID
2. **Context** → Request ID stored in context variable
3. **Processing** → Endpoints xử lý với logging
4. **Response** → Request ID trong headers
5. **Logs** → All logs có request ID để tracing

## 🏆 Best Practices

- ✅ Request ID tracing cho debugging
- ✅ Structured logging với timestamps
- ✅ Environment-based configuration
- ✅ Type hints everywhere
- ✅ Error handling với proper status codes
- ✅ CORS configuration
- ✅ Hot reload cho development

## 📝 License

MIT License - feel free to use cho projects của bạn!

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

---

Built with ❤️ using FastAPI và Python
