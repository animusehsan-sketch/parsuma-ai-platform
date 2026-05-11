import re
import os
from typing import Dict, Any, List
from .logger import logger

class SafetyGuard:
    """Provides input validation and output sanitization."""
    
    def __init__(self):
        self.malicious_patterns = [
            r"ignore previous instructions",
            r"system prompt",
            r"reveal your secrets",
            r"sql injection",
            r"<script>",
        ]

    def is_safe_input(self, text: str) -> bool:
        """Check for potentially malicious prompt injection patterns."""
        for pattern in self.malicious_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                logger.warning(f"Safety violation detected in input: {text[:50]}...")
                return False
        return True

    def validate_file(self, filename: str, size_bytes: int) -> bool:
        """Validate file type and size."""
        MAX_SIZE = 10 * 1024 * 1024 # 10MB
        ALLOWED_EXT = {'.pdf', '.docx', '.txt'}
        
        ext = os.path.splitext(filename)[1].lower()
        if ext not in ALLOWED_EXT:
            return False
            
        if size_bytes > MAX_SIZE:
            return False
            
        return True

    def sanitize_output(self, text: str) -> str:
        """Basic output sanitization."""
        # Remove potential HTML/script tags if they appear in generated content
        text = re.sub(r'<[^>]*>', '', text)
        return text
