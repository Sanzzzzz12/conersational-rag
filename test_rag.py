from app.services.rag_service import RAGService


rag = RAGService()

question = "What is Python useful for?"

result = rag.ask(question)

print("\nQUESTION:")
print(result["question"])

print("\nANSWER:")
print(result["answer"])

print("\nSOURCES:")
for source in result["sources"]:
    print("-", source)