## AWS Deployment Details

**AWS Region:** US East (Ohio) – `us-east-2`

**Lambda Function:** `ImageResizerFunction`

**Step Functions State Machine:** `ImageProcessingStateMachine`

**Step Functions ARN:**
```text
arn:aws:states:us-east-2:448678333340:stateMachine:ImageProcessingStateMachine
```

**API Gateway URL:**
```text
https://htos9gd1vj.execute-api.us-east-2.amazonaws.com/prod
```

**Testing Results:**
- API Gateway returned HTTP 200.
- Step Functions execution completed successfully.
- Image resizing was tested using an S3 image event.
