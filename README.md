# Serverless Image Processing Pipeline

## 1. Project Overview

This project uses AWS services to automatically resize images uploaded to an Amazon S3 bucket. The resized images are saved in a separate S3 bucket.

## 2. Team Members

- Deep Patel
- Harsh Viradiya
- Dvij Patel

## 3. AWS Services Used

- Amazon S3 – Stores original and resized images.
- AWS Lambda – Resizes images using Python.
- Pillow – Image processing library.
- AWS Lambda Layer – Provides the Pillow library.
- AWS Step Functions – Controls the processing workflow.
- Amazon API Gateway – Starts the Step Functions execution.
- Amazon CloudWatch – Stores execution logs.

## 4. Project Structure

```text
Serverless Image Processing/
├── lambda/
│   └── lambda_function.py
├── step-functions/
│   └── state-machine.json
├── screenshots/
├── testing/
└── README.md
```

## 5. S3 Bucket Configuration

**Original Images Bucket**

`deep-harsh-dvij-original-images-2026`

**Resized Images Bucket**

`deep-harsh-dvij-resized-images-2026`

## 6. Lambda Configuration

- Function name: `ImageResizerFunction`
- Runtime: Python 3.12
- Library: Pillow
- Environment variable: `OUTPUT_BUCKET`
- Trigger: S3 Object Created event

The Lambda function downloads an uploaded image, resizes it to a maximum size of 800 × 800 pixels, and uploads the resized image to the output bucket.

## 7. Step Functions Workflow

State machine name: `ImageProcessingStateMachine`

The workflow contains:

1. ResizeImage – Calls the Lambda function.
2. CheckResult – Checks the processing result.
3. Success – Completes the workflow successfully.
4. Fail – Handles unsuccessful processing.

## 8. API Gateway Configuration

- API name: `ImageProcessingAPI`
- Method: POST
- Stage: `prod`
- AWS Region: `us-east-2`

API Endpoint:

`https://htos9gd1vj.execute-api.us-east-2.amazonaws.com/prod`

## 9. Testing Results

The project was tested using Postman.

- API Gateway returned HTTP 200.
- Step Functions execution completed successfully.
- The image processing workflow was tested using an S3 image event.

## 10. Deployment Instructions

1. Create two Amazon S3 buckets.
2. Create the Lambda function using Python 3.12.
3. Add the Pillow Lambda Layer.
4. Configure the `OUTPUT_BUCKET` environment variable.
5. Configure the S3 upload trigger.
6. Create the Step Functions state machine.
7. Configure API Gateway to start the state machine.
8. Deploy the API to the `prod` stage.
9. Test the API using Postman.
10. Verify the resized image in the output bucket.

## 11. AWS Resource Details

**AWS Region:** `us-east-2`

**Lambda Function:** `ImageResizerFunction`

**Step Functions ARN:**

`arn:aws:states:us-east-2:448678333340:stateMachine:ImageProcessingStateMachine`

**API Gateway URL:**

`https://htos9gd1vj.execute-api.us-east-2.amazonaws.com/prod`

## 12. Demonstration Video

The project demonstration video will be included with the final submission.

## 13. Conclusion

This project demonstrates how AWS serverless services can work together to process images. It uses S3, Lambda, Step Functions, and API Gateway to create an automated image resizing workflow.