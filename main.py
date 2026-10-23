from fastapi import FastAPI, HTTPException

app = FastAPI(title="Books API")

bd = [
 {"id": 1, "title": "Typeshi", "author": "sntxzss"}   
]

@app.get("/books")
def books(author: str | None = None):
  if author is None:
   return bd
  return [b for b in bd if b["author"].lower() == author.lower()]

@app.get("/books/{bk_id}")
def book_by_id(bk_id: int | None = None):
  if bk_id is None:
    return None
  for book in bd:
    if book["id"] == bk_id:
     return book