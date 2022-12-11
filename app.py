import logging
import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS

DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
cors = CORS(app, resources={r'/*': {'origins': '*'}})

logging.getLogger('flask-cors').level = logging.DEBUG

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'TEST',
        'author': 'Jan Lucca',
        'read': True
    }
]


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/books', methods=['GET', 'POST'])
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
        response_object['message'] = 'Book added!'
    return response_object


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=DEBUG)
