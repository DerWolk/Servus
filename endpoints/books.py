import uuid

from flask import Blueprint, request, jsonify

bp = Blueprint('books', __name__, url_prefix="/books")

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'TEST',
        'author': 'Jan Lucca',
        'read': True
    }
]


@bp.route('/', methods=('GET', 'POST',))
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'GET':
        response_object['books'] = BOOKS
    elif request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Buch hinzugefügt.'
    return response_object


@bp.route('/<book_id>', methods=('PUT', 'DELETE',))
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Buch aktualisiert.'
    elif request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Buch entfernt.'
    return jsonify(response_object)


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False
