import logging

from flask import Flask
from flask_cors import CORS

from endpoints import health, auth, books

DEBUG = True
logging.getLogger('flask-cors').level = logging.DEBUG

if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(__name__)

    cors = CORS(app, resources={r'/*': {'origins': '*'}})

    app.register_blueprint(health.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(books.bp)
    app.run(host='0.0.0.0', port=9090, debug=DEBUG)
