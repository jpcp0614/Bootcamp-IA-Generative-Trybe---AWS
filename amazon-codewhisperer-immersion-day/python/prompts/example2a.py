# Create a function to create a DynamoDB table
import boto3
from botocore.exceptions import ClientError


def create_table(table_name, partition_key, sort_key):
    dynamodb = boto3.resource('dynamodb')

    try:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': partition_key,
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': sort_key,
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': partition_key,
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': sort_key,
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        return table
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None
