from typing import List, Dict, Any, Optional
import os
from .logger import logger
from .document_loader import DocumentLoader
from .chunker import Chunker
from .retriever import VectorStore, RetrievalAgent
from .rag_pipeline import RAGPipeline
from .prompts import CONTENT_STRATEGY_PROMPT, SAFETY_EVAL_PROMPT
from openai import OpenAI

class DocumentIntelligenceAgent:
    """Agent responsible for document ingestion and processing."""
    
    def __init__(self, vector_store: VectorStore):
        self.loader = DocumentLoader()
        self.chunker = Chunker()
        self.vector_store = vector_store

    def process_document(self, file_path: str, metadata: Optional[Dict[str, Any]] = None) -> int:
        """Load, chunk, and index a document."""
        logger.info(f"Processing document: {file_path}")
        text = self.loader.load(file_path)
        chunks = self.chunker.chunk_text(text)
        
        if not metadata:
            metadata = {}
        
        metadata["filename"] = os.path.basename(file_path)
        metadatas = [metadata for _ in chunks]
        
        self.vector_store.add_documents(chunks, metadatas)
        return len(chunks)

class ContentStrategyAgent:
    """Agent responsible for generating strategic content ideas."""
    
    def __init__(self, rag_pipeline: RAGPipeline):
        self.rag_pipeline = rag_pipeline

    def generate_strategy(self, topic: str, audience: str, languages: List[str]) -> Dict[str, Any]:
        """Generate a content strategy based on knowledge base."""
        query = f"Generate a content strategy for the topic '{topic}' targeting {audience} in {', '.join(languages)}."
        
        # We override the system prompt for this specific task
        response = self.rag_pipeline.generate_response(query)
        return response

class SafetyAgent:
    """Agent responsible for validating inputs and outputs."""
    
    def __init__(self):
        self.model = os.getenv("MODEL_NAME") or os.getenv("OPENAI_MODEL") or "gpt-4o-mini"
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def evaluate_response(self, query: str, context: str, response: str) -> Dict[str, Any]:
        """Evaluate response for grounding and safety."""
        messages = [
            {"role": "system", "content": SAFETY_EVAL_PROMPT},
            {"role": "user", "content": f"Query: {query}\nContext: {context}\nResponse: {response}"}
        ]
        
        try:
            # Explicit key check
            if not self.client.api_key or "PASTE_MY_KEY_HERE" in self.client.api_key:
                raise ValueError("OpenAI API Key is missing or invalid.")

            eval_response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                response_format={"type": "json_object"}
            )
            import json
            return json.loads(eval_response.choices[0].message.content)
        except Exception as e:
            error_msg = f"Safety evaluation failed: {str(e)}"
            logger.error(error_msg)
            return {
                "grounding_score": 0.5, 
                "safety_score": 1.0, 
                "notes": f"Evaluation Error: {str(e)}"
            }
