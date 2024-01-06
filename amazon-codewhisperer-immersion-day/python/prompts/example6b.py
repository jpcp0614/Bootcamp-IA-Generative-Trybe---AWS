import boto3

# Create SES client
ses = boto3.client('ses')

# Function to verify email address


def verify_email_address(email_address):
    response = ses.verify_email_address(
        EmailAddress=email_address
    )
    print(response)
