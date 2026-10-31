class Movie(BaseModel):
 title: str = Field(ge=1, le=200)
 year: int = Field(ge=1888, le=2100)
 rating: float = Field(ge=0, le=10)

def valid_check(movie: str):
 try:
  movie
 except ValueError:
  print("Hello, world")
 