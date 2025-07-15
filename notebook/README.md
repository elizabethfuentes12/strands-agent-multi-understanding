# Multi-Understanding Notebooks

This directory contains notebooks and supporting files for demonstrating multi-modal understanding capabilities using the Strands Agent framework.

## Contents

- `multi-understanding.ipynb` - Main notebook demonstrating how to process and analyze different types of media (images, documents, videos)
- `video_reader.py` - Custom tool implementation for video processing
- `requirements.txt` - Required Python packages for running the notebooks
- `data-sample/` - Directory containing sample files for testing

## Getting Started

1. Create a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure AWS credentials for Bedrock access

4. Open `multi-understanding.ipynb` to see the multi-modal agent in action

## Notebook Overview

The `multi-understanding.ipynb` notebook demonstrates:

1. Setting up a Strands Agent with multi-modal capabilities
2. Configuring AWS Bedrock for model inference
3. Processing different types of media:
   - Images using `image_reader`
   - Documents using `file_read`
   - Videos using `video_reader`
4. Analyzing content and generating human-readable responses

## Sample Files

The `data-sample/` directory includes sample files for testing:
- `diagram.jpg` - Sample image file for image analysis
- `Welcome-Strands-Agents-SDK.pdf` - Sample PDF document for text extraction
- `Prompt-Engineering.pdf` - Sample PDF document for content analysis
- `moderation-video.mp4` - Sample video file for video frame extraction and analysis

## Video Reader Tool

The `video_reader.py` file implements a custom tool for processing video content. It extracts frames from videos at specified intervals, converts them to base64-encoded images, and provides them to the agent for analysis. This enables the agent to understand and describe video content by analyzing key frames throughout the video.
