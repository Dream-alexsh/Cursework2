import pytest
from utils import get_posts_all, get_posts_by_user, get_comments_by_post_id, search_for_posts, get_post_by_pk


def test_get_posts_all():
    posts = get_posts_all()
    assert type(posts) == list, 'Не список'
    assert len(posts) == 8, 'неправильное число'


def test_get_posts_all_type_error():
    with pytest.raises(TypeError):
        get_posts_all(1)


def test_get_posts_by_user():
    user_post = get_posts_by_user('larry')
    assert type(user_post) == list, 'не список'
    assert len(user_post) == 2, 'неправильное число'


def test_get_posts_by_user_type_error():
    with pytest.raises(TypeError):
        get_posts_by_user(2)


def test_get_comments_by_post_id():
    comment_user = get_comments_by_post_id(1)
    assert type(comment_user) == list, 'не список'
    assert len(comment_user) == 4, 'неправильное число'


def test_get_comments_by_post_id_type_error():
    with pytest.raises(TypeError):
        get_comments_by_post_id()


def test_search_for_posts():
    search_post = search_for_posts('лампочка')
    assert type(search_post) == list, 'не список'
    assert len(search_post) == 1, 'неправильное число'


def test_search_for_posts_type_error():
    with pytest.raises(TypeError):
        search_for_posts()


def test_get_post_by_pk():
    post_pk = get_post_by_pk(4)
    assert type(post_pk) == dict, 'не словарь'
    assert len(post_pk) == 7, 'неправильное число'


def test_test_get_post_by_pk():
    with pytest.raises(TypeError):
        test_get_post_by_pk(4)

