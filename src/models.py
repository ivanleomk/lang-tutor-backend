from pydantic import Field, BaseModel
from typing import List


class UserConversationHistory(BaseModel):
    messages: List[str]


class Mistake(BaseModel):
    original_input: str = Field(
        ...,
        description="This is the original sentence from the user's response which contained a mistake. This can be a grammatical mistake or the wrong use of vocabulary",
    )
    correction: str = Field(
        ...,
        description="This is the corrected sentence which no longer has the user's mistake",
    )


class Vocabulary(BaseModel):
    vocabulary: str = Field(
        ...,
        description="This is a new phrase or word that the user should learn in the target language specified in the prompt.",
    )
    translation: str = Field(
        ...,
        description="This is what the new vocabulary item means in English. Make sure to provide a short description of how to use it too.",
    )


class LanguageResponse(BaseModel):
    response: str = Field(
        ...,
        description="This is a response to the user's latest message. Make sure to answer in the target language specificed in the prompt, this should be a question that will allow you to carry on the conversation quite naturally",
    )
    vocabulary: List[Vocabulary] = Field(
        ...,
        description="This is a list of strings containing relevant vocabulary in the target language that the user should learn. This includes phrases, idioms or even specific words. Provide 3 new vocabulary items at most",
        max_length=3,
    )
    mistakes: List[Mistake] = Field(
        ..., description="This is a list of mistakes that the user made"
    )
    translation: str = Field(
        ...,
        description="This is a English translation of your latest response to the user.",
    )
