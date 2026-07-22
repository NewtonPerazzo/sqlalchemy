from infra.configs.connection import DBConncetionHandler
from infra.entities.actors import Actors
from infra.entities.movies import Movies

class ActorsRepository():
    def select(self):
        with DBConncetionHandler() as db:
            data = db.session\
                .query(Actors, Movies)\
                .join(Movies, Actors.movie_title == Movies.title)\
                .with_entities(
                    Actors.name,
                    Movies.gender,
                    Movies.title
                ).all()
            return data
        
    # def insert(self, actor: Actors):
    #     with DBConncetionHandler() as db:
    #         db.session.add(actor)
    #         db.session.commit()

    # def delete(self, title: str):
    #     with DBConncetionHandler() as db:
    #         db.session.query(Actors).filter(Actors.title == title).delete()
    #         db.session.commit()
    
    # def update(self, title, actor_updated: Actors):
    #     with DBConncetionHandler() as db:
    #         actor_dict = actor_updated.__dict__.copy()
    #         actor_dict.pop("_sa_instance_state", None) # removing unusable things from dict copy
        
    #         db.session.query(Actors).filter(Actors.title == title).update(actor_dict)
    #         db.session.commit()