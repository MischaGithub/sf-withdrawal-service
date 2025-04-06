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

# A class to represent the withdrawal event we want to publish
class WithdrawalEvent:
    def __init__(self, amount, account_id, status):
        self.amount = amount
        self.account_id = account_id
        self.status = status

    def to_dict(self):
        return {
            "amount": str(self.amount),
            "account_id": str(self.account_id),
            "status": self.status
        }


@app.route("/withdraw", methods=["POST"])
def withdraw():
    try:
        data = request.get_json()

        if not data or "amount" not in data or "account_id" not in data:
            return jsonify({"error": "Missing account_id or amount"}), 400

        amount = Decimal(str(data["amount"]))
        account_id = data["account_id"]

        if amount > SIMULATED_BALANCE:
            return jsonify({"error": "Insufficient funds"}), 400

        new_balance = SIMULATED_BALANCE - amount
        event = WithdrawalEvent(amount, account_id, "SUCCESSFUL")

        # Try to publish the withdrawal event to SNS
        # In a real system, this would notify other systems about the transaction
        if SNS_TOPIC_ARN:
            try:
                sns_client.publish(
                    TopicArn=SNS_TOPIC_ARN,
                    Message=str(event.to_dict())
                )
            except Exception as sns_err:
                # Log but don't fail if SNS publish doesn't work
                print("Warning: Failed to publish to SNS", sns_err)


        return jsonify({
            "message": "Withdrawal successful",
            "new_balance": str(new_balance),
            "event": event.to_dict()
        })

    except Exception as e:
        print("Exception:", str(e))
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def health_check():
    return "✅ App is up", 200


if __name__ == "__main__":
    app.run(debug=True)
