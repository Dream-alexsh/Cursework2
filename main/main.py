from flask import render_template, request, Blueprint
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def index():
    data = get_posts_all()
    return render_template('index.html', data=data)


@main_blueprint.route('/posts/<int:post_id>')
def post(post_id):
    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    return render_template('post.html', post=post, comments=comments, comments_len=len(comments))


@main_blueprint.route('/search/')
def search():
    search_post = request.args.get('s')
    posts = search_for_posts(search_post)
    return render_template('search.html', search_post=search_post, posts=posts)


@main_blueprint.route('/users/<username>')
def user_page(username):
    user = get_posts_by_user(username)
    return render_template('user-feed.html', user=user)
