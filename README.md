# Sentinel RAG

An enterprise-ready Retrieval-Augmented Generation (RAG) system built with FastAPI and LangGraph. Sentinel RAG is designed to securely answer questions from internal company documentation while enforcing strict role-based access control (RBAC).

## Key Features

- **Role-Based Access Control (RBAC)**: Documents are tagged with security labels (e.g., `ADMIN`, `FINANCE`, `HR`) and users are assigned roles. The system automatically filters out documents the user does not have permission to view.
- **Claim-Level Verification**: Unlike standard RAG, Sentinel verifies each claim in the generated answer against the retrieved documents. If a claim is not supported by the evidence, it is omitted from the final response, preventing hallucinations.
- **Hybrid Retrieval**: Combines semantic search (vector similarity) with traditional keyword search (BM25) to ensure relevant results are retrieved even for very specific or technical queries.
- **Traceability & Observability**: Full integration with LangSmith for detailed tracing of every node execution, cost tracking, and debugging.
- **Evaluation Framework**: Built-in `RAGAS` integration and custom evaluation scripts to measure retrieval quality, answer faithfulness, and security compliance.
- **Modular Architecture**: Built on FastAPI with a clear separation between the API layer, agent logic, retrieval components, and UI.

## Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **API Framework** | `FastAPI` | High-performance web server and API layer |
| **Agent Orchestration** | `LangGraph` | Stateful, graph-based workflow engine for the verification loop |
| **LLM** | `Groq` (default) | Fast inference for generation and verification steps |
| **Embeddings** | `BGE` (Open Source) | High-performance semantic embeddings for retrieval |
| **Database** | `PostgreSQL + pgvector` | Primary storage for document metadata and vector embeddings |
| **Keyword Search** | PostgreSQL Full-Text Search | Hybrid retrieval combined with vector search |
| **Reranker** | `Cross-encoder / BGE Reranker` | Improves retrieval precision |
| **Security** | `JWT + RBAC` | Authentication and authorization |
| **Evaluation** | `RAGAS + Custom Tests` | Metrics for RAG quality and security |
| **Experiment Tracking** | `MLflow` | Logging and comparing retrieval experiments |
| **Observability** | `LangSmith` | Tracing and monitoring of agent execution |
| **UI** | `Streamlit` | Rapid development of the user interface |
| **Containerization** | `Docker + Docker Compose` | Reproducible and isolated deployment |
| **Testing** | `pytest` | Unit, integration, and security tests |

## Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/upanyachennoju/sentinel-rag.git
    cd sentinel-rag
    ```

2.  **Install Dependencies:**
    Create a virtual environment and install the required packages.
    ```bash
    python3.12 -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Configuration:**
    Copy the example environment file and fill in your credentials.
    ```bash
    cp .env.example .env
    # Edit .env with your API keys and database URL
    ```

4.  **Run the Application:**
    Start the FastAPI server using Uvicorn.
    ```bash
    uvicorn app.main:app --reload
    ```
    The API will be available at `http://localhost:8000`.

## Running Tests

Run the built-in test suite to verify the system's functionality:
```bash
pytest
```
