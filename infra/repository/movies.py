from infra.configs.connection import DBConncetionHandler
from infra.entities.movies import Movies
from sqlalchemy.orm.exc import NoResultFound

class MoviesRepository():
    def select(self):
        with DBConncetionHandler() as db:
            data = db.session.query(Movies).all()
            return data
    
    def select_horror_movies(self):
        with DBConncetionHandler() as db:
            try:
                data = db.session.query(Movies).filter(Movies.gender == 'sasa').one()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception


    def insert(self, movie: Movies):
        with DBConncetionHandler() as db:
            try:
                db.session.add(movie)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, title: str):
        with DBConncetionHandler() as db:
            db.session.query(Movies)\
                .filter(Movies.title == title)\
                .delete()
            db.session.commit()
    
    def update(self, title, movie_updated: Movies):
        with DBConncetionHandler() as db:
            movie_dict = movie_updated.__dict__.copy()
            movie_dict.pop("_sa_instance_state", None) # removing unusable things from dict copy
        
            db.session.query(Movies).filter(Movies.title == title).update(movie_dict)
            db.session.commit()