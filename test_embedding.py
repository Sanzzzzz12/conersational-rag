from app.services.embedding_service import EmbeddingService


service = EmbeddingService()

texts = [
    "Python is useful for artificial intelligence.",
    "I love eating pizza."
]

embeddings = service.generate_embeddings(texts)

print("Number of embeddings:", len(embeddings))
print("Vector size:", len(embeddings[0]))
print("First few numbers:", embeddings[0][:5])