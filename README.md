# Conversational RAG Backend

A FastAPI-based Conversational Retrieval-Augmented Generation (RAG) backend that allows users to upload documents and ask questions based on their content.

## Features

- Document upload and ingestion
- Text extraction and chunking
- Multiple chunking strategies
- Text embeddings
- Qdrant vector database for semantic search
- Retrieval-Augmented Generation (RAG)
- LLM-powered question answering
- Session-based conversational interaction
- Source/context retrieval
- Interview booking API
- SQLite database for document and booking metadata

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Qdrant
- Sentence Transformers
- LLM
- Pydantic
- Uvicorn

## Project Structure

```text
conversational-rag-backend/
│
├── app/
│   ├── api/
│   │   └── documents.py
│   │
│   ├── db/
│   │   ├── database.py
│   │   └── models.py
│   │
│   ├── schemas/
│   │   └── request.py
│   │
│   ├── services/
│   │   ├── chunking_service.py
│   │   ├── document_service.py
│   │   ├── embedding_service.py
│   │   ├── ingestion_service.py
│   │   ├── llm_service.py
│   │   ├── rag_service.py
│   │   ├── redis_service.py
│   │   └── vector_store.py
│   │
│   └── main.py
│
├── requirements.txt
├── test_embedding.py
├── test_llm.py
├── test_qdrant.py
├── test_rag.py
├── test_search.py
├── test_store.py
└── README.md
