from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore


text = "Python is useful for artificial intelligence."

embedding_service = EmbeddingService()
vector_store = VectorStore()

vector = embedding_service.generate_embeddings([text])[0]

vector_store.create_collection()
vector_store.add_vector(vector, text,1)