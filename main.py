from typing import List
from fastapi import FastAPI
from src.models import UserConversationHistory
from src.chat import generate_language_response

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "Ok"}


@app.post("/chat")
def reply_to_user(response: UserConversationHistory):
    return generate_language_response(response.messages)
