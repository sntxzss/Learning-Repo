from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")         
def read_current_user():
    return {"user": "That's me"}

@app.get("/users/{user.id}")
def users(user_id: int):
    return {"user_id": user_id, "next_id": user_id + 1}