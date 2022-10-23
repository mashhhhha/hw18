from dao.movie_DAO import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_by_director_id(self, did):
        return self.dao.get_by_director_id(did)

    def get_by_genre_id(self, gid):
        return self.dao.get_by_genre_id(gid)

    def get_by_year(self, year):
        return self.dao.get_by_year(year)

    def add_new(self, data):
        self.dao.add_new(data)

    def update_existing(self, data, mid):
        return self.dao.update_existing(data, mid)

    def delete(self, mid):
        return self.dao.delete(mid)