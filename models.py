from sqlalchemy import create_engine, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


db_url = "sqlite:///movies_data.db"
engine = create_engine(db_url)


class Base(DeclarativeBase):
    pass


class Movie(Base):
    __tablename__ = 'movies'
    movieId: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)
    genres: Mapped[str] = mapped_column(String)


class Link(Base):
    __tablename__ = 'links'
    movieId: Mapped[int] = mapped_column(primary_key=True)
    imdbId: Mapped[str] = mapped_column(String)
    tmdbId: Mapped[str] = mapped_column(String)


class Rating(Base):
    __tablename__ = 'ratings'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    userId: Mapped[int] = mapped_column(Integer)
    movieId: Mapped[int] = mapped_column(Integer)
    rating: Mapped[float] = mapped_column(Float)
    timestamp: Mapped[int] = mapped_column(Integer)


class Tag(Base):
    __tablename__ = 'tags'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    userId: Mapped[int] = mapped_column(Integer)
    movieId: Mapped[int] = mapped_column(Integer)
    tag: Mapped[str] = mapped_column(String)
    timestamp: Mapped[int] = mapped_column(Integer)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
