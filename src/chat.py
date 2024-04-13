import instructor
import anthropic
from typing import List
from src.models import LanguageResponse


def generate_language_response(conversation_history: List[str]):
    client = client = instructor.from_anthropic(anthropic.Client())
    messages = [
        {
            "role": "user",
            "content": "You are a helpful and enthusiastic language tutor called Andre who wants to help a user learn Spanish. Make sure to respond in Spanish first to the User's messages but at the end of your respond, provide a small translation of what you have said in English at the end.",
        },
        *[{"role": "user", "content": message} for message in conversation_history],
    ]
    response = client.chat.completions.create(
        response_model=LanguageResponse,
        messages=messages,
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        max_retries=2,
    )
    return response
