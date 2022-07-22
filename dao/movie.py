from dao.model.movies import Movie
from dao.model.genres import Genre
from dao.model.directors import Director


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director_id(self, val):
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self, val):
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year(self, val):
        return self.session.query(Movie).filter(Movie.year == val).all()

    def get_one(self, movie_id):
        return self.session.query(Movie).get(movie_id)

    def create(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, movie_id):
        self.session.delete(self.get_one(movie_id))
        self.session.commit()