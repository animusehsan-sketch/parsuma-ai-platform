# Parsuma AI: Architecture Overview

This document provides a detailed technical overview of the Parsuma AI Knowledge Intelligence Platform. It covers the system's structural components, the multi-agent orchestration layer, and the data processing pipeline.

---

## 1. System Architecture Diagram

The end-to-end flow from user interaction to verified response generation is illustrated below:

```mermaid
graph TD
    User([User])
    
    subgraph UI_Layer [Frontend Layer]
        Streamlit[Streamlit UI]
        Modules[Document Upload / Chat / Strategy Studio]
        CSS[Custom Glassmorphism CSS]
    end

    subgraph Ingestion_Agent [Document Intelligence Agent]
        Extraction[Text Extraction - PDF/DOCX/TXT]
        Chunking[Recursive Character Chunking]
        Embeddings[Local Embeddings - all-MiniLM-L6-v2]
        VectorStore[(ChromaDB Vector Store)]
    end

    subgraph Retrieval_Layer [Retrieval & Reasoning Agent]
        QueryProcessing[Query Semantic Analysis]
        Retriever[Similarity Search - Cosine Similarity]
        RAGPipeline[RAG Context Injection]
    end

    subgraph LLM_Orchestration [AI Pipeline]
        OpenAI[OpenAI API - gpt-4o-mini]
        SystemPrompt[Dynamic System Prompting]
    end

    subgraph Validation_Layer [Safety & Evaluation Agent]
        Guardrails[Safety Filtering]
        Eval[Faithfulness & Relevancy Scoring]
        FinalOutput[Final Answer with Citations]
    end

    %% Connections
    User --> Streamlit
    Streamlit --> Modules
    Modules --> Ingestion_Agent
    Streamlit --> CSS
    
    Extraction --> Chunking
    Chunking --> Embeddings
    Embeddings --> VectorStore
    
    Modules --> Retrieval_Layer
    VectorStore -.-> Retriever
    Retrieval_Layer --> LLM_Orchestration
    LLM_Orchestration --> Validation_Layer
    Validation_Layer --> Streamlit
```

---

## 2. Core Architectural Pillars

### **Federated Agentic Framework**
Unlike standard RAG implementations, Parsuma AI utilizes a **Multi-Agent Orchestration Layer**. This design allows for specialized "Expert Agents" to handle specific domains of the pipeline (Retrieval, Synthesis, Safety), improving overall system reliability and maintainability.

### **Localized Vector Intelligence**
By utilizing local embedding models (`all-MiniLM-L6-v2`) and persistent vector stores (`ChromaDB`), the platform ensures high performance and data privacy, critical for institutional and academic environments.

### **Safety-First Synthesis**
Every response is processed through a dedicated **Safety & Evaluation Agent**. This agent performs factual grounding checks to ensure that the LLM does not hallucinate information beyond the provided knowledge base.

---

## 3. Data Flow Pipeline

1.  **Ingestion**: Documents are parsed, chunked using a recursive character strategy, and vectorized.
2.  **Semantic Retrieval**: Queries are converted to high-dimensional vectors and matched against the ChromaDB index using Cosine Similarity.
3.  **Context Augmentation**: The top relevant chunks are injected into a structured system prompt.
4.  **Verification**: The generated response is audited for faithfulness and relevancy before reaching the UI.
