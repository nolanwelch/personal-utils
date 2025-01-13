from enum import Enum

from openai import OpenAI
from pydantic import BaseModel, Field


class RevisionResponse(BaseModel):
    can_answer: bool = Field(
        description="Whether or not you are able to complete this revision task."
    )
    revised_text: str = Field(
        description="The revised text, or an empty string if unable to answer."
    )


class MessageType(Enum):
    SLACK = "slack message"
    EMAIL = "email"


class RevisionClient:
    GPT_MODEL = "gpt-4o-mini"
    SCHEMA = RevisionResponse

    def __init__(self, api_key: str | None = None):
        self._client = OpenAI(api_key=api_key)

    def get_revision(
        self, user_text: str, msg_type: MessageType = MessageType.EMAIL
    ) -> str:
        response = (
            self._client.beta.chat.completions.parse(
                model=self.GPT_MODEL,
                response_format=self.SCHEMA,
                messages=[
                    {
                        "role": "system",
                        "content": "Revise the message below to improve tone, clarity, professionalism, and any other relevant features."
                        + " If you are unable to safely revise the message, you may indicate that in your response using can_answer=false.",
                    },
                    {
                        "role": "system",
                        "content": f"The message below is a(n) {msg_type}",
                    },
                    {"role": "user", "content": user_text},
                ],
            )
            .choices[0]
            .message.parsed
        )

        if response is None:
            raise ValueError("Got null response")

        elif not response.can_answer:
            raise RuntimeError("Could not revise the specified text")

        else:
            return response.revised_text
