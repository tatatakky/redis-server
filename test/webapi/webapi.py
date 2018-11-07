from flask import Flask, jsonify, abort, make_response
from matchtype import matchtyper

# Flaskクラスのインスタンスを作成
api = Flask(__name__)

li = ["Kodai",[165, 60, "male"]]

# GETの実装
@api.route('/get', methods=['GET'])
def get():
    #result = { "greeting": 'hello flask' }
    result = matchtyper(li)
    return make_response(jsonify(result))

# エラーハンドリング
@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    api.run(host='localhost', port=8080)
