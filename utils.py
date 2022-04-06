import json

__posts = []


def get_posts_all():  # возвращает список всех постов
    global __posts
    if type(__posts) not in [list]:
        raise TypeError('Должен быть список')
    with open('data/data.json', 'r', encoding='utf-8') as file:
        __posts = json.load(file)
    return __posts


def get_posts_by_user(user_name):  # возвращает посты определенного пользователя
    post_user = []
    if type(post_user) not in [list]:
        raise TypeError('Должен быть список')
    for post in __posts:
        if user_name in post['poster_name']:
            post_user.append(post)
    return post_user


def get_comments_by_post_id(post_id):  # возвращает комментарии определенного поста
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        comments = json.load(file)
    post_comments = []
    if type(post_comments) not in [list]:
        raise TypeError('Должен быть список')
    for comment in comments:
        if post_id == comment['post_id']:
            post_comments.append(comment)
    return post_comments


def search_for_posts(query):  # возвращает список постов по ключевому слову
    posts_query = []
    if type(posts_query) not in [list]:
        raise TypeError('Должен быть список')
    for post in __posts:
        if query.lower() in post['content'].lower():
            posts_query.append(post)
    return posts_query


def get_post_by_pk(pk):  # возвращает один пост по его идентификатору
    global post
    for post in __posts:
        if pk == post['pk']:
            return post
    if type(post) not in [dict]:
        raise TypeError('Должен быть dict')


