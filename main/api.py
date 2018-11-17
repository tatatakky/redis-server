from flask import Flask, jsonify, abort, make_response
from matchtype import matchtyper
from db import db_handle
import sys

api = Flask(__name__)

@api.route('/get/<key_name>', methods=['GET'])
def get(key_name):
    li = db_handle(key_name)
    if li[1] is None:
        abort(404)
    else:
        result = matchtyper(li)
        return make_response(jsonify(result))

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    api.debug = True
    api.run(host='localhost', port=8080)
