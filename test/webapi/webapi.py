from flask import Flask, jsonify, abort, make_response
from matchtype import matchtyper

# create Flask instance
api = Flask(__name__)

li = ["Kodai",[165, 60, "male"]]

# GET implementation
@api.route('/get', methods=['GET'])
def get():
    result = matchtyper(li)
    return make_response(jsonify(result))

# error-handling
@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    api.run(host='localhost', port=8080)
