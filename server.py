from flask import Flask
from flask_restful import Api, reqparse
from tiny import Tiny, TinyList
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
api = Api(app)
api.add_resource(Tiny, '/api/v1/url/<string:url>')
api.add_resource(TinyList, '/api/v1/url/')



if __name__ == '__main__':
    app.run()
