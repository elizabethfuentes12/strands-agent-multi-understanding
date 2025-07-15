'''

{"prompt": '',
"s3object": ''
}

'''

import boto3
from strands.models import BedrockModel
from strands import Agent
from strands_tools import image_reader, file_read
from video_reader import video_reader
from strands.tools import tool
import os
from file_utils import download_file
from typing import Dict, Any


#os.environ["BYPASS_TOOL_CONSENT"] = "true"
region_name = os.environ["REGION_NAME"]
model_id = os.environ["MODEL_ID"]

client_s3 = boto3.client('s3')
session = boto3.Session(region_name='us-west-2')
base_path="/tmp/"

# Define a weather-focused system prompt
MULTIMODAL_SYSTEM_PROMPT = """ You are a helpful assistant that can process documents, images, and videos. 
Analyze their contents and provide relevant information.

You can:

1. For PNG, JPEG/JPG, GIF, or WebP formats use image_reader to process file
2. For PDF, csv, docx, xls or xlsx formats use file_read to process file  
3. For MP4, MOV, AVI, MKV, WebM formats use video_reader to process file
4. Just deliver the answer

When displaying responses:
- Format answers data in a human-readable way
- Highlight important information
- Handle errors appropriately
- Convert technical terms to user-friendly language
- Always reply in the original user language

Always reply in the original user language.
"""

def handler(event: Dict[str, Any], _context) -> str:
    print(event)
    try: 

        prompt = event.get('prompt')
        s3object = event.get('s3object')

        s3bucket = s3object.split("/")[2]
        s3key = "/".join(s3object.split("/")[3:])
        filename = s3object.split("/")[-1]
        ext = filename.split(".")[-1]

        print("s3object: ",s3object)
        print("bucket: ",s3bucket)
        print("key: ",s3key)
        print("filename: ", filename)
        print("ext: ", ext)


        if ext == 'MP4': #, MOV, AVI, MKV, WebM 
            print("es video")
            final_prompt = f"{prompt}, file_path: {s3object}"
            print("final_prompt: ", final_prompt)
        else:
            path_file = base_path +filename
            final_prompt = f"{prompt}, file_path: {path_file}"
            download_file(base_path,s3bucket, s3key, filename)
            print("final_prompt: ", final_prompt)


        bedrock_model = BedrockModel(
            #model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
            model_id= model_id,
            boto_session=session,
            streaming=False
        )

        # Updated multimodal agent with video support
        multimodal_agent = Agent(
            system_prompt=MULTIMODAL_SYSTEM_PROMPT,
            tools=[image_reader, file_read, video_reader],
            model=bedrock_model
        )

        result_agent = multimodal_agent(final_prompt)
        print(result_agent)
        return str(result_agent.message['content'][0]['text'])
    
    except:
        return str("Error")