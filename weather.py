from typing import Annotated
from fastapi import Depends, FastAPI

app = FastAPI()

def get_logbook():
    logbook = [] 
    print("ВІДКРИЛИ журнал")
    try:
        yield logbook
    finally:
        print("ЗАКРИЛИ журнал, записів:", len(logbook))  # навіть після помилки

Logbook = Annotated[list, Depends(get_logbook)]

class Filters:
    def __init__(self, city: str = "Kyiv", min_temp: int = 0):
        self.city = city
        self.min_temp = min_temp

def note_city(logbook: Logbook, f: Annotated[Filters, Depends()]):
    logbook.append(f"місто {f.city}")

@app.get("/weather", dependencies=[Depends(note_city)])
def weather(logbook: Logbook, f: Annotated[Filters, Depends()]):
    logbook.append("відповідь")  
    return {"city": f.city, "min_temp": f.min_temp, "log": logbook}