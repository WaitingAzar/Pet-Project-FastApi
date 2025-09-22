import uuid
from pydantic import BaseModel, Field, root_validator


class Tasks(BaseModel):
    taskId: str = Field(default_factory=lambda: str(uuid.uuid4())[:6])
    id: str = None
    title: str = "завдання"
    category: str = "шопінг"
