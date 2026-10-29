from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Todos")

todos: dict[int, dict] = {}
next_id = 1

@app.get("/todos")
def list_tasks():
    return list(todos.values())

class TodoIn(BaseModel):
 title: str = Field(ge=1, le=100)
 desc: str = ""
 priority: int = Field(default=3, ge=1, le=5)

@app.post("/todos", status_code=201)
def create_task(todo: TodoIn):
   global next_id
   record = {"id": next_id, **todo.model_dump(), "done": False}
   todos[next_id] = record
   next_id += 1
   return record
