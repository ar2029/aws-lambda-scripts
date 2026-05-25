# aws-lambda-scripts

Python scripts using **AWS boto3** to automatically stop EC2 instances on a schedule, deployed as AWS Lambda functions with CloudWatch cron triggers.

---

## What It Does

Automates EC2 instance shutdown to reduce AWS costs by stopping instances when they are not needed (e.g. outside business hours). Configured with a cron job in AWS Console (CloudWatch Events / EventBridge).

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| AWS boto3 | AWS SDK — interact with EC2 |
| AWS Lambda | Serverless function runtime |
| AWS CloudWatch Events | Cron-based scheduling trigger |
| AWS EC2 | Compute instances being managed |

---

## Key Concepts

- Using `boto3.client("ec2")` to programmatically stop instances
- Filtering instances by tag or instance ID
- Lambda handler pattern: `def lambda_handler(event, context)`
- Scheduling via CloudWatch Events cron expression (e.g. `cron(0 18 * * ? *)` = 6pm daily)

---

## Files

| File | Description |
|---|---|
| `aws scripts.py` | Lambda function to stop EC2 instances |
| `README.md` | Documentation |

---

## How to Deploy

1. Zip `aws scripts.py` and upload to AWS Lambda
2. Set the handler to `aws scripts.lambda_handler`
3. Attach IAM role with `ec2:StopInstances` permission
4. Add a CloudWatch Events trigger with your desired cron schedule

---

## Skills Demonstrated

- Cloud automation with Python and AWS SDK (boto3)
- Serverless architecture with AWS Lambda
- Cost optimisation through scheduled instance management
- Infrastructure scripting applicable to DataOps and CloudOps workflows

---

*Part of a broader data engineering portfolio — [view more](https://ar2029.github.io/prasoon-portfolio/)*
