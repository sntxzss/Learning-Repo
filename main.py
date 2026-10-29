from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class UserCreate(BaseModel):          # що надсилає клієнт
    username: str = Field(min_length=3)
    password: str = Field(min_length=8)

class UserRead(BaseModel):            # що бачить клієнт
    id: int
    username: str

users: dict[int, dict] = {}

@app.post("/users", response_model=UserRead, status_code=201)
def create_user(data: UserCreate):
    user_id = len(users) + 1
    # зберігаємо все, навіть пароль (у справжньому житті — лише хеш!)
    users[user_id] = {"id": user_id, **data.model_dump()}
    return users[user_id]             # пароль відфільтрує response_model

@app.get("/users", response_model=list[UserRead])
def list_users():
    return list(users.values())
