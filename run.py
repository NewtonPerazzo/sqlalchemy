from infra.repository.movies import MoviesRepository
from infra.repository.actors import ActorsRepository
from infra.entities.movies import Movies
from infra.entities.actors import Actors
from infra.configs.connection import DBConncetionHandler

repo = MoviesRepository(DBConncetionHandler)
repoActors = ActorsRepository()

# repo.insert(Movies(title='Random', gender='fictional', year_movie=2022))
# repo.update('Random', Movies(title='Avengers Ultimate', gender='fictional', year_movie=2019))
# repo.delete('Avengers Ultimate')

data = repo.select_horror_movies()
data_actors = repoActors.select()
print(data)