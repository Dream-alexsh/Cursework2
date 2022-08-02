from flask import jsonify, Blueprint
from utils import get_posts_all, get_post_by_pk

api_blueprint = Blueprint('api_blueprint', __name__, template_folder='templates')


@api_blueprint.route('/api/posts')
def get_json():
    data = get_posts_all()
    return jsonify(data)


@api_blueprint.route('/api/posts/<int:post_id>')
def get_json_post(post_id):
    data = get_post_by_pk(post_id)
    return jsonify(data)
