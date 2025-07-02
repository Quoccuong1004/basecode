import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional
from core.config import settings


class RequestIDFormatter(logging.Formatter):
    """Custom formatter để thêm request ID vào logs"""
    
    def format(self, record):
        # Import here to avoid circular import
        try:
            from core.middleware import get_request_id
            req_id = get_request_id()
            if req_id:
                record.request_id = f"[{req_id}]"
            else:
                record.request_id = ""
        except:
            record.request_id = ""
        
        return super().format(record)


def setup_logging() -> logging.Logger:
    """
    Setup logging configuration for the entire application
    """
    # Create log directory if it doesn't exist
    log_dir = Path(settings.log_file).parent
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Create main logger
    logger = logging.getLogger(settings.project_name)
    logger.setLevel(getattr(logging, settings.log_level.upper()))
    
    # Custom formatter với request ID
    log_format = "%(asctime)s %(request_id)s - %(name)s - %(levelname)s - %(message)s"
    formatter = RequestIDFormatter(log_format)
    
    # Console handler
    if settings.log_to_console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(getattr(logging, settings.log_level.upper()))
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    
    # File handler with rotation
    if settings.log_to_file:
        file_handler = RotatingFileHandler(
            settings.log_file,
            maxBytes=settings.log_max_size,
            backupCount=settings.log_backup_count,
            encoding='utf-8'
        )
        file_handler.setLevel(getattr(logging, settings.log_level.upper()))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Get logger instance for specific module
    """
    if name:
        return logging.getLogger(f"{settings.project_name}.{name}")
    return logging.getLogger(settings.project_name)

# Setup logging when importing module
main_logger = setup_logging() 