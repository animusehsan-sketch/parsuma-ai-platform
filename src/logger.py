import logging
import os
from datetime import datetime

def setup_logger(name: str, log_file: str = "logs/app.log", level=logging.INFO):
    """System-wide logging configuration."""
    
    # Ensure log directory exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # File Handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# Default app logger
logger = setup_logger("ParsumaAI")
