import json


def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
        "1": 4
    }

    return {"statusCode": 200, "body": json.dumps(body)}
