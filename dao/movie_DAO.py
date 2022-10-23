from dao.models.Movie import Movie, MovieSchema

movie_schema = MovieSchema()


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        movies = self.session.query(Movie).all()

        return movies

    def get_one(self, mid):
        movie = self.session.query(Movie).get(mid)

        return movie

    def get_by_director_id(self, did):
        movies = self.session.query(Movie).filter(Movie.director_id == did)

        return movies

    def get_by_genre_id(self, gid):
        movies = self.session.query(Movie).filter(Movie.genre_id == gid)

        return movies

    def get_by_year(self, year):
        movies = self.session.query(Movie).filter(Movie.year == year)

        return movies

    def add_new(self, data):

        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

    def update_existing(self, data, mid):
        self.session.query(Movie).filter(Movie.id == mid).update(data)
        self.session.commit()

    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()