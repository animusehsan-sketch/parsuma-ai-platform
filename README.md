# 🌌 Parsuma AI | Knowledge Intelligence Platform
> **A Master’s Level Multi-Agent RAG System for Intercultural Digital Publishing**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/AI-OpenAI%20GPT--4o--mini-412991.svg?logo=openai&logoColor=white)](https://openai.com/)
[![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-00ADD8.svg?logo=chroma&logoColor=white)](https://www.trychroma.com/)
[![Docker](https://img.shields.io/badge/Deployment-Docker-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Project Overview

**Parsuma AI** is a production-grade Knowledge Intelligence platform engineered as a **Final Project for the Master’s Program in Applied AI Engineering**. 

The platform addresses the complex challenge of **Intercultural Digital Publishing** by providing an intelligent orchestration layer between unstructured institutional knowledge and global content strategy. By leveraging state-of-the-art **Retrieval-Augmented Generation (RAG)**, Parsuma AI enables organizations to transform vast document repositories into actionable, localized, and culturally sensitive publishing roadmaps.

---

## 🏗️ Architecture & Engineering
The system is built on a **Federated Agentic Framework**, moving beyond simple RAG scripts into a decentralized ecosystem of specialized agents.

- **[Full Architecture Overview](docs/architecture_overview.md)**: Detailed Mermaid diagrams and structural pillars.
- **[AI Engineering Decisions](docs/ai_engineering_decisions.md)**: Rationale for our model selection and vector core.

---

## 🌟 Core Features
- **⚡ Neural Intelligence**: Advanced semantic search using the `all-MiniLM-L6-v2` transformer.
- **🤖 Multi-Agent Orchestration**: Specialized agents for Ingestion, Retrieval, and Content Strategy.
- **🛡️ Safety & Trust**: Real-time faithfulness evaluation and citation mapping.
- **🎨 Premium UI**: A futuristic glassmorphism dashboard designed for institutional users.

---

## 📊 Quantitative Evaluation
To ensure Master's level rigour, the platform is benchmarked against the RAG Triad:
- **Faithfulness**: > 0.90 (Verified grounding)
- **Relevancy**: > 0.85 (Semantic alignment)
- **Context Precision**: > 0.80 (Retrieval accuracy)

For the full evaluation report, see **[docs/evaluation.md](docs/evaluation.md)**.

---

## 🚀 Installation & Deployment

### 1. Prerequisites
- Python 3.10+ | Docker | OpenAI API Key

### 2. Local Setup
```bash
git clone https://github.com/animusehsan-sketch/parsuma-ai-platform.git
cd parsuma-ai-platform
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file (see `.env.example`):
```bash
OPENAI_API_KEY=sk-...
MODEL_NAME=gpt-4o-mini
```

### 4. Run Application
```bash
streamlit run app.py
```

For containerized deployment, see the **[Deployment Section](docs/architecture_overview.md#3-docker-deployment)**.

---

## 🛡️ Safety, Limitations & Future Roadmap
Every AI system has boundaries. We document our constraints and future plans transparently.

- **[Current Limitations](docs/limitations.md)**: Context window challenges and OCR constraints.
- **[Ethical AI & Safety](docs/evaluation.md#3-safety--hallucination-guardrails)**: Implementation of grounding guardrails.
- **[Future Roadmap](docs/limitations.md#3-future-roadmap)**: Multi-modal RAG and ReAct reasoning loops.

---

## 📂 Project structure
```text
├── app.py              # Dashboard Entry Point
├── src/                # Agent & RAG Logic
├── docs/               # Master-Grade Documentation
│   ├── architecture_overview.md
│   ├── evaluation.md
│   ├── ai_engineering_decisions.md
│   └── limitations.md
├── tests/              # Reliability Suite
└── requirements.txt    # Production Dependencies
```

---

## 👨‍💻 Author
**Ehsan [Last Name]** | *Applied AI Engineering Student*  
[Xamk - South-Eastern Finland University of Applied Sciences](https://www.xamk.fi/)

---
*This repository is finalized for Master’s level academic submission.*
