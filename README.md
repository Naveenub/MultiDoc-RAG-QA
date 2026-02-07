# **Multi-Document RAG QA System**

Multi-Document RAG QA System is a research-grade, open-source platform designed for **question answering across multiple documents** using Retrieval-Augmented Generation (RAG). It is engineered to be universal, scalable, ML-driven, and explainable—not just another document search tool.

This is not a simple search engine. It is a **full end-to-end system** with multi-document ingestion, embedding pipelines, vector DB retrieval, LLM-based QA, RAG explanations, evaluation metrics, and interactive UI.

---

🚀 **Why This System Exists**

Current limitations in document QA systems:

* No open-source, research-grade multi-document QA pipeline
* No universal ingestion for PDFs, DOCX, TXT, or other file types
* No explainable reasoning when the system fails to answer accurately

This project addresses these gaps by providing:

* ML-assisted retrieval for heterogeneous documents
* Multi-stage RAG pipelines for answer generation
* Explainable reasoning using RAG to prevent hallucination
* Transparent evaluation with QA metrics and benchmarks
* Reproducible, production-ready deployment

---

🧠 **Core Design Goals**

* 🧩 **Universal** – supports PDF, DOCX, TXT, and more
* ⚡ **Adaptive & Efficient** – retrieves and ranks relevant documents intelligently
* 🔍 **Explainable** – RAG provides reasoning and citations
* 🎯 **Benchmark-first** – evaluates QA performance on multi-document corpora
* 🛠️ **Tool-aware** – integrates logs, embeddings, and file context
* 🔓 **Fully open** – MIT / Apache 2.0 license

---

📐 **System Overview**

The system treats QA as a **decision and retrieval problem** rather than just text generation.

| Stage                | Description                                                               |
| -------------------- | ------------------------------------------------------------------------- |
| Ingestion            | Reads documents, extracts metadata, text, and structure                   |
| Feature Extraction   | Chunking, tokenization, embedding creation                                |
| Vector DB Storage    | FAISS / Pinecone to store embeddings for retrieval                        |
| Retriever            | Finds relevant chunks for queries                                         |
| LLM QA Pipeline      | Generates context-aware answers from retrieved content                    |
| Explainer (RAG)      | Provides reasoning and citations when answers are incomplete or uncertain |
| Evaluator            | Computes F1, Exact Match, ROUGE, BLEU, hallucination metrics              |
| Frontend Interaction | React-based interface for uploads, queries, and answers                   |

---

📊 **ML & Embedding Overview**

The ML components do not answer questions directly but **guide retrieval and ranking**:

| Attribute  | Value                                                      |
| ---------- | ---------------------------------------------------------- |
| Model type | Random Forest / Transformer embeddings                     |
| Inputs     | Chunk embeddings, document metadata, prior query relevance |
| Outputs    | Ranked documents, predicted relevance scores               |
| Libraries  | Hugging Face, OpenAI embeddings, scikit-learn              |
| License    | MIT / Apache 2.0                                           |

---

🔍 **Retrieval-Augmented Generation (RAG)**

RAG ensures **accurate, explainable answers**:

* Uses embeddings and historical document context
* References only retrieved documents to prevent hallucination
* Generates actionable, human-readable explanations for uncertain answers
* Supports multi-document queries with context merging

---

🏗️ **Tech Stack**

| Layer              | Choice                               |
| ------------------ | ------------------------------------ |
| Backend            | FastAPI, Python 3.11                 |
| ML & Embeddings    | Hugging Face, OpenAI, scikit-learn   |
| Vector DB          | FAISS, Pinecone                      |
| LLM QA Pipeline    | OpenAI GPT / LLaMA or similar        |
| RAG                | LangChain + FAISS / Chroma           |
| Frontend UI        | React + Tailwind                     |
| PDF / DOCX Parsing | PyMuPDF, python-docx                 |
| Evaluation         | QA metrics & hallucination detection |
| Deployment         | Docker, Docker Compose, AWS EC2      |

---

🧱 **Repository Structure**

```
multi-doc-rag-qa/
├── README.md
├── LICENSE
├── .env.example
├── docker-compose.yml
├── backend/
│   ├── app.py                  # FastAPI main server
│   ├── config.py               # Configs (DB, embeddings, LLM)
│   ├── ingest.py               # Document ingestion pipeline
│   ├── retriever.py            # Vector DB retrieval
│   ├── llm.py                  # LLM query handling
│   ├── evaluator.py            # QA evaluation & metrics
│   ├── requirements.txt
│   └── utils/
│       ├── file_loader.py      # PDF, DOCX, TXT loaders
│       ├── text_splitter.py    # Chunking & tokenization
│       ├── embedding_utils.py  # Embedding creation & DB insertion
│       └── logger.py           # Logging utility
├── frontend/
│   ├── package.json
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── index.jsx
│       ├── App.jsx
│       ├── components/
│       │   ├── ChatWindow.jsx
│       │   ├── FileUploader.jsx
│       │   ├── QueryInput.jsx
│       │   └── EvaluationPanel.jsx
│       └── services/
│           ├── api.js          # API calls to backend
│           └── utils.js
├── ml/
│   ├── feature_engineering/
│   │   └── embedding_pipeline.py
│   ├── models/
│   │   └── local_models.py
│   └── training/
│       └── model_finetune.py
├── rag/
│   ├── pipelines/
│   │   ├── multi_doc_rag.py
│   │   ├── streaming_rag.py
│   │   └── evaluation_rag.py
│   └── vector_db/
│       ├── faiss_db.py         # FAISS vector DB integration
│       └── pinecone_db.py      # Pinecone alternative
├── tests/
│   ├── test_ingest.py
│   ├── test_retriever.py
│   ├── test_llm.py
│   └── test_api.py
├── .github/
│   └── workflows/
│       └── ci-cd.yml           # GitHub Actions CI/CD pipeline
└── docker/
    ├── Dockerfile.backend
    └── Dockerfile.frontend
```

---

🧱 **ASCII Architecture Diagram**

```
                                        ┌────────────────────────┐
                                        │       User / Client    │
                                        │  (Web UI, CLI, API)    │
                                        └────────────┬───────────┘
                                                     │
                                                     ▼
                                        ┌────────────────────────┐
                                        │     FastAPI Backend    │
                                        └────────────┬───────────┘
                                                     │
                                ┌───────────────┬───────────┬───────────────┐
                                │               │           │               │
                                ▼               ▼           ▼               ▼
                          ┌───────────┐   ┌───────────┐ ┌───────────┐ ┌───────────┐
                          │ Ingestion │   │ Retriever │ │ LLM QA    │ │ Evaluator │
                          └─────┬─────┘   └─────┬─────┘ └─────┬─────┘ └─────┬─────┘
                                │               │           │               │
                                ▼               ▼           ▼               ▼
                          ┌───────────┐   ┌───────────┐ ┌───────────┐ ┌───────────┐
                          │ File Load │   │ Vector DB │ │ RAG       │ │ Metrics   │
                          │ & Parsing │   │  (FAISS/  │ │ Explainer │ │ (F1, EM,  │
                          │ (PDF/DOCX)│   │ Pinecone) │ │           │ │ BLEU, etc)│
                          └───────────┘   └───────────┘ └───────────┘ └───────────┘

```

---

🧪 **Training & Ingestion Pipeline**

1. Collect diverse documents (PDF, DOCX, TXT)
2. Extract text and metadata
3. Chunk documents and generate embeddings
4. Store embeddings in vector DB (FAISS / Pinecone)
5. Evaluate QA retrieval, RAG explanations, and metrics
6. Fine-tune embedding model if necessary

---

🛠️ **Tool-Aware Reasoning**

* Grounded reasoning based on document embeddings
* Detects missing or ambiguous context
* Avoids hallucination by referencing only retrieved chunks

---

📊 **Evaluation & Metrics**

* F1-score, Exact Match, ROUGE, BLEU
* Hallucination detection
* Retrieval relevance & ML strategy accuracy

---

🌐 **Quick Start (Docker)**

```bash
docker build -t multi-doc-rag-qa .
docker run -p 8000:8000 multi-doc-rag-qa
```

Visit: [http://localhost:8000](http://localhost:8000)

---

⚖️ **License**

Apache 2.0

---

⚠️ **Disclaimer**

Fully research-grade, open-source project.
No magical QA claims. Fully transparent, reproducible, and explainable.

---

📘 Detailed Case Study:

🔗 Notion Portfolio: https://trail-bramble-8d5.notion.site/Naveen-Badiger-DevOps-Cloud-Engineer-300b680e255b80618978c2654214a6c6
