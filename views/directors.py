from flask_restx import Resource, Namespace
from dao.model.directors import DirectorSchema, director_schema, directors_schema
from implemented import director_service

director_ns = Namespace('directors')

@director_ns.route('/')
class DirectorsView(Resource):
    # schema = DirectorSchema(many=True)
    #
    # def get(self):
    #     return self.schema.dump(director_service.get()), 200
    def get(self):
        all_dir = director_service.get_all()
        return directors_schema.dump(all_dir)


@director_ns.route('/<int:did>')
class DirectorViews(Resource):
    # schema = DirectorSchema()
    #
    # def get(self, did):
    #     return self.schema.dump(director_service.get(did)), 200
    def get(self, did: int):
        dir = director_service.get_one(did)
        return director_schema.dump(dir), 200
