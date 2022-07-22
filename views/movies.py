from flask import request, make_response
from flask_restx import Resource, Namespace
from dao.model.movies import MovieSchema, movie_schema, movies_schema
from implemented import movie_service

movie_ns = Namespace('movies')

# @movie_ns.route('/')
# class MovieView(Resource):
#     schema = MovieSchema(many=True)
#
#     def get(self):
#         movies = self.schema.dump(movie_service.get_movies(**request.args))
#         return movies, 200
#
#     def post(self):
#         new_movie = movie_service.create_movie(request.json)
#         resp = make_response("", 201)
#         resp.headers['location'] = f"{movie_ns.path}/{new_movie.id}"
#         return resp
#
#
# @movie_ns.route('/<int:movie_id>')
# class MovieViews(Resource):
#     schema = MovieSchema()
#
#     def get(self, movie_id: int):
#         return self.schema.dump(movie_service.get_movies(movie_id)), 200
#
#     def patch(self, movie_id: int):
#         return self.schema.dump(movie_service.update_movie_partial(movie_id, request.json)), 200
#
#     def put(self, movie_id):
#         return self.schema.dump(movie_service.update_movie_full(movie_id, request.json)), 200
#
#     def delete(self, movie_id):
#         movie_service.delete(movie_id)
#         return "", 204

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")

        filters = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
        }

        all_movies = movie_service.get_all(filters)
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        new_movie = movie_service.create(req_json)
        return f'Новый фильм c id {new_movie.id} успешно добавлен в БД', 201, {
            'location': f'{movie_ns.path}/{new_movie.id}'}


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id: int):
        movie = movie_service.get_one(movie_id)
        return movie_schema.dump(movie), 200

    def put(self, movie_id: int):
        req_json = request.json
        req_json['id'] = movie_id
        movie_service.update(req_json)
        return f'Фильм с id {movie_id} обновлен', 204

    def patch(self, movie_id: int):
        req_json = request.json
        req_json['id'] = movie_id
        movie_service.update_partial(req_json)
        return f'Фильм с id {movie_id} обновлен', 204

    def delete(self, movie_id: int):
        movie_service.delete(movie_id)
        return f'Фильм с id {movie_id} удален', 204