import pytest

from cs235flix.adapters.memory_repository import populate, MemoryRepository
import cs235flix.adapters.repository as repo
import cs235flix.home.services as home_services
import cs235flix.advsearch.services as advsearch_services
import cs235flix.authentication.services as auth_services


def test_get_page():
    repo.repo_instance = MemoryRepository()
    populate("cs235flix/adapters/data/Data1000Movies.csv", repo.repo_instance)

    movie_list = repo.repo_instance.get_movies()
    real_page1 = movie_list[0: 20]
    func_page1 = home_services.get_page(0)

    movie_list = repo.repo_instance.get_movies()
    real_page5 = movie_list[100: 120]
    func_page5 = home_services.get_page(5)

    assert real_page1 == func_page1
    assert real_page5 == func_page5


def test_get_movie_with_movieID():
    repo.repo_instance = MemoryRepository()
    populate("cs235flix/adapters/data/Data1000Movies.csv", repo.repo_instance)

    movie = home_services.get_movie(14)
    assert movie.title == "Colossal"


def test_authentication_with_valid_credentials():
    username = 'fomorfly'
    password = 'Abcd12345'

    auth_services.add_user(username, password)

    try:
        auth_services.authenticate_user(username, password)
    except Exception:
        assert False


def test_authentication_with_invalid_credentials():
    username = 'fomorfly'
    password = 'Abcd12345'

    # Use try clause in case cache is not wiped
    try:
        auth_services.add_user(username, password)
    except:
        a = 1  # do nothing

    with pytest.raises(auth_services.AuthenticationException):
        auth_services.authenticate_user(username, '0987654321')


def test_get_filtered_movies():
    repo.repo_instance = MemoryRepository()
    populate("cs235flix/adapters/data/Data1000Movies.csv", repo.repo_instance)

    filtered_movies = advsearch_services.get_filtered_movies(["thriller", "drama"], ["florian gallenberger"],
                                                             ["emma watson"])
    assert filtered_movies[0].title == "Colonia"
