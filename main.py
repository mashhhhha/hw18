from config import Config
from flask import Flask
from flask_restx import Api
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


# creating the application
def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    register_extensions(application)

    return application


# register extensions
def register_extensions(app: Flask):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    app.run()
