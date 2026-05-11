import pytest
from src.rag_pipeline import RAGPipeline
from src.retriever import RetrievalAgent, VectorStore
import os

def test_pipeline_initialization():
    """Test that the RAG pipeline initializes correctly."""
    vs = VectorStore(persist_directory="chroma_db_test")
    ra = RetrievalAgent(vs)
    pipeline = RAGPipeline(ra)
    
    assert pipeline.retrieval_agent == ra
    assert pipeline.client is not None

def test_rag_response_structure():
    """Test the structure of the RAG response object."""
    # This is a unit test, we'll mock the actual LLM call if needed, 
    # but here we check if the pipeline handles empty context gracefully.
    vs = VectorStore(persist_directory="chroma_db_test")
    ra = RetrievalAgent(vs)
    pipeline = RAGPipeline(ra)
    
    # Using a dummy query that will likely return no context
    response = pipeline.generate_response("Test query for unit testing")
    
    assert "answer" in response
    assert "sources" in response
    assert isinstance(response["sources"], list)
