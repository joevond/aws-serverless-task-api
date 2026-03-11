# aws-serverless-task-api

Serverless Task Management API

This project demonstrates a serverless backend application built on Amazon Web Services using managed cloud services.
The API allows users to create, delete, and retrieve tasks using a scalable serverless architecture powered by API Gateway, AWS Lambda, and DynamoDB.


Architecture flow:

Client
  ↓
API Gateway
  ↓
AWS Lambda
  ↓
DynamoDB


API Endpoints:

GET /tasks
DELETE /task/{taskId}
POST /task

Example POST request body:

{
  "task": "Learn AWS Lambda",
  "priority": "high",
  "completed": false
}


Example POST response:

{
  "taskId": "uuid",
  "task": "Learn AWS Lambda",
  "priority": "high",
  "completed": false
}


Technologies Used:

Python
AWS Lambda
Amazon API Gateway
Amazon DynamoDB
IAM Roles and Policies
CloudWatch


What I Learned:

Building serverless applications using AWS managed services
Designing REST APIs with API Gateway
Connecting Lambda functions to DynamoDB
Managing service permissions with IAM
Debugging serverless systems using CloudWatch logs

Author:
Joe Vonderlinden
