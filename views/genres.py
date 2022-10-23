from container import genre_service
from dao.models.Genre import GenreSchema
from flask_restx import Namespace, Resource

genre_ns = Namespace('/genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):

    def get(self):
        """
        returns all genres
        """
        try:
            return genres_schema.dump(genre_service.get_all())

        except Exception as e:
            return f'{e}'

@genre_ns.route('/<int:gid>')
class GenreView(Resource):

    def get(self, gid):
        """
        returns certain genre
        """
        try:
            return genre_schema.dump(genre_service.get_one(gid))

        except Exception as e:
            return f'{e}'