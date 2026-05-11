# System Evaluation & Metrics: Parsuma AI

This document outlines the evaluation framework used to validate the reliability, accuracy, and safety of the Parsuma AI platform. As an Applied AI Engineering project, rigorous quantitative measurement is central to our development lifecycle.

---

## 1. RAG Triad Metrics
We utilize the "RAG Triad" to measure the performance of our Retrieval-Augmented Generation pipeline:

### **A. Faithfulness (Groundedness)**
- **Definition**: Is the answer derived solely from the retrieved context?
- **Target**: > 0.90
- **Measurement**: Our **Evaluation Agent** performs a claim-level extraction from the LLM response and cross-references each claim against the retrieved chunks in ChromaDB.

### **B. Answer Relevancy**
- **Definition**: Does the response actually address the user's query?
- **Target**: > 0.85
- **Measurement**: Calculated via semantic similarity (Cosine Distance) between the original user query and the generated response.

### **C. Context Precision**
- **Definition**: Are the retrieved chunks actually relevant to the query?
- **Target**: > 0.80
- **Measurement**: Benchmarked against a "Golden Dataset" of curated question-context pairs.

---

## 2. Quantitative Performance Benchmarks

| Metric | Target | Result (v1.0) | Status |
| :--- | :--- | :--- | :--- |
| **Response Latency** | < 2.0s | 1.45s | ✅ Optimized |
| **Retrieval Confidence** | > 75% | 82.4% | ✅ High |
| **Safety Violation Rate**| < 0.01% | 0.00% | ✅ Secure |
| **Token Efficiency** | < 2k/q | 1.4k/q | ✅ Efficient |

---

## 3. Safety & Hallucination Guardrails
The **Safety Agent** implements a multi-step verification process:
1.  **Input Filtering**: Detecting adversarial prompts and out-of-scope requests.
2.  **Context Verification**: Ensuring that at least 3 chunks with a similarity score > 0.7 exist before allowing generation.
3.  **Hallucination Check**: If the LLM generates a response that cannot be mapped back to a source ID, the response is flagged and the user is notified of the "low confidence" status.

---

## 4. User-Centric Qualitative Feedback
Beyond raw metrics, Parsuma AI is evaluated on its **Intercultural Utility**:
- **Strategy Coherence**: Does the "Strategy Studio" provide actionable, non-generic advice?
- **Citation Clarity**: Are source links intuitive and accurate for an academic/institutional user?
- **Visual Telemetry**: Does the dashboard effectively communicate system "confidence" to the end-user?
