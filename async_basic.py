# main.py — перші залежності
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()
GREETINGS = {"uk": "Привіт", "en": "Hello", "pl": "Cześć"}

def get_lang(lang: str = "uk") -> str:
    # залежність читає query-параметр ?lang=... і перевіряє його
    if lang not in GREETINGS:
        raise HTTPException(400, f"Невідома мова: {lang}")
    return lang

# Annotated-аліас: тип + залежність в одному імені
Lang = Annotated[str, Depends(get_lang)]

def get_greeting(lang: Lang) -> str:
    # залежність від залежності: спочатку get_lang, потім ця
    return GREETINGS[lang]

Greeting = Annotated[str, Depends(get_greeting)]

@app.get("/hello/{name}")
def hello(name: str, greeting: Greeting):
    return {"text": f"{greeting}, {name}!"}

@app.get("/lang")
def current_lang(lang: Lang):
    return {"lang": lang}
