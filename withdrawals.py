from flask import Flask, request, jsonify
from decimal import Decimal
import boto3
import os
from dotenv import load_dotenv


# Load variables from .env file into environment
load_dotenv()

app = Flask(__name__)

# Just simulating an account balance for now
SIMULATED_BALANCE = Decimal("1000.00")

# Setup the SNS client using credentials from environment variables
sns_client = boto3.client(
    "sns",
    region_name=os.getenv("AWS_REGION", "us-east-1"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

# Get the SNS topic ARN from env
SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")