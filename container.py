from dao.director_DAO import DirectorDAO
from dao.genre_DAO import GenreDAO
from dao.movie_DAO import MovieDAO
from service.director_service import DirectorService
from service.genre_service import GenreService
from service.movie_service import MovieService
from setup_db import db


# creating instances of each DAO
movie_dao = MovieDAO(db.session)
director_dao = DirectorDAO(db.session)
genre_dao = GenreDAO(db.session)

# creating instances of each service
movie_service = MovieService(movie_dao)
director_service = DirectorService(director_dao)
genre_service = GenreService(genre_dao)