from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import os

from app.services.ingestion_service import IngestionService
from app.services.rag_service import RAGService

from app.db.database import Base, engine
from app.db import models


app = FastAPI(
    title="Conversational RAG Backend",
    description="A document-based conversational RAG API",
    version="1.0.0"
)


# -----------------------------
# Create SQL tables
# -----------------------------

Base.metadata.create_all(bind=engine)


# -----------------------------
# Services
# -----------------------------

ingestion_service = IngestionService()

rag_service = RAGService(
    embedding_service=ingestion_service.embedding_service,
    vector_store=ingestion_service.vector_store
)


# -----------------------------
# Request Model
# -----------------------------

class QuestionRequest(BaseModel):
    question: str
    session_id: str = "default"


# -----------------------------
# Home
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "Conversational RAG Backend is running!"
    }


# -----------------------------
# Health Check
# -----------------------------

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# -----------------------------
# Upload Document
# -----------------------------

@app.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    result = ingestion_service.ingest_pdf(
        file_path
    )

    return {
        "filename": file.filename,
        **result
    }


# -----------------------------
# Ask Question
# -----------------------------

@app.post("/ask")
def ask_question(request: QuestionRequest):

    result = rag_service.ask(
        question=request.question,
        session_id=request.session_id
    )

    return result