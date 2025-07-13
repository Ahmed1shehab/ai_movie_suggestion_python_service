# 🎬 AI Movie Suggestion Microservice

This **FastAPI** microservice provides AI-powered movie recommendations based on user prompts. It leverages **Hugging Face transformers** to extract movie names from natural language input and enriches the suggestions with detailed movie metadata fetched from **The Movie Database (TMDb) API**.

-----

## ✨ Features

  * **Intelligent Movie Extraction**: Uses a transformer language model to accurately identify movie titles from user prompts.
  * **Rich Movie Data**: Fetches comprehensive movie information including title, poster, overview, and more from TMDb.
  * **High Performance**: Built with FastAPI for a fast, asynchronous, and efficient API.
  * **Developer-Friendly**: Simple JSON request/response structure, easy to test, and extend.

-----

## 🛠️ Tech Stack

  * **FastAPI**: Modern, fast (high-performance) web framework for building APIs.
  * **Uvicorn**: Lightning-fast ASGI server to run your FastAPI application.
  * **Hugging Face Transformers**: Powerful library for natural language processing, enabling AI model integration.
  * **PyTorch**: The deep learning framework powering the transformer models.
  * **python-dotenv**: For securely managing environment variables.
  * **Requests**: Simple yet powerful HTTP library for interacting with the TMDb API.

-----

## 📂 Project Structure

```
├── main.py
├── models/
│   └── request_models.py
├── services/
│   ├── ai_model.py
│   └── tmdb_api.py
├── .env
├── requirements.txt
└── README.md
```

-----

## 🚀 Getting Started

Follow these steps to get your AI Movie Suggestion Microservice up and running quickly.

### 1\. Clone the Repository

```bash
git clone https://github.com/Ahmed1shehab/ai_movie_suggestion_python_service.git
cd ai_movie_suggestion_python_service
```

### 2\. Set Up Virtual Environment & Install Dependencies

It's highly recommended to use a virtual environment.

```bash
python -m venv venv
source venv/bin/activate # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

### 3\. Configure Environment Variables

Create a `.env` file in the root directory of your project and add your TMDb API key:

```
TMDB_API_KEY=your_tmdb_api_key_here
```

You can obtain a TMDb API key by registering on [TMDb's website](https://www.themoviedb.org/documentation/api).

### 4\. Run the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be accessible at `http://localhost:8000`.

### 5\. Explore the API

You can access the interactive API documentation (Swagger UI) at:

```
http://localhost:8000/docs
```

-----

## 📞 Contact

Feel free to reach out if you have any questions or feedback\!

  * **Ahmed Shehab**
  * **Email**: ahmed.shehab.7355@gmail.com
  * **GitHub**: [Ahmed1shehab](https://github.com/Ahmed1shehab)
  * **LinkedIn**: [Ahmed Shehab](https://www.linkedin.com/in/ahmed-shehab-6767652b3/)

-----

Last updated: July 13, 2025