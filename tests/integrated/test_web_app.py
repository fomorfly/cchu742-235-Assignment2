import pytest

from flask import session


def test_register(client):
    # Check that GET response with code 200 ok
    response_code = client.get('/authentication/register').status_code
    assert response_code == 200

    response = client.post(
        '/authentication/register', data={'username': 'fomorfly', 'password': 'Abcd1234'}
    )
    assert response.headers['Location'] == 'http://localhost/authentication/login'


def test_login(client, auth):
    # check that GET response with code 200 ok
    status_code = client.get('/authentication/login').status_code
    assert status_code == 200

    response = auth.login()
    assert response.headers['Location'] == 'http://localhost/'


def test_logout(auth):
    auth.login()

    auth.logout()
    assert 'user_id' not in session


def test_login_required(client):
    response = client.post('/comment')
    assert response.headers['Location'] == 'http://localhost/authentication/login'


def test_review(client, auth):
    auth.login()

    response = client.get('review?movie_id=0')

    response = client.post('/review', data={'review': 'review testing, hello', 'article_id': 0})
    assert response.headers['Location'] == 'http://localhost:5000/view_movie?movie_id=0'


def test_advsearch(client):
    response = client.get("advsearch/advsearch")

    response = client.post('/genre', data={'genre': "romance"})
    assert response.headers['Location'] == 'http://localhost:5000/advsearch/results'
