import json
import sagemaker
import boto3
from sagemaker.huggingface import HuggingFaceModel, get_huggingface_llm_image_uri

REGION = ['YOUR_REGION'] # Change to your region

# Manually set credentials
boto_session = boto3.Session(
    aws_access_key_id= ['YOUR_Access_Key'],
    aws_secret_access_key=['YOUR_Secret_Key'],
    region_name=REGION,
)

sagemaker_session = sagemaker.Session(boto_session=boto_session )

try:
	role = sagemaker.get_execution_role()
except ValueError:
	iam = boto3.client('iam')
	role = iam.get_role(RoleName='sagemaker_execution_role')['Role']['Arn']

# Hub Model configuration. https://huggingface.co/models
hub = {
	'HF_MODEL_ID':'Salesforce/blip-image-captioning-base',
	'HF_TOKEN': ['HF_Toke'],
    'HF_TASK':'image-to-text',
}


# create Hugging Face Model Class
huggingface_model = HuggingFaceModel(
	transformers_version='4.37.0',
	pytorch_version='2.1.0',
	py_version='py310',
	env=hub,
	role=role, 
)

# deploy model to SageMaker Inference
predictor = huggingface_model.deploy(
	initial_instance_count=1, # number of instances
	instance_type='ml.m5.xlarge', # ec2 instance type
	 endpoint_name= 'imagetotext4'
)