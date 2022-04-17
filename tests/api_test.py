import pytest
from app import app
from utils import get_posts_all


def test_app_all():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200
    assert response.json == get_posts_all()
    assert type(response.json) == list, 'Не список'

    need_keys = ['content', 'pic', 'poster_avatar', 'poster_name', 'views_count', 'likes_count', 'pk']
    for i in response.json:
        for key in need_keys:
            assert bool(key in i.keys()) == True


def test_app_post():
    params = {"poster_name": "larry"}
    response = app.test_client().get('/api/posts/8', query_string=params)
    assert response.status_code == 200
    assert type(response.json) == dict, 'не словарь'
    need_keys = ['content', 'pic', 'poster_avatar', 'poster_name', 'views_count', 'likes_count', 'pk']
    for key in need_keys:
        assert key in response.json
