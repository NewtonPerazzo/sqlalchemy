from infra.repository.movies import MoviesRepository
from infra.repository.actors import ActorsRepository
from infra.entities.movies import Movies
from infra.entities.actors import Actors

repo = MoviesRepository()
repoActors = ActorsRepository()

# repo.insert(Movies(title='sdhjkgsd', gender='fictional', year_movie=2022))
# repo.update('sdhjkgsd', Movies(title='Avengers Ultimato', gender='fictional', year_movie=2019))
# repo.delete('Avengers Ultimato')

data = repo.select()
data_actors = repoActors.select()
print(data)