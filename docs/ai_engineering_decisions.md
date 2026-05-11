# AI Engineering Decisions: Parsuma AI Platform

This document details the critical engineering decisions made during the development of Parsuma AI, justifying the selection of specific models, frameworks, and architectural patterns within the context of a Master's level Applied AI project.

---

## 1. LLM Selection: OpenAI `gpt-4o-mini`
**Decision**: Adoption of `gpt-4o-mini` over larger models like `gpt-4o` or `claude-3-opus`.
**Rationale**:
- **Efficiency-Performance Ratio**: `gpt-4o-mini` provides near-state-of-the-art reasoning for RAG tasks while maintaining significantly lower latency and cost.
- **Context Window Management**: The model's 128k context window allows for substantial context injection during multi-document retrieval without significant performance degradation.
- **Safety Fine-tuning**: OpenAI's native safety layers provide a robust baseline for the platform's secondary Safety Agent.

## 2. Embedding Strategy: Local `all-MiniLM-L6-v2`
**Decision**: Use of a local Transformer-based embedding model via `sentence-transformers`.
**Rationale**:
- **Data Privacy**: By generating embeddings locally, sensitive institutional data remains within the application boundary until the final synthesis phase.
- **Resource Optimization**: `all-MiniLM-L6-v2` is a lightweight model that performs exceptionally well on semantic similarity tasks without requiring high-end GPU resources.
- **Latency**: Eliminating API calls for embedding generation during document ingestion significantly speeds up the "Time-to-Index" for the user.

## 3. Vector Database: ChromaDB (Persistent)
**Decision**: Implementation of **ChromaDB** as the primary vector storage engine.
**Rationale**:
- **Serverless Architecture**: ChromaDB's persistent client allows for a "database-as-a-file" approach, simplifying deployment in Docker and Streamlit Cloud environments.
- **Native Filtering**: Supports metadata filtering out-of-the-box, which is essential for our "Asset Library" management feature.
- **Community Support**: Extensive integration with the RAG ecosystem ensures long-term maintainability.

## 4. Orchestration Pattern: Federated Multi-Agent System
**Decision**: Moving away from a monolithic RAG script toward a decentralized agentic framework.
**Rationale**:
- **Separation of Concerns**: Each agent (Ingestion, Retrieval, Strategy, Safety) has a dedicated system prompt and logic, reducing prompt complexity.
- **Error Isolation**: Failures in the retrieval agent can be caught and handled gracefully by the Safety Agent before reaching the UI.
- **Scalability**: New agents (e.g., a "Citation Auditor" or "Financial Analyst") can be integrated without rewriting the core pipeline.

## 5. Chunking Strategy: Recursive Character Splitting
**Decision**: Implementing recursive splitting with a 200-token overlap.
**Rationale**:
- **Semantic Continuity**: Unlike fixed-size chunking, recursive splitting attempts to keep paragraphs and sentences together, preserving the flow of institutional knowledge.
- **Context Preservation**: The overlap ensures that concepts split at chunk boundaries are represented in both segments, improving retrieval accuracy for queries targeting those boundaries.
