# Strands Agent Multi-Understanding

A repository for implementing and demonstrating multi-modal understanding capabilities using the Strands Agent framework. This project enables processing and analysis of various types of content including documents, images, and videos.

## Overview

This repository contains tools and examples for building AI agents capable of understanding and processing multiple types of media:
- Images (PNG, JPEG/JPG, GIF, WebP)
- Documents (PDF, CSV, DOCX, XLS, XLSX)
- Videos (MP4, MOV, AVI, MKV, WebM)

## Features

- Multi-modal content processing and analysis
- Integration with AWS Bedrock models
- Custom tools for different media types
- Example notebooks demonstrating implementation
- AWS CDK application for deploying Lambda functions
- Serverless implementation of multi-modal agents

## Repository Structure

- `/notebook/` - Contains Jupyter notebooks with implementation examples
  - `multi-undestanding.ipynb` - Main notebook demonstrating multi-modal capabilities
  - `video_reader.py` - Custom tool for video processing
- `/my_agent_cdk/` - AWS CDK application for deploying Lambda functions
  - `lambdas/code/lambda-s-agent` - Weather forecasting agent Lambda function
  - `lambdas/code/lambda-s-multimodal` - Multi-modal processing agent Lambda function

## Getting Started

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r notebook/requirements.txt
   ```
3. Configure AWS credentials for Bedrock access
4. Run the example notebooks to see the multi-modal agent in action

## CDK Application

The `/my_agent_cdk/` directory contains an AWS CDK application for deploying serverless Lambda functions that implement the Strands Agent framework:

1. **Weather Forecasting Agent** (`lambda-s-agent`): A Lambda function that uses Strands Agent to provide weather forecasting capabilities.

2. **Multi-modal Processing Agent** (`lambda-s-multimodal`): A Lambda function that processes different types of media (images, documents, videos) using the Strands Agent framework.

### Deploying the CDK Application

1. Navigate to the CDK directory:
   ```
   cd my_agent_cdk
   ```

2. Create a Python virtual environment and install dependencies:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Install Lambda layer dependencies:
   ```
   pip install -r layers/lambda_requirements.txt --python-version 3.12 --platform manylinux2014_aarch64 --target layers/strands/_dependencies --only-binary=:all:
   ```

4. Package the Lambda layers:
   ```
   python layers/package_for_lambda.py
   ```

5. Bootstrap your AWS environment (if not already done):
   ```
   cdk bootstrap
   ```

6. Deploy the stack:
   ```
   cdk deploy
   ```

For more details, see the [CDK application README](/my_agent_cdk/README.md).

## Requirements

- Python 3.8+
- AWS account with Bedrock access
- Required Python packages (see `notebook/requirements.txt`)
- AWS CDK (for deploying Lambda functions)

## Usage

The repository demonstrates how to create an agent that can process different types of media:

```python
from strands import Agent
from strands.models import BedrockModel
from strands_tools import image_reader, file_read
from video_reader import video_reader

# Create an agent with multi-modal capabilities
agent = Agent(
    system_prompt=MULTIMODAL_SYSTEM_PROMPT,
    tools=[image_reader, file_read, video_reader],
    model=bedrock_model
)

# Process different types of content
response = agent.process("Analyze this image: path/to/image.jpg")
```

## License

[Specify your license information here]

## Contributing

[Add contribution guidelines if applicable]
