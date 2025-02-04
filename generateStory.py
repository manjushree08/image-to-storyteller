import boto3
import json
import base64
import os
from dotenv import find_dotenv, load_dotenv
from transformers import pipeline 
from kokoro import KPipeline
from IPython.display import display, Audio
import soundfile as sf
import re
import json

load_dotenv(find_dotenv())
from huggingface_hub import InferenceClient

# AWS Configuration
ENDPOINT_NAME = "YOUR_ENDPOINT_NAME"  # Replace with your endpoint name
REGION = "YPUR_REGION"  # Change to your region

# Initialize SageMaker runtime client
sagemaker_runtime = boto3.client("sagemaker-runtime", 
                            aws_access_key_id="YOUR_aws_access_key_id",
                            aws_secret_access_key="YOUR_aws_secret_access_key",
                            region_name=REGION)

# Load and Encode Image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Set image path

def generate_image_to_text(image_path):
    # Prepare payload for SageMaker (Modify based on model requirement)
    encoded_image = encode_image(image_path)
    payload = json.dumps({
        "inputs": encoded_image,  # Base64-encoded image
        "parameters": {"max_new_tokens": 50}  # Optional: Adjust token limit
    })

    # Invoke SageMaker Endpoint
    response = sagemaker_runtime.invoke_endpoint(
    EndpointName=ENDPOINT_NAME,
    ContentType="application/json",
    Body=payload
    )

    # Parse Response
    result = json.loads(response["Body"].read().decode("utf-8"))
    return result[0]["generated_text"]

def generate_text_to_story(caption):
    client = InferenceClient(
	provider="together",
	api_key="HF_Token"
    )

    prompt = f"""You are a story teller;
    you can generate a short story based on a simple narative, 
    the story should be no more than 20 words
    make the story like bedtime story
    Context: {caption}
    Give your response as a json with key as Story
    """
    print(prompt)
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    completion = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1", 
        messages=messages, 
        max_tokens=500
    )
    
    print(completion.choices[0].message)
    json_match = re.search(r"```json\n(.*?)\n```", completion.choices[0].message.content, re.DOTALL)
    story = ''
    if json_match:
        json_content = json_match.group(1)
        try:
            json_data = json.loads(json_content)  # Parse JSON
            story = json_data.get("Story", "Story key not found")
            print(story)
        except json.JSONDecodeError:
            print("Invalid JSON format")
    else:
        print("No JSON found in text")

    return story

def generate_story_to_audio(story, folder):
    pipeline = KPipeline(lang_code='a') # <= make sure lang_code matches voice

    # 4️⃣ Generate, display, and save audio files in a loop.
    generator = pipeline(
    story, voice='af_heart', # <= change voice here
    speed=1, split_pattern=r'\n+'
    )

    for i, (gs, ps, audio) in enumerate(generator):
        print(i)  # i => index
        print(gs) # gs => graphemes/text
        print(ps) # ps => phonemes
        display(Audio(data=audio, rate=24000, autoplay=i==0))
        sf.write(f'./{folder}/audio.wav', audio, 24000) # save each audio file
    





