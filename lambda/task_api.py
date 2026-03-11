import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Tasks")

def lambda_handler(event, context):

    method = event["requestContext"]["http"]["method"]

    # CREATE TASK
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

    # GET ALL TASKS
    elif method == "GET":

        response = table.scan()

        return {
            "statusCode": 200,
            "body": json.dumps(response["Items"])
        }

    # DELETE TASK
    elif method == "DELETE":

        path_params = event.get("pathParameters") or {}
        task_id = path_params.get("taskId")

        if not task_id:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "message": "Missing taskId in path"
                })
            }

        table.delete_item(
            Key={
                "taskId": task_id
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Task deleted",
                "taskId": task_id
            })
        }

    # METHOD NOT SUPPORTED
    else:

        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Unsupported HTTP method"
            })
        }
