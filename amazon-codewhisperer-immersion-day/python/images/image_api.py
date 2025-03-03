import os
import boto3
import json
import base64

BUCKET_NAME = os.getenv("BUCKET_NAME", default="mybucket")
s3 = boto3.client("s3")


# Upload the image to S3
def upload_image_to_s3(key, file, type):
    print("Uploading image to S3")
    s3.put_object(
        Body=file, Bucket=BUCKET_NAME, Key=key, ContentType="image/jpeg"
    )


# Function to moderate image with AWS Rekognition
def moderate_image(image):
    client = boto3.client("rekognition")
    response = client.detect_moderation_labels(Image={"Bytes": image})
    print(response)
    return len(response["ModerationLabels"]) == 0


# Lambda function to upload an image to S3
def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        key = body["file_name"]
        type = body["file_type"]
        image = base64.b64decode(body["file_content"])

        # Validate the image
        if not moderate_image(image):
            return {"statusCode": 400}

        upload_image_to_s3(key, image, type)
        return {"statusCode": 200}
    except Exception as e:
        print(e)
        return {"statusCode": 500}
