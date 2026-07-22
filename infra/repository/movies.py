from infra.configs.connection import DBConncetionHandler
from infra.entities.movies import Movies

class MoviesRepository():
    def select(self):
        with DBConncetionHandler() as db:
            data = db.session.query(Movies).all()
            return data
        
    def insert(self, movie: Movies):
        with DBConncetionHandler() as db:
            db.session.add(movie)
            db.session.commit()

    def delete(self, title: str):
        with DBConncetionHandler() as db:
            db.session.query(Movies).filter(Movies.title == title).delete()
            db.session.commit()
    
    def update(self, title, movie_updated: Movies):
        with DBConncetionHandler() as db:
            movie_dict = movie_updated.__dict__.copy()
            movie_dict.pop("_sa_instance_state", None) # removing unusable things from dict copy
        
            db.session.query(Movies).filter(Movies.title == title).update(movie_dict)
            db.session.commit()