from typing import List, Dict, Any
import re

class Chunker:
    """Intelligently splits text into manageable chunks for RAG."""
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_text(self, text: str) -> List[str]:
        """Split text into chunks with overlap, attempting to preserve sentence integrity."""
        if not text:
            return []
            
        # Basic cleanup
        text = re.sub(r'\s+', ' ', text).strip()
        
        chunks = []
        start = 0
        text_len = len(text)
        
        while start < text_len:
            end = min(start + self.chunk_size, text_len)
            
            # If not at the end, try to find a sentence boundary
            if end < text_len:
                # Look for last sentence end (., !, ?) within last 100 chars
                boundary_search_area = text[end-100:end]
                boundary_match = re.search(r'[.!?]\s', boundary_search_area[::-1])
                if boundary_match:
                    end = end - boundary_match.start()
            
            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)
            
            start = end - self.chunk_overlap
            # Prevent infinite loops if end doesn't advance
            if start >= end:
                start = end
                
        return chunks
