from flask_restful import Resource, abort, reqparse
from flask import redirect

from generate_id import ID

_datastore = {"123": "https://news.ycombinator.com"}

class TinyList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('url')

    def get(self):
        return _datastore, 200

    def post(self):
        args = TinyList.parser.parse_args()
        url = args["url"]
        if url is None:
            abort(422, message = "unable to process")

        key = ID.generate(url)


        while key in _datastore:
            if _datastore[key] == url:
                break
            key = ID.generate(url, len(key)+1)

        _datastore[key] = args["url"]

        return { key: _datastore[key]}, 201


class Tiny(Resource):


    def get(self, url):

        if url in _datastore:
            return redirect(_datastore[url])
            # return  _datastore[url], 200

        abort(404, message = "URL Not Found")

