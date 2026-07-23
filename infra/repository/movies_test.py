from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from infra.entities.movies import Movies
from infra.entities.actors import Actors
from .movies import MoviesRepository


class ConnectionHandlerMock:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(Movies)],
                    [Movies(title="Loving", gender="romance", year_movie=1999)]
                ),
                (
                    [
                        mock.call.query(Movies),
                        mock.call.filter(Movies.gender=="horror")
                    ],
                    [Movies(title="It", gender="horror", year_movie=2021)],
                )
            ]
        )
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.session.close()

def test_select_horror_movies():
    movie_repository = MoviesRepository(ConnectionHandlerMock)
    response = movie_repository.select_horror_movies()
    print()
    print(response)
    assert isinstance(response, Movies)
    assert response.title == 'It'

def test_select():
    movie_repository = MoviesRepository(ConnectionHandlerMock)
    response = movie_repository.select()
    print()
    print(response)
    assert isinstance(response, list)
    assert isinstance(response[0], Movies)

def test_insert():
    movie_repository = MoviesRepository(ConnectionHandlerMock)
    response = movie_repository.insert(Movies(title="Run", gender="suspense", year_movie=2029))
    print()
    print(response)