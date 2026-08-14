import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


class LLMService:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is missing from .env"
            )

        self.client = genai.Client(
            api_key=api_key
        )

    def generate_answer(
        self,
        question: str,
        context: str,
        history: list
    ) -> str:

        # Convert Redis history into readable text

        conversation = ""

        for message in history:

            role = message.get("role", "")
            content = message.get("content", "")

            conversation += (
                f"{role}: {content}\n"
            )

        prompt = f"""
You are a helpful document assistant.

You answer questions using the provided document context.

You also have access to previous conversation history.

Use the conversation history to understand references
such as:
- she
- he
- it
- they
- that
- previous questions

IMPORTANT:
Answer using ONLY information supported by the
document context and conversation history.

If the answer cannot be found, say:

"I don't have enough information in the provided documents."

Previous Conversation:
{conversation}

Document Context:
{context}

Current Question:
{question}

Answer:
"""

        interaction = self.client.interactions.create(
            model="gemini-3.6-flash",
            input=prompt
        )

        return interaction.output_text