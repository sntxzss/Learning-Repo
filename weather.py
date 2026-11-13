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

