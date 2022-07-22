from flask_restx import Resource, Namespace
from dao.model.genres import GenreSchema, genre_schema, genres_schema
from implemented import genre_service

genre_ns = Namespace('genres')

@genre_ns.route('/')
class GenresView(Resource):
    # schema = GenreSchema(many=True)
    #
    # def get(self):
    #     return self.schema.dump(genre_service.get()), 200
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres)

@genre_ns.route('/<int:did>')
class GenreViews(Resource):
    # schema = GenreSchema()
    #
    # def get(self, did):
    #     return self.schema.dump(genre_service.get(did)), 200
    def get(self, genre_id: int):
        genre = genre_service.get_one(genre_id)
        return genre_schema.dump(genre), 200