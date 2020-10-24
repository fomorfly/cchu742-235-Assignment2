import pytest

from cs235flix.adapters.memory_repository import MemoryRepository
from cs235flix.domain.model import *


def test_can_add_movie():
    movie = Movie("Ninja Turtle", 2001)
    repo = MemoryRepository()
    repo.add_movie(movie)
    assert repo.get_movies()[0] == movie

def test_can_add_user():
    user = User("fomorfly", "Abcd12345")
    repo = MemoryRepository()
    repo.add_user(user)
    assert repo.get_user("fomorfly") == user


test_can_add_movie()