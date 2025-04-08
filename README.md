# Withdrawals Microservice (Flask + AWS SNS)

This is a simple Flask-based withdrawals microservice that simulates bank account deductions and publishes a withdrawal event to an AWS SNS topic. It's intended as part of a take-home technical assessment.

---

## Features

- Accepts `POST /withdraw` requests with account ID and amount
- Validates the request and simulates balance checks
- Publishes successful withdrawals to an AWS SNS topic
- Environment-based AWS config (safe & clean)
- Includes basic error handling and health check endpoint

---

## Technologies Used

- Python 3.9+
- Flask
- Boto3 (AWS SDK for Python)
- python-dotenv

---

## Project Structure

```
.
├── withdrawals.py           # Main Flask app
├── requirements.txt         # Python dependencies
├── README.md                # You're reading it
├── approach_notes.md        # My design & implementation notes
```

---

## Setup Instructions

Follow these steps to get the app running locally. This guide assumes **no prior experience** with Python or Flask.

### 1. Clone the repo

```bash
git clone https://github.com/MischaGithub/sf-withdrawal-service.git
cd sf-withdrawal-service
```

---

### 2. Create a virtual environment (recommended)

```bash
# Create environment (only once)
python3 -m venv venv

# Activate it
# macOS/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Set up environment variables

Create a copy of the example env file:

```bash
cp .env.example .env
```

Then fill in your real AWS credentials and SNS Topic ARN in the `.env` file:

```
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_REGION=us-east-1
SNS_TOPIC_ARN=arn:aws:sns:us-east-1:123456789012:your-topic-name
FLASK_DEBUG=true
```

> If you just want to run the app without publishing to AWS SNS, you can leave `SNS_TOPIC_ARN` blank or comment it out.

---

### 5. Run the app

```bash
python withdrawals.py
```

By default, it runs at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## How to Test

Use **Postman** or **curl** to send a request:

**POST** `/withdraw`  
**Content-Type:** `application/json`

```json
{
  "account_id": "abc123",
  "amount": 100
}
```

If successful, you'll receive:

```json
{
  "message": "Withdrawal successful",
  "new_balance": "900.00",
  "event": {
    "amount": "100",
    "account_id": "abc123",
    "status": "SUCCESSFUL"
  }
}
```

---

