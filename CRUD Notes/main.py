# main.py — лабораторія кодів статусу
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()
rooms: dict[str, dict] = {}       # ключ — назва кімнати в нижньому регістрі

class Room(BaseModel):
    name: str = Field(min_length=2)
    capacity: int = Field(ge=1)

@app.post("/rooms", status_code=status.HTTP_201_CREATED)
def create_room(room: Room):
    key = room.name.lower()
    if key in rooms:              # така назва вже є -> конфлікт
        raise HTTPException(409, f"Room '{room.name}' already exists")
    rooms[key] = room.model_dump()
    return rooms[key]

@app.get("/rooms/{name}")
def get_room(name: str):
    if name.lower() not in rooms:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Room not found")
    return rooms[name.lower()]

@app.get("/rooms")
def find_rooms(min_cap: int = 1, max_cap: int = 100):
    if min_cap > max_cap:         # запит безглуздий -> 400
        raise HTTPException(400, "min_cap must be <= max_cap")
    return [r for r in rooms.values() if min_cap <= r["capacity"] <= max_cap]
