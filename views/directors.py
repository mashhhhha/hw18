from container import director_service
from dao.models.Director import DirectorSchema
from flask_restx import Namespace, Resource

director_ns = Namespace('/directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        """
        return all directors
        """
        try:
            return directors_schema.dump(director_service.get_all())

        except Exception as e:
            return f'{e}'

@director_ns.route('/<int:did>')
class DirectorView(Resource):

    def get(self, did):
        """
        return certain director
        """
        try:
            return director_schema.dump(director_service.get_one(did))

        except Exception as e:
            return f'{e}'