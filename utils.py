import json


def get_posts_all():

    """" Возвращает список всех постов """

    posts = []
    if type(posts) not in [list]:
        raise TypeError('Должен быть список')
    with open('data/data.json', 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def get_posts_by_user(user_name):

    """" Возвращает посты определенного пользователя """

    post_user = []
    if type(post_user) not in [list]:
        raise TypeError('Должен быть список')
    posts = get_posts_all()
    for post in posts:
        if user_name in post['poster_name']:
            post_user.append(post)
    return post_user


def get_comments_by_post_id(post_id):

    """" Возвращает комментарии определенного поста """

    with open('data/comments.json', 'r', encoding='utf-8') as file:
        comments = json.load(file)
    post_comments = []
    if type(post_comments) not in [list]:
        raise TypeError('Должен быть список')
    for comment in comments:
        if post_id == comment['post_id']:
            post_comments.append(comment)
    return post_comments


def search_for_posts(query):

    """" Возвращает список постов по ключевому слову """

    posts_query = []
    if type(posts_query) not in [list]:
        raise TypeError('Должен быть список')
    posts = get_posts_all()
    for post in posts:
        if query.lower() in post['content'].lower():
            posts_query.append(post)
    return posts_query


def get_post_by_pk(pk):

    """" Возвращает один пост по его идентификатору """

    posts = get_posts_all()
    for post in posts:
        if type(post) not in [dict]:
            raise TypeError('Должен быть dict')
        elif pk == post['pk']:
            return post



