import chromadb
from chromadb.config import Settings
from typing import List, Dict, Any, Optional
from .logger import logger
from .embeddings import EmbeddingEngine
from .utils import generate_id

class VectorStore:
    """Manages ChromaDB vector operations."""
    
    def __init__(self, persist_directory: str = "chroma_db"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.embedding_engine = EmbeddingEngine()
        self.collection_name = "parsuma_knowledge"
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={"hnsw:space": "cosine"}
        )

    def add_documents(self, chunks: List[str], metadatas: List[Dict[str, Any]], ids: Optional[List[str]] = None):
        """Add document chunks and their embeddings to the vector store."""
        if not ids:
            ids = [generate_id(chunk) for chunk in chunks]
            
        embeddings = self.embedding_engine.generate_embeddings(chunks)
        
        self.collection.add(
            embeddings=embeddings,
            documents=chunks,
            metadatas=metadatas,
            ids=ids
        )
        logger.info(f"Added {len(chunks)} chunks to vector store.")

    def search(self, query: str, n_results: int = 5) -> Dict[str, Any]:
        """Perform semantic search."""
        query_embedding = self.embedding_engine.generate_single_embedding(query)
        
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
            include=["documents", "metadatas", "distances"]
        )
        return results

class RetrievalAgent:
    """High-level retrieval logic with reranking and confidence scoring."""
    
    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store

    def retrieve_context(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Retrieve relevant context with confidence scores."""
        raw_results = self.vector_store.search(query, n_results=top_k)
        
        retrieved_items = []
        
        if not raw_results['documents'] or not raw_results['documents'][0]:
            return []

        # results are nested lists
        docs = raw_results['documents'][0]
        metas = raw_results['metadatas'][0]
        distances = raw_results['distances'][0]
        
        for i in range(len(docs)):
            # Convert cosine distance to similarity score (0 to 1)
            # Chroma returns squared L2 or cosine distance. Assuming cosine distance 0-2.
            # similarity = 1 - distance
            score = 1 - distances[i]
            
            retrieved_items.append({
                "content": docs[i],
                "metadata": metas[i],
                "score": round(float(score), 4)
            })
            
        return retrieved_items
