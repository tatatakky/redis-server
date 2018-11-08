from flask import Flask, jsonify, abort, make_response
from matchtype import matchtyper
from db import db_handle
import sys

arg = sys.argv[1]

# create Flask instance
api = Flask(__name__)

# GET implementation
@api.route('/get/' + arg, methods=['GET'])
def get():
    li = db_handle(arg)
    result = matchtyper(li)
    return make_response(jsonify(result))

# error-handling
@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    api.run(host='localhost', port=8080)
