from infra.repository.movies import MoviesRepository
from infra.entities.movies import Movies

repo = MoviesRepository()

# repo.insert(Movies(title='sdhjkgsd', gender='fictional', year_movie=2022))
# repo.update('sdhjkgsd', Movies(title='Avengers Ultimato', gender='fictional', year_movie=2019))
repo.delete('Avengers Ultimato')

data = repo.select()
print(data)