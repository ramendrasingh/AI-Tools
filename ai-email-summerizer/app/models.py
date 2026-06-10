from typing import Literal
from pydantic import BaseModel

class EmailRequest(BaseModel):
    email: str

class ActionItem(BaseModel):
    task: str
    owner: str
    deadline: str


class EmailSummeryResponse(BaseModel):
    summary: str
    priority: Literal["low", "medium", "high"]
    sentiment: Literal["positive", "negative", "neutral"]
    action_items: list[ActionItem]
    suggested_reply: str

