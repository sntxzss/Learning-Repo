from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/admin")
def admin():
    return{"Message": "Hello, Admin"}    

@app.get("/hello/{name}")
def hello(name: str):
    return{"Message": f"Hello, {name}"}         

@app.get("/square/{sqr}")
def square(sqr:int):
    return{f"Square of {sqr}": sqr * sqr}
