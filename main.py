from fastapi import FastAPI, HTTPException

app = FastAPI(title="Movies API")

MOVIES = [
    {"id":1 ,"title":"Mark","year": 2222,"genre": "Thriller","rating": 1},
    {"id":2 ,"title":"Sntxzss" ,"year": 2000,"genre": "Romantic","rating": 5},
    {"id":3 ,"title":"Anna" ,"year": 1902,"genre": "Romantic","rating": 3},
    {"id":4 ,"title":"Kevin" ,"year": 2039,"genre": "Thriller","rating": 5},
    {"id":5 ,"title":"Andreq" ,"year": 9000,"genre": "Absolute Cinema","rating": 6},
    {"id":6 ,"title":"2 Years" ,"year": 2039,"genre": "Trash","rating": 7}
]

@app.get("/movies")
def allmovies():
    return MOVIES

@app.get("/movies/id/{m_id}")
def find_id(m_id: int):
    for movie in MOVIES:
        if movie["id"] == m_id:
            return movie
    raise HTTPException(status_code=404, detail="Not found")

@app.get("/movies/genre/{genre}")
def find_genre(genre: str):
    results = [movie for movie in MOVIES if movie["genre"].lower() == genre.lower()]
    if results:
        return results
    raise HTTPException(status_code=404, detail="Not Found")
