import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Tasks")

def lambda_handler(event, context):

    method = event["requestContext"]["http"]["method"]

    if method == "POST":

        body = json.loads(event["body"])

        task_id = str(uuid.uuid4())

        item = {
            "taskId": task_id,
            "task": body.get("task"),
            "priority": body.get("priority", "normal"),
            "completed": body.get("completed", False),
            "createdAt": datetime.utcnow().isoformat()
        }

        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "body": json.dumps(item)
        }

    elif method == "GET":

        response = table.scan()

        return {
            "statusCode": 200,
            "body": json.dumps(response["Items"])
        }
