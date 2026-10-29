from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime

app = FastAPI(title="Todos")

todos: dict[int, dict] = {}
next_id = 1

@app.get("/todos", response_model=list[TodoRead])
def list_tasks():
    return list(todos.values())

class TodoBase(BaseModel):
 title: str = Field(ge=1, le=100)
 desc: str = ""
 priority: int = Field(default=3, ge=1, le=5)

class TodoCreate(TodoBase):
   pass

class TodoRead(TodoBase):
   id: int 
   done: bool
   created_at: str


@app.post("/todos", status_code=201, response_model=TodoRead)
def create_task(todo: TodoCreate):
   global next_id
   record = {
      "id": next_id,
      **todo.model_dump(),
      "done": False,
      "created_at": datetime.now().isoformat(timespec="seconds"),
      "source": "api"
   }
   todos[next_id] = record
   next_id += 1
   return record
