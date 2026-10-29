from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class MessageIn(BaseModel):
    author: str = Field(min_length=2, max_length=30)
    text: str = Field(min_length=1, max_length=200)

messages: list[dict] = []   # «база даних» у пам'яті
next_id = 1                  # лічильник для нових id

@app.post("/messages", status_code=201)
def create_message(message: MessageIn):   # модель -> береться з тіла
    global next_id
    record = {"id": next_id, **message.model_dump()}
    messages.append(record)
    next_id += 1
    return record                          # повертаємо запис з id

@app.get("/messages")
def list_messages():
    return messages
