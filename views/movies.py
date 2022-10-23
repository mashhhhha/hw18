from container import movie_service
from dao.models.Movie import MovieSchema
from flask import request
from flask_restx import Resource, Namespace

movie_ns = Namespace('/movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """
        returns all movies or movies with certain genre
        or movies with certain director
        """
        movies = movies_schema.dump(movie_service.get_all())
        query_director = request.args.get('director_id')
        query_genre = request.args.get('genre_id')
        query_year = request.args.get('year')

        if query_director:
            movies = movies_schema.dump(movie_service.get_by_director_id(query_director))
        if query_genre:
            movies = movies_schema.dump(movie_service.get_by_genre_id(query_genre))
        if query_year:
            movies = movies_schema.dump(movie_service.get_by_year(query_year))

        if len(movies) == 0:
            return 'there no suitable movies', 200

        return movies, 200

    def post(self):
        """
        add a new movie
        """

        req_json = request.json

        if not req_json:
            return '', 404

        movie_service.add_new(req_json)

        return '', 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        """
        returns certain movie
        """
        try:
            return movie_schema.dump(movie_service.get_one(mid)), 200
        except Exception as e:
            return f'{e}', 404

    def put(self, mid):
        """
                upgrades certain movie
        """
        req_json = request.json

        if not req_json:
            return '', 404

        movie_service.update_existing(req_json, mid)

        return '', 204

    def delete(self, mid):
        """
            delete certain movie
        """
        try:
            movie_service.delete(mid)

            return '', 204
        except Exception as e:
            return f'{e}', 404