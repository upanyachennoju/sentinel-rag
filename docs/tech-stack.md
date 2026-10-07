| Layer | Choice | Why |
|---|---|---|
| Language | **Python** | ML/RAG ecosystem |
| API | **FastAPI** | Clean async API + easy auth/deployment |
| Agent orchestration | **LangGraph** | Stateful verification/retrieval workflow |
| LLM | **Groq initially** | Fast + inexpensive experimentation |
| Embeddings | **BGE / similar open embedding model** | Strong retrieval without depending entirely on proprietary APIs |
| Vector DB | **PostgreSQL + pgvector** | Production-style relational + vector storage |
| Keyword search | **PostgreSQL full-text/BM25-style search** | Hybrid retrieval |
| Reranker | **Cross-encoder / BGE reranker** | Improve relevance after initial retrieval |
| Auth | **JWT + RBAC** | Role-based document access |
| Evaluation | **RAGAS + custom security/eval tests** | Measure RAG quality and security |
| Experiment tracking | **MLflow** | Compare retrieval/RAG experiments |
| Observability | **LangSmith** | Trace LangGraph execution |
| UI | **Streamlit initially** | Fastest way to demo |
| Containers | **Docker + Compose** | Reproducible deployment |
| CI | **GitHub/GitLab CI** | Automated tests/evals |
| Testing | **pytest** | Unit/integration/security tests |