from fastapi import FastAPI

app = FastAPI()

@app.get("/add")
def add(a: float, b: float):
    return{"a": a, "b": b, "Add": a +  b}

@app.get("multiply") 
def multiply(a: float, b: float):
    return{"a": a, "b": b, "multiply": a *  b}

