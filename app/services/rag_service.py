from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore
from app.services.llm_service import LLMService
from app.services.redis_service import RedisService


class RAGService:

    def __init__(
        self,
        embedding_service: EmbeddingService,
        vector_store: VectorStore
    ):
        self.embedding_service = embedding_service
        self.vector_store = vector_store
        self.llm_service = LLMService()
        self.redis_service = RedisService()

    def ask(self, question: str, session_id: str = "default"):

        # --------------------------------
        # 1. Get previous conversation
        # --------------------------------

        history = self.redis_service.get_history(session_id)

        # --------------------------------
        # 2. Convert question into embedding
        # --------------------------------

        query_vector = self.embedding_service.generate_embeddings(
            [question]
        )[0]

        # --------------------------------
        # 3. Search Qdrant
        # --------------------------------

        results = self.vector_store.search(
            query_vector,
            limit=3
        )

        # --------------------------------
        # 4. Extract retrieved context
        # --------------------------------

        context_parts = []

        for result in results:

            text = result.payload.get("text", "")

            if text:
                context_parts.append(text)

        context = "\n\n".join(context_parts)

        # --------------------------------
        # 5. Generate answer
        # --------------------------------

        answer = self.llm_service.generate_answer(
            question=question,
            context=context,
            history=history
        )

        # --------------------------------
        # 6. Save conversation to Redis
        # --------------------------------

        history.append({
            "role": "user",
            "content": question
        })

        history.append({
            "role": "assistant",
            "content": answer
        })

        self.redis_service.save_history(
            session_id,
            history
        )

        # --------------------------------
        # 7. Return response
        # --------------------------------

        return {
            "question": question,
            "answer": answer,
            "sources": context_parts,
            "session_id": session_id
        }