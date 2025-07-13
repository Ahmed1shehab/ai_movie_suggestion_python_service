from fastapi import FastAPI
from models.request_models import MovieRequest, MovieResponse
from services.ai_model import get_movie_name
from services.tmdb_api import get_movie_details
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.post("/suggest_movie", response_model=MovieResponse)
def suggest_movie(req: MovieRequest):
    movie_name = get_movie_name(req.prompt)
    if not movie_name:
        return {"error": "Could not extract movie name."}

    movie_data = get_movie_details(movie_name)
    if not movie_data:
        return {"error": f"No data found for '{movie_name}'"}

    return movie_data
