from fastapi import FastAPI
from pydantic import BaseModel, ValidationError, Field

app = FastAPI(title="Notes Rework")

class NoteBase(BaseModel):
    title: str = Field(ge=1, le=100)
    desc: str = ""
    pinned: bool = False

id = 1

class NoteCreate(NoteBase):
    pass

class NoteRead(NoteBase):
    id: int

class NoteUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    desc: str | None = None
    pinned: bool | None = None


   

