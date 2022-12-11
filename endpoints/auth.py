from flask import Blueprint, request, jsonify
from flask_jwt_extended import unset_jwt_cookies, jwt_required, create_access_token, create_refresh_token, \
    set_access_cookies, set_refresh_cookies, get_jwt_identity

from models.user import *

bp = Blueprint('auth', __name__, url_prefix="/auth")


@bp.route('/register', methods=('POST',))
def register():
    username, password = creds_from_json_data()
    user = get_user_by(username, 'username')
    if user is None:
        user = add_user(username, password)
        access_token = create_access_token(identity=user['id'])
        refresh_token = create_refresh_token(identity=user['id'])
        response = jsonify()
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return response, 201
    return jsonify(message="Nutzer konnte nicht angelegt werden."), 400


@bp.route('/login', methods=('POST',))
def login():
    username, password = creds_from_json_data()
    user = authenticate(username, password)
    if user:
        access_token = create_access_token(identity=user['id'])
        refresh_token = create_refresh_token(identity=user['id'])
        response = jsonify()
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return response, 201
    return jsonify(message="Unauthorized"), 401


@bp.route('/logout', methods=('POST',))
@jwt_required
def logout():
    response = jsonify()
    unset_jwt_cookies(response)
    return response, 200


@bp.route('/refresh', methods=('POST',))
@jwt_required(refresh=True)
def refresh():
    user_id = get_jwt_identity()
    user = get_user_by(user_id, 'id')
    access_token = create_access_token(identity=user['id'])
    response = jsonify()
    set_access_cookies(response, access_token)
    return response, 201


def creds_from_json_data():
    data = request.get_json()
    password = data['password']
    username = data['username']
    return username, password
