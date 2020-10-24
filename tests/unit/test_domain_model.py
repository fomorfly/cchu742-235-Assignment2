from cs235flix.domain.model import *


def test_movie_construction():
    movie = Movie("Moana", 2016)
    assert movie.title == "Moana"
    assert movie.release == 2016


def test_movie_set_director():
    movie = Movie("Moana", 2016)
    director = Director("John")
    movie.director = director
    assert movie.director == director


def test_movie_set_genre():
    movie = Movie("Moana", 2016)
    gen_horror = Genre("horror")
    gen_action = Genre("action")
    movie.add_genre(gen_action)
    movie.add_genre(gen_horror)
    assert movie.genres == [gen_action, gen_horror]


def test_movie_set_actors():
    movie = Movie("Moana", 2016)
    actor_alexandra = Actor("alexandra")
    actor_wick = Actor("wick")
    movie.add_actor(actor_alexandra)
    movie.add_actor(actor_wick)
    assert movie.actors == [actor_alexandra, actor_wick]


def add_review_to_user():
    user = User("fomorfly", "Abcd12345")
    movie = Movie("Moana", 2016)
    review = Review(movie, "hello review", "fomorfly")
    user.add_review(review)
    assert user.reviews[0] == review


def add_watchlist_to_user():
    user = User("fomorfly", "Abcd12345")
    movie = Movie("Moana", 2016)
    user.add_watchlist(movie)
    assert user.watchlist[0] == movie


def remove_watchlist_from_user():
    user = User("fomorfly", "Abcd12345")
    movie = Movie("Moana", 2016)
    user.add_watchlist(movie)
    assert user.watchlist[0] == movie
    user.del_watchlist(movie)
    assert len(user.watchlist) == 0


# test_movie_set_actors()
# test_movie_set_genre()
# test_movie_construction()
# test_movie_set_director()
