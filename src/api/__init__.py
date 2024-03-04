from flask import Flask, jsonify
from .metrics import mb
from src.metrics.errors import ApiError

app = Flask(__name__)
app.register_blueprint(mb)

@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
        'msg': err.description
    }
    return jsonify(response), err.code

