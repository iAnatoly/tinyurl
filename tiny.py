from flask_restful import Resource, abort, reqparse
from flask import redirect, request

from generate_id import ID
from lru import LRU

_datastore = LRU(2, {'123': 'https://news.ycombinator.com'})

class TinyList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('url')

    def auth_required(decorated):
        'mock auth decorator'
        def wrapper(self):
            auth_header = request.headers.get('Authorization')
            if not auth_header: 
                abort(401, message = 'auth required')
            (scheme,auth_token) = auth_header.split(' ')
            if scheme !='Bearer' or auth_token != 'bear': 
                abort(401, message = 'auth required')
           
            return decorated(self)
        return wrapper

    @auth_required
    def get(self):
        return _datastore, 200

    def post(self):
        args = TinyList.parser.parse_args()
        url = args['url']
        if url is None:
            abort(422, message = 'unable to process')

        key = ID.generate(url)


        while key in _datastore:
            if _datastore[key] == url:
                break
            key = ID.generate(url, len(key)+1)

        _datastore[key] = args['url']

        return { key: _datastore[key]}, 201


class Tiny(Resource):


    def get(self, url):

        if url in _datastore:
            return redirect(_datastore[url])
            # return  _datastore[url], 200

        abort(404, message = 'URL Not Found')

