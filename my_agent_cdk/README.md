# AWS CDK Lambda Deployment Example (Python)

## Introduction

This is a Python-based CDK (Cloud Development Kit) example that demonstrates how to deploy a Python function to AWS Lambda. The example deploys a weather forecaster application that requires AWS authentication to invoke the Lambda function.

This is the Python version of the TypeScript CDK stack found in the parent directory.

## Prerequisites

- [AWS CLI](https://aws.amazon.com/cli/) installed and configured
- Python 3.8 or later
- [jq](https://stedolan.github.io/jq/) (optional) for formatting JSON output

## Project Structure

- `agent_lambda/` - Contains the CDK stack definition in Python
- `app.py` - Main CDK application entry point
- `package_for_lambda.py` - Python script that packages Lambda code and dependencies into deployment archives
- `lambda/` - Contains the Python Lambda function code
- `packaging/` - Directory used to store Lambda deployment assets and dependencies

## Setup and Deployment

1. Create a Python virtual environment and install dependencies:

```bash
# Create a Python virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install CDK dependencies
pip install -r requirements.txt

# Install Python dependencies for lambda with correct architecture
pip install -r layers/lambda_requirements.txt --python-version 3.12 --platform manylinux2014_aarch64 --target layers/strands/_dependencies --only-binary=:all:
```

2. Package the lambda:

```bash
python layers/package_for_lambda.py
```

3. Bootstrap your AWS environment (if not already done):

```bash
cdk bootstrap
```

4. Deploy the lambda:

```bash
cdk deploy
```

## Usage

After deployment, you can invoke the Lambda function using the AWS CLI or AWS Console. The function requires proper AWS authentication to be invoked.

```bash
aws lambda invoke --function-name AgentSFunction \
      --region us-east-2 \
      --cli-binary-format raw-in-base64-out \
      --payload '{"prompt": "What is the weather in New York?"}' \
      output.json
```

If you have jq installed, you can output the response from output.json like so:

```bash
jq -r '.' ./output.json
```

Otherwise, open output.json to view the result.

## Cleanup

To remove all resources created by this example:

```bash
cdk destroy
```

## Key Differences from TypeScript Version

- Uses Python CDK constructs instead of TypeScript
- Main entry point is `app.py` instead of `bin/cdk-app.ts`
- Stack definition is in `agent_lambda/agent_lambda_stack.py`
- Uses Python naming conventions (snake_case instead of camelCase)
- Dependencies managed via `requirements.txt` instead of `package.json`

## Additional Resources

- [AWS CDK Python Documentation](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html)
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Python CDK API Reference](https://docs.aws.amazon.com/cdk/api/v2/python/)
