import csv
import os
from sqlalchemy.orm import Session
from models import engine, Base, Movie, Link, Rating, Tag


def get_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def load_movies(session):
    with open(get_path('movies.csv'), encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            session.add(Movie(
                movieId=int(row['movieId']),
                title=row['title'],
                genres=row['genres']
            ))


def load_links(session):
    with open(get_path('links.csv'), encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            session.add(Link(
                movieId=int(row['movieId']),
                imdbId=row['imdbId'],
                tmdbId=row['tmdbId']
            ))


def load_tags(session):
    with open(get_path('tags.csv'), encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            session.add(Tag(
                userId=int(row['userId']),
                movieId=int(row['movieId']),
                tag=row['tag'],
                timestamp=int(row['timestamp'])
            ))


def load_ratings(session):
    with open(get_path('ratings.csv'), encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            session.add(Rating(
                userId=int(row['userId']),
                movieId=int(row['movieId']),
                rating=float(row['rating']),
                timestamp=int(row['timestamp'])
            ))
            if i % 10000 == 0:
                session.commit()


if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        print("Trwa ładowanie danych...")

        load_movies(session)
        load_links(session)
        load_tags(session)
        load_ratings(session)

        session.commit()
        print("Gotowe. Baza utworzona.")
