import csv
import os
from fastapi import FastAPI

app = FastAPI()

class Movie:
    def __init__(self, movie_id, title, genres):
        self.id = movie_id
        self.title = title
        self.genres = genres

class Link:
    def __init__(self, movie_id, imdb_id, tmdb_id):
        self.movie_id = movie_id
        self.imdb_id = imdb_id
        self.tmdb_id = tmdb_id

class Rating:
    def __init__(self, user_id, movie_id, rating, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp

class Tag:
    def __init__(self, user_id, movie_id, tag, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.tag = tag
        self.timestamp = timestamp

@app.get("/movies")
def get_movies():
    movies_list = []
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "database", "movies.csv")

    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}

    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            new_movie = Movie(
                movie_id=row['movieId'],
                title=row['title'],
                genres=row['genres']
            )
            movies_list.append(new_movie.__dict__)

    return movies_list

@app.get("/links")
def get_links():
    links_list = []
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "database", "links.csv")

    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}

    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            new_link = Link(
                movie_id=row['movieId'],
                imdb_id=row['imdbId'],
                tmdb_id=row['tmdbId']
            )
            links_list.append(new_link.__dict__)

    return links_list

@app.get("/ratings")
def get_ratings(limit: int = 100):
    ratings_list = []
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "database", "ratings.csv")

    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}

    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)