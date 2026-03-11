#Title # aws-serverless-task-api

##Section Serverless Task Management API

###Subsection This project demonstrates a serverless backend application built on Amazon Web Services using managed cloud services.
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

Retrieve All Tasks:

GET /tasks

Delete a Task:

DELETE /task/{taskId}

Create a Task:

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

Amazon CloudWatch

What I Learned:

Building serverless applications using AWS managed services

Designing REST APIs with Amazon API Gateway

Connecting Lambda functions with DynamoDB for data persistence

Managing permissions using IAM roles and policies

Debugging and monitoring serverless applications using CloudWatch logs

Future Improvements

- Add task update endpoint (PATCH /task/{taskId})
  
- Implement frontend UI hosted on S3
  
- Add authentication using Amazon Cognito
  
- Add filtering and querying for tasks

Author
Joe Vonderlinden
