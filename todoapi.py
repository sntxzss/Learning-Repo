from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime

app = FastAPI(title="Todos")

todos: dict[int, dict] = {}
next_id = 1

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

class TodoUpdate(BaseModel):
   title: str | None = Field(default=None, min_length=1, max_length=100)
   desc: str | None = None
   priority: int | None = Field(default=None, ge=1, le=5)
   done: bool | None = None

def get_todo_or_404(todo_id: int) -> dict:
   if todo_id not in todos:
      raise HTTPException(status_code=404, detail="Todo not found")
   return todos[todo_id]

@app.get("/todos/{todo_id}", response_model=TodoRead)
def get_task(todo_id: int):
    return get_todo_or_404(todo_id)

@app.get("/todos", response_model=list[TodoRead])
def list_tasks():
    return list(todos.values())

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

@app.patch("/todos/{todo_id}", response_model=TodoRead)
def update_task(todo_id: int, data: TodoUpdate):
   task = get_todo_or_404(todo_id)
   task.update(data.model_dump(exclude_unset=True))
   return task

@app.delete("/todos/{todo_id}", status_code=204)
def delete_task(todo_id: int):
   get_todo_or_404(todo_id)
   del todos[todo_id]
