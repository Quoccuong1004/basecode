from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../.env",
        case_sensitive=False,
        extra="ignore",
        protected_namespaces = ('settings_',)
    )
    
    # Application Settings
    project_name: str = Field(default="LLM API Base", description="Tên project")
    version: str = Field(default="1.0.0", description="Version của API")
    debug: bool = Field(default=True, description="Debug mode")
    
    # CORS Settings
    allowed_hosts: List[str] = Field(default=["*"], description="Allowed origins for CORS")
    cors_allow_credentials: bool = Field(default=True, description="Allow credentials in CORS")
    cors_allow_methods: List[str] = Field(default=["*"], description="Allowed HTTP methods")
    cors_allow_headers: List[str] = Field(default=["*"], description="Allowed headers")
    
    # API Keys
    openai_api_key: str = Field(default="", description="OpenAI API key")
    gemini_api_key: str = Field(default="", description="Google Gemini API key")
    
    # LLM Settings
    model_name: str = Field(default="gpt-4o", description="Model mặc định")
    temperature: float = Field(default=0.5, ge=0, le=2, description="Temperature cho LLM")
    max_tokens: int = Field(default=1000, gt=0, description="Max tokens")
    
    # Logging Settings
    log_level: str = Field(default="INFO", description="Log level (DEBUG, INFO, WARNING, ERROR)")
    log_file: str = Field(default="logs/app.log", description="Log file path")
    log_max_size: int = Field(default=10485760, description="Max log file size (10MB)")
    log_backup_count: int = Field(default=3, description="Number of backup log files")
    log_to_console: bool = Field(default=True, description="Log to console")
    log_to_file: bool = Field(default=True, description="Log to file")


settings = Settings()

