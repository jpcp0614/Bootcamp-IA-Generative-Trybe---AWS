# Function to create a DynamoDB table with employee ID as primary key and ReadCapacityUnits at 100 and WriteCapacityUnits at 200
import boto3


def create_employee_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url="XXXXXXXXXXXXXXXXXXXXX")

    table = dynamodb.create_table(
        TableName='Employee',
        KeySchema=[
            {
                'AttributeName': 'EmployeeID',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'EmployeeID',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 100,
            'WriteCapacityUnits': 200
        }
    )
    print("Table status:", table.table_status)
    return table
