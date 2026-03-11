# aws-serverless-task-api

Serverless Task Management API

This project demonstrates a serverless backend application built on Amazon Web Services using managed cloud services.

The API allows users to create and retrieve tasks using a scalable serverless architecture powered by API Gateway, AWS Lambda, and DynamoDB.

Architecture

The application uses the following AWS services:

API Gateway – receives HTTP requests

AWS Lambda – executes backend logic

DynamoDB – stores task data

IAM – controls service permissions

CloudWatch – logs and monitors function execution

Architecture flow:

Client
  ↓
API Gateway
  ↓
AWS Lambda
  ↓
DynamoDB

API Endpoints
Create a Task
POST /task

Example request body:

{
  "task": "Learn AWS Lambda",
  "priority": "high",
  "completed": false
}

Example response:

{
  "taskId": "uuid",
  "task": "Learn AWS Lambda",
  "priority": "high",
  "completed": false
}
Retrieve Tasks
GET /tasks

Example response:

[
  {
    "taskId": "uuid",
    "task": "Learn AWS Lambda",
    "priority": "high",
    "completed": false
  }
]
Technologies Used

Python

AWS Lambda

Amazon API Gateway

Amazon DynamoDB

IAM Roles and Policies

What I Learned

Building serverless applications using AWS managed services

Designing REST APIs with API Gateway

Connecting Lambda functions to DynamoDB

Managing service permissions with IAM

Debugging serverless systems using CloudWatch logs

Author

Joe Vonderlinden
