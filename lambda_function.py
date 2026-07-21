import json
import boto3

s3 = boto3.client("s3")

def lambda_handler(event, context):

    bucket = event["queryStringParameters"]["bucket"]
    key = event["queryStringParameters"]["key"]

    response = s3.head_object(
        Bucket=bucket,
        Key=key
    )

    result = {
        "File": key,
        "Size": response["ContentLength"],
        "Extension": key.split(".")[-1],
        "ContentType": response["ContentType"],
        "LastModified": str(response["LastModified"])
    }

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }