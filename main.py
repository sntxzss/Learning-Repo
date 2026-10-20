from fastapi import FastAPI

app = FastAPI(title="Hello, API")

@app.get("/")
def main():
    return{"message": "Hello, FastAPI"}

@app.get("/about")
def about_page():
    return{"city": "Los Angeles"}

@app.get("/skills")
def skills():
    return["FastAPI","Test",".venv"]