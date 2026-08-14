from app.services.llm_service import LLMService


llm = LLMService()

question = "What is Python useful for?"

context = """
Python is useful for artificial intelligence.
It is commonly used for machine learning and data analysis.
"""

answer = llm.generate_answer(question, context)

print("\nANSWER:")
print(answer)