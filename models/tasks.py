import uuid
from pydantic import BaseModel, Field




class Tasks(BaseModel):
    id: str = '0'
    title: str = "завдання"

