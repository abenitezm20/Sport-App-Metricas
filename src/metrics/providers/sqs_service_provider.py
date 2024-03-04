import boto3
import os
import json
import hashlib
import time

class SqsClient():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SqsClient, cls).__new__(cls)
            session = boto3.Session(
                aws_access_key_id= os.getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                region_name=os.getenv('AWS_REGION_NAME')
            )

            cls._instance = session.client('sqs')
        return cls._instance

    @staticmethod
    def enqueue(data):
        client = SqsClient()
        data['t1'] = time.perf_counter()
        data['device_id'] = '387529002849' #saldria del token de autenticación 
        encodedData = json.dumps(data)
        response = client.send_message(
            QueueUrl=os.getenv('METRICS_QUEUE'),
            MessageBody=encodedData,
            MessageGroupId='proyecto-final',
            MessageDeduplicationId=hashlib.md5(encodedData.encode('utf-8')).hexdigest()
        )
        return response