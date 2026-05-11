from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np
from .logger import logger

class EmbeddingEngine:
    """Generates high-quality vector embeddings using sentence-transformers."""
    
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        try:
            logger.info(f"Initializing EmbeddingEngine with model: {model_name}")
            self.model = SentenceTransformer(model_name)
        except Exception as e:
            logger.error(f"Failed to load embedding model: {str(e)}")
            raise

    def generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Convert a list of texts into vector embeddings."""
        if not texts:
            return []
        
        try:
            embeddings = self.model.encode(texts)
            # Convert numpy array to list of lists for ChromaDB compatibility
            return embeddings.tolist()
        except Exception as e:
            logger.error(f"Error generating embeddings: {str(e)}")
            return []

    def generate_single_embedding(self, text: str) -> List[float]:
        """Convert a single text into a vector embedding."""
        return self.generate_embeddings([text])[0]
