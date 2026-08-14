from app.services.chunking_service import (
    fixed_size_chunking,
    sentence_chunking
)
from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore
from app.services.document_service import DocumentService


class IngestionService:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()
        self.document_service = DocumentService()

        self.vector_store.create_collection()

    def ingest_text(
        self,
        text: str,
        chunk_strategy: str = "fixed"
    ):

        if chunk_strategy == "fixed":
            chunks = fixed_size_chunking(
                text,
                chunk_size=500,
                overlap=50
            )

        elif chunk_strategy == "sentence":
            chunks = sentence_chunking(
                text,
                sentences_per_chunk=5
            )

        else:
            raise ValueError(
                "Invalid chunk strategy. "
                "Use 'fixed' or 'sentence'."
            )

        if not chunks:
            return {
                "message": "No text found.",
                "chunks": 0,
                "chunk_strategy": chunk_strategy
            }

        embeddings = self.embedding_service.generate_embeddings(
            chunks
        )

        for index, (chunk, embedding) in enumerate(
            zip(chunks, embeddings),
            start=1
        ):
            self.vector_store.add_vector(
                vector=embedding,
                text=chunk,
                vector_id=index
            )

        return {
            "message": "Document ingested successfully.",
            "chunks": len(chunks),
            "chunk_strategy": chunk_strategy
        }

    def ingest_pdf(
        self,
        file_path: str,
        chunk_strategy: str = "fixed"
    ):

        text = self.document_service.extract_text_from_pdf(
            file_path
        )

        return self.ingest_text(
            text,
            chunk_strategy
        )