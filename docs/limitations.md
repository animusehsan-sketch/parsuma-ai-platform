# Constraints, Limitations & Future Roadmap

While Parsuma AI implements a robust multi-agent architecture, certain technical and environmental constraints exist. This document provides a transparent overview of these limitations and the proposed roadmap for future development.

---

## 1. Technical Constraints

### **Context Window & "Lost in the Middle"**
Despite using models with large context windows, RAG systems can suffer from performance degradation when too many chunks are injected. We currently limit retrieval to $k=5$, which may exclude secondary supporting evidence in extremely dense documents.

### **Document Parsing (OCR)**
The current implementation relies on standard text-extraction libraries (`PyPDF2`, `python-docx`). Documents that are primarily image-based or contain complex non-linear tables may not be fully vectorized without an additional OCR (Optical Character Recognition) layer.

### **Dependency on External APIs**
The synthesis and reasoning layers are dependent on OpenAI's API availability. High latency or API outages directly impact the "Strategy Studio" and "Research Chat" functionality.

---

## 2. Security & Privacy

### **Vector Data at Rest**
While embeddings are generated locally, the persistent storage in `chroma_db/` is not currently encrypted at the application level. Users are responsible for securing the host environment (Docker/Server) where the database resides.

---

## 3. Future Roadmap

### **Phase 1: Agentic Reasoning (Short-term)**
- Implement the **ReAct (Reasoning + Acting)** pattern to allow agents to perform iterative searches if the first retrieval is insufficient.
- Add support for **Hybrid Search** (Keyword + Semantic) to handle specific technical terminology more effectively.

### **Phase 2: Multi-Modality (Mid-term)**
- Integration of **GPT-4o Vision** capabilities to allow the "Document Intelligence Agent" to analyze charts, infographics, and layout structures.
- Support for image-based PDF ingestion via Tesseract OCR.

### **Phase 3: Enterprise Integration (Long-term)**
- **User Authentication**: Implementing SSO and Role-Based Access Control (RBAC).
- **Evaluation Dashboard**: A dedicated UI for real-time RAGAS-style evaluation metrics.
- **Asynchronous Ingestion**: Moving document processing to a background task (Celery/Redis) for large-scale asset libraries.
