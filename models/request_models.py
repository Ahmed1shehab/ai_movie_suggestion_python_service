from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class MovieRequest(BaseModel):
    prompt: str

class Genre(BaseModel):
    id: int
    name: str

class Language(BaseModel):
    english_name: str
    iso_639_1: str
    name: str

class MovieResponse(BaseModel):
    title: str
    overview: str
    poster_url: Optional[HttpUrl]
    imdb_link: Optional[HttpUrl]
    trailer: Optional[HttpUrl]
    genres: List[Genre]
    release_date: Optional[str]
    spoken_languages: List[Language]
    vote_average: float
