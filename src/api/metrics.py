from flask import Blueprint, jsonify, request
from src.metrics.commands.metrics_save import MetricsSave

mb = Blueprint('metricas', __name__)

@mb.route('/health', methods = ['GET'])
def health():
    return jsonify({'msg': 'ok'}), 200

@mb.route('/metrics', methods = ['POST'])
def store():
    data = request.get_json()
    response = MetricsSave.execute(data)
    return jsonify(response), 200