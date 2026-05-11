import os
from typing import List, Dict, Any, Optional
from openai import OpenAI
from .logger import logger
from .retriever import RetrievalAgent, VectorStore
from .prompts import RAG_SYSTEM_PROMPT
from dotenv import load_dotenv

load_dotenv()

class RAGPipeline:
    """Orchestrates the Retrieval-Augmented Generation process."""
    
    def __init__(self, retrieval_agent: RetrievalAgent):
        self.retrieval_agent = retrieval_agent
        # Prioritize MODEL_NAME from .env, fallback to OPENAI_MODEL, then gpt-4o-mini
        self.model = os.getenv("MODEL_NAME") or os.getenv("OPENAI_MODEL") or "gpt-4o-mini"
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_response(self, query: str, top_k: int = 5) -> Dict[str, Any]:
        """Generate a grounded response using retrieved context."""
        logger.info(f"Processing query: {query} with model: {self.model}")
        
        # 1. Retrieve Context
        context_items = self.retrieval_agent.retrieve_context(query, top_k=top_k)
        
        if not context_items:
            logger.warning("No relevant context found.")
            context_text = "No relevant context found in the knowledge base."
        else:
            context_text = "\n\n".join([
                f"--- Source: {item['metadata'].get('filename', 'Unknown')} ---\n{item['content']}"
                for item in context_items
            ])

        # 2. Prepare Prompt
        messages = [
            {"role": "system", "content": RAG_SYSTEM_PROMPT},
            {"role": "user", "content": f"Context:\n{context_text}\n\nQuery: {query}"}
        ]

        # 3. Generate Completion
        try:
            # Check for API Key explicitly
            if not self.client.api_key or "PASTE_MY_KEY_HERE" in self.client.api_key:
                raise ValueError("OpenAI API Key is missing or invalid. Please check your .env file.")

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.3,
                max_tokens=1000
            )
            
            answer = response.choices[0].message.content
            
            return {
                "answer": answer,
                "sources": context_items,
                "model": self.model,
                "usage": {
                    "prompt_tokens": response.usage.prompt_tokens,
                    "completion_tokens": response.usage.completion_tokens,
                    "total_tokens": response.usage.total_tokens
                }
            }
        except Exception as e:
            error_msg = f"OpenAI API Error ({type(e).__name__}): {str(e)}"
            logger.error(error_msg)
            return {
                "answer": f"⚠️ ERROR: {error_msg}",
                "sources": [],
                "error": str(e)
            }
