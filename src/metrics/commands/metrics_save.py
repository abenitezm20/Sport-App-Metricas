from src.metrics.providers.sqs_service_provider import SqsClient
from src.metrics.errors import SqsError

class MetricsSave():
    @staticmethod
    def execute(data):
        try:
            SqsClient.enqueue(data)
            return {'msg': 'Ok'}
        except Exception as e:
            raise SqsError(e, 400)