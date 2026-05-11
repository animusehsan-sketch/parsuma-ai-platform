# Final Submission Notes: Parsuma AI Platform
**Course**: AI in Practice | Master’s in Applied AI Engineering
**Student**: Ehsan [Last Name]
**Project Title**: Parsuma AI: Multi-Agent Knowledge Intelligence Platform

---

## 1. Project Purpose
Parsuma AI is designed to bridge the gap between vast, unstructured institutional knowledge and the specific needs of intercultural digital publishing. It automates the extraction of insights from complex documents, ensuring that localized content strategies remain grounded in factual, original data.

## 2. Technologies Used
- **Language**: Python 3.10
- **Framework**: Streamlit (Advanced Dashboarding)
- **Orchestration**: Custom Multi-Agent Framework
- **Vector Database**: ChromaDB (On-device storage)
- **Embeddings**: `text-embedding-3-small` (OpenAI) for high-dimensional semantic mapping.
- **Inference**: `gpt-4o-mini` (OpenAI) for reasoning and synthesis.
- **Security**: Dotenv for environment management, Safety & Evaluation agents for output filtering.

## 3. AI Engineering Decisions

### **Vector Database Selection**
I chose **ChromaDB** for its lightweight, persistent nature. For a platform focusing on institutional knowledge, data privacy is paramount; local vector storage ensures that indices are not shared across third-party vector clouds unnecessarily.

### **Chunking Strategy**
We implemented **Recursive Character Chunking** with a 15% overlap. This preserves semantic context at the boundaries of chunks, which is critical for understanding complex academic or legal texts where meanings are often dependent on preceding sentences.

### **Multi-Agent Coordination**
The system uses a **federated agent model**. Instead of a single "God-prompt," the task is broken down:
1.  **Ingestion Agent**: Focuses on parsing and metadata extraction.
2.  **Retrieval Agent**: Focuses on semantic accuracy.
3.  **Synthesis Agent**: Focuses on tone and clarity.
4.  **Evaluation Agent**: Focuses on factual grounding.

## 4. RAG Implementation
Our Retrieval-Augmented Generation (RAG) pipeline includes:
- **Metadata Filtering**: Ensuring queries are targeted at the correct document subsets.
- **Context Injection**: Dynamically building system prompts with the most relevant $k$ document segments.
- **Citation Engine**: Mapping LLM output tokens back to the source chunks in the vector database.

## 5. Safety & Evaluation Strategy
To ensure the platform is "production-ready," we implemented:
- **Faithfulness Checks**: Verifying the response against retrieved chunks to prevent hallucinations.
- **Response Relevancy**: Measuring how well the answer satisfies the user's intent.
- **Safety Guardrails**: Hard-coded constraints to prevent the model from generating out-of-scope content (e.g., medical or financial advice not present in the docs).

## 6. Limitations
- **Context Window**: Extremely large documents (>500 pages) may require more advanced "Lost in the Middle" mitigation.
- **OCR**: Current implementation relies on text-based PDFs; image-heavy documents require an additional OCR layer (e.g., Tesseract or Azure Document Intelligence).

## 7. Future Work
- **Advanced Agentic Loops**: Implementing ReAct patterns to allow agents to "think" through multiple steps of research.
- **Multi-Modal RAG**: Including image and table extraction in the vector space.
- **Enterprise Integration**: Adding SSO and Role-Based Access Control (RBAC).
