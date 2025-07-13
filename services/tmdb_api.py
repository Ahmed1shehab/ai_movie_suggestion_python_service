import requests
import os
import logging
from dotenv import load_dotenv

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

if not TMDB_API_KEY:
    raise EnvironmentError("❌ TMDB_API_KEY is missing in .env")

def get_movie_details(movie_name: str):
    search_url = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": TMDB_API_KEY, "query": movie_name}
    try:
        res = requests.get(search_url, params=params).json()
        if not res.get('results'):
            return None

        movie = res['results'][0]
        movie_id = movie['id']
        imdb_id = get_imdb_id(movie_id)
        trailer = get_trailer(movie_id)
        details = get_full_movie_details(movie_id)

        return {
            "title": movie['title'],
            "overview": movie.get('overview', 'No overview available.'),
            "poster_url": f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie.get('poster_path') else "",
            "imdb_link": f"https://www.imdb.com/title/{imdb_id}" if imdb_id else "",
            "trailer": trailer,
            "genres": details.get("genres", []),
            "release_date": details.get("release_date", ""),
            "spoken_languages": details.get("spoken_languages", []),
            "vote_average": details.get("vote_average", 0.0),
        }
    except Exception as e:
        logging.error("Failed to fetch movie details: %s", e)
        return None

def get_full_movie_details(movie_id: int):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    try:
        res = requests.get(url, params={"api_key": TMDB_API_KEY}).json()
        return {
            "genres": res.get("genres", []),
            "release_date": res.get("release_date", ""),
            "spoken_languages": res.get("spoken_languages", []),
            "vote_average": res.get("vote_average", 0.0)
        }
    except Exception as e:
        logging.warning("Failed to get full movie details: %s", e)
        return {}

def get_imdb_id(movie_id: int) -> str:
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/external_ids"
    try:
        res = requests.get(url, params={"api_key": TMDB_API_KEY}).json()
        return res.get("imdb_id")
    except Exception as e:
        logging.warning("Failed to get IMDB ID: %s", e)
        return None

def get_trailer(movie_id: int) -> str:
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos"
    try:
        res = requests.get(url, params={"api_key": TMDB_API_KEY}).json()
        for video in res.get("results", []):
            if video.get("type") == "Trailer" and video.get("site") == "YouTube":
                return f"https://www.youtube.com/watch?v={video['key']}"
    except Exception as e:
        logging.warning("Failed to fetch trailer: %s", e)
    return ""
