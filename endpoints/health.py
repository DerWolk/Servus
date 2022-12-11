from flask import Blueprint, jsonify

bp = Blueprint('health', __name__, url_prefix="/")


@bp.route('/ping', methods=('GET',))
def ping_pong():
    return jsonify('pong!')
