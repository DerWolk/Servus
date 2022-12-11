import logging

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
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    return response_object


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=DEBUG)
