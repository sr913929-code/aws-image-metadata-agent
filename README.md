# Image Metadata Agent (AWS Serverless)

## Overview

This project is built using AWS Serverless services.

It reads image metadata stored in Amazon S3 and returns it through an HTTP API.

## AWS Services Used

- IAM
- Amazon S3
- AWS Lambda
- API Gateway
- CloudWatch

## Tech Stack

- Python
- boto3
- AWS

## Architecture

User
↓
API Gateway
↓
Lambda
↓
Amazon S3
↓
JSON Response

## Output

{
  "File":"a.png.webp",
  "Size":246726,
  "Extension":"webp",
  "ContentType":"image/webp",
  "LastModified":"2026-07-20"
}

## Author

Sanjay Kumar