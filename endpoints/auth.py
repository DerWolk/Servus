from flask import Blueprint, request, jsonify
from flask_jwt_extended import unset_jwt_cookies, jwt_required

bp = Blueprint('auth', __name__, url_prefix="/auth")


@bp.route('/register', methods=('POST',))
def register():
    password, username = creds_from_json_data()
    return jsonify(message="Nutzer konnte nicht angelegt werden."), 400


@bp.route('/login', methods=('POST',))
def login():
    password, username = creds_from_json_data()
    return jsonify(message="Unauthorized"), 401


@bp.route('/logout', methods=('POST',))
@jwt_required
def logout():
    response = jsonify()
    unset_jwt_cookies(response)
    return response, 200


def creds_from_json_data():
    data = request.get_json()
    password = data['password']
    username = data['username']
    return password, username
