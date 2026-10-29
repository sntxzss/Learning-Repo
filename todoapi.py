from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Todos")

todos: dict[int, dict] = {}

@app.get("/todos")
def list_tasks():
    return list(todos.values())

class TodoIn(BaseModel):
 title: str = Field(ge=1, le=100)
 desc: str = ""
 priority: int = Field(default=3, ge=1, le=5)
