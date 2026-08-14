from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore


query = "What is Python useful for?"

embedding_service = EmbeddingService()
vector_store = VectorStore()

query_vector = embedding_service.generate_embeddings([query])[0]

results = vector_store.search(query_vector)

print("\nSEARCH RESULTS:")
print("----------------")

for result in results:
    print("Score:", result.score)
    print("Text:", result.payload["text"])
    print()