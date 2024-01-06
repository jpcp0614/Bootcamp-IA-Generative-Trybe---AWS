import os
import boto3
import json
import re


QUEUE_URL = os.getenv("QUEUE_URL", default="test")
sqs = boto3.client('sqs')


# Function to send the message to SQS
def send_message_to_sqs(body):
    print('Sending message to SQS')
    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(body)
    )


# Function to validate an email address using a regular expression
def validate_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False


# Lambda function to publish user to a queue
def lambda_handler(event, context):
    print(event)
    try:
        body = json.loads(event['body'])

        # Validate email
        if not validate_email(body['email']):
            return {'statusCode': 400}

        send_message_to_sqs(body)
        return {'statusCode': 200}
    except Exception as e:
        print(e)
        return {'statusCode': 500}
