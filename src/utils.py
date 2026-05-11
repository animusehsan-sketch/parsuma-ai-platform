import os
import uuid
import hashlib
from typing import List, Dict, Any
from .logger import logger

def generate_id(content: str) -> str:
    """Generate a unique ID based on content hash."""
    return hashlib.md5(content.encode()).hexdigest()

def ensure_dirs(dirs: List[str]):
    """Ensure that necessary directories exist."""
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)
            logger.info(f"Created directory: {d}")

def get_file_extension(filename: str) -> str:
    """Get file extension in lowercase."""
    return os.path.splitext(filename)[1].lower()

def validate_file_type(filename: str, allowed_extensions: List[str]) -> bool:
    """Check if file extension is allowed."""
    return get_file_extension(filename) in allowed_extensions
