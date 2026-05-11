# Parsuma AI: Demo Scenarios & User Workflows

This document provides a set of standardized demo scenarios to showcase the full capabilities of the Parsuma AI Knowledge Intelligence Platform. These scenarios are designed for evaluators, stakeholders, and developers to verify system functionality.

---

## Scenario 1: Knowledge Ingestion & Vectorization
**Objective**: Successfully ingest institutional documents and prepare them for semantic retrieval.

1.  **Action**: Navigate to the **Knowledge Base** (Document Upload) section.
2.  **Input**: Upload a sample document (e.g., `Nordic_Marketing_Strategy.pdf`).
3.  **Observation**: 
    - The system displays a progress bar during text extraction.
    - Chunks are generated and vectorized using the embedding model.
    - A success message confirms the document is indexed in ChromaDB.
4.  **Verification**: The "Database Statistics" updated to show the new document and total chunk count.

---

## Scenario 2: Deep-Dive RAG Research
**Objective**: Query the knowledge base and receive a grounded answer with citations.

1.  **Action**: Navigate to the **AI Research Chat**.
2.  **Prompt**: *"What are the primary cultural barriers identified in our expansion strategy for the Persian market?"*
3.  **System Process**:
    - Query is vectorized.
    - Top-k relevant chunks are retrieved from ChromaDB.
    - LLM synthesizes an answer using ONLY the retrieved context.
4.  **Expected Result**:
    - A detailed answer citing specific sections of the uploaded documents.
    - A "Source Citations" expander showing the exact text snippets used.
    - A confidence score above 0.8.

---

## Scenario 3: Intercultural Strategy Generation
**Objective**: Use the **Strategy Studio** to generate actionable publishing roadmaps.

1.  **Action**: Navigate to the **Strategy Studio**.
2.  **Input**:
    - **Target Region**: Middle East / Iran.
    - **Content Type**: Educational Webinar Series.
    - **Tone**: Academic & Formal.
3.  **Prompt**: *"Generate a 3-month localized publishing roadmap that respects local visual taboos and emphasizes our Nordic reliability."*
4.  **Expected Result**:
    - A structured table or list with monthly milestones.
    - Localization tips (e.g., "Avoid specific color palettes," "Emphasize high-quality translations").
    - Integration of Nordic values found in the knowledge base.

---

## Scenario 4: Safety & Hallucination Check
**Objective**: Verify the system's refusal to answer out-of-scope or ungrounded queries.

1.  **Action**: Navigate to **AI Research Chat**.
2.  **Prompt**: *"What is the recipe for a chocolate cake?"* (Assuming no cake recipes are in the knowledge base).
3.  **Expected Result**:
    - System Response: *"I'm sorry, but I cannot find any information regarding cake recipes in the provided knowledge base. My expertise is limited to the uploaded institutional documents."*
4.  **Evaluation**: Check the **Evaluation** tab to see the "Grounding Score" (should be 0 or N/A).

---

## Scenario 5: System Telemetry & Evaluation
**Objective**: Audit the performance and reliability of the AI agents.

1.  **Action**: Navigate to the **Evaluation & Logs** dashboard.
2.  **Observation**:
    - View the distribution of **Faithfulness** and **Relevancy** scores for recent queries.
    - Inspect the **Latency Graph** to see response times.
    - Review the **Safety Logs** for any flagged adversarial attempts.

---

## Summary of RAG Query Examples
| Context | Example Prompt |
| :--- | :--- |
| **Expansion** | "Summarize the financial risks of the Berlin office opening." |
| **Branding** | "What are our core brand colors and font guidelines?" |
| **Legal** | "Does our privacy policy comply with the new EU regulations mentioned in the audit?" |
| **Creative** | "Suggest 5 blog titles for the 'Nordic Minimalism' campaign based on the style guide." |
