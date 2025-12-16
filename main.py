from fastapi import FastAPI
from sqlalchemy.orm import Session
from sqlalchemy import select, func, desc
from models import engine, Movie, Rating

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Witaj w API Filmowym! Przejdź pod /docs aby testować."}


@app.get("/stats")
def read_stats():
    with Session(engine) as session:
        movies = session.query(func.count(Movie.movieId)).scalar()
        ratings = session.query(func.count(Rating.id)).scalar()

    return {"liczba_filmow": movies, "liczba_ocen": ratings}


@app.get("/movies/")
def search_movies(title: str = ""):
    if not title:
        return {"error": "Podaj parametr title, np. /movies/?title=Toy"}

    with Session(engine) as session:
        stmt = select(Movie).where(Movie.title.ilike(f"%{title}%")).limit(10)
        res = session.execute(stmt).scalars().all()

        data = []
        for m in res:
            data.append({
                "id": m.movieId,
                "title": m.title,
                "genres": m.genres
            })
        return data


@app.get("/movies/top")
def get_top_movies():
    with Session(engine) as session:
        stmt = select(Movie.title, func.avg(Rating.rating).label("avg_rate")) \
            .join(Rating, Movie.movieId == Rating.movieId) \
            .group_by(Movie.title) \
            .having(func.count(Rating.rating) > 50) \
            .order_by(desc("avg_rate")) \
            .limit(10)

        res = session.execute(stmt).all()

        top = []
        for r in res:
            top.append({
                "title": r.title,
                "rating": round(r.avg_rate, 2)
            })
        return top