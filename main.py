from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")         
def read_current_user():
    return {"user": "That's me"}
