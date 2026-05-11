import pytest
from src.retriever import VectorStore, RetrievalAgent
from src.chunker import Chunker

def test_vector_store_add_and_search():
    """Test adding documents and searching in the vector store."""
    vs = VectorStore(persist_directory="chroma_db_test")
    chunks = ["The capital of Finland is Helsinki.", "Python is a programming language."]
    metadatas = [{"filename": "test1.txt"}, {"filename": "test2.txt"}]
    
    vs.add_documents(chunks, metadatas)
    results = vs.search("What is the capital of Finland?", n_results=1)
    
    assert len(results["documents"][0]) > 0
    assert "Helsinki" in results["documents"][0][0]

def test_retrieval_agent_scoring():
    """Test that the retrieval agent returns items with scores."""
    vs = VectorStore(persist_directory="chroma_db_test")
    ra = RetrievalAgent(vs)
    
    context = ra.retrieve_context("Finland")
    
    if context:
        assert "score" in context[0]
        assert 0 <= context[0]["score"] <= 1
