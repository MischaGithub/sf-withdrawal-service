## 🧠 My Thought Process

1. **Keep It Simple**
   I didn’t want to over-engineer the solution since the core requirement was just to deduct an amount from an account and emit an event. I knew persistence and authentication were likely handled by other systems, so I avoided unnecessary complexity.

2. **Flask for the API**
   I used Flask because it's lightweight and perfect for prototyping or building small services like this one. It also lets me focus more on logic than infrastructure.

3. **Simulated Balance Instead of Real Database**
   I used a simulated balance (`SIMULATED_BALANCE`) instead of connecting to a database. The original task didn’t specify storage, so I assumed that managing state wasn’t necessary for the demo. I still showed how deduction would work.

4. **Try/Except for Error Handling**
   I made sure to wrap risky logic inside `try/except` blocks — like parsing JSON, handling decimal conversion, and calling external services (like SNS). This helps avoid crashing the app and makes it easier to debug.

5. **Environment Variables and dotenv**
   I didn’t want to hardcode AWS credentials or the topic ARN, so I used environment variables and loaded them with `python-dotenv`. This is good practice and keeps secrets out of the code.

6. **SNS Event Publishing (Optional but Present)**
   I included logic to publish a withdrawal event to AWS SNS if the `SNS_TOPIC_ARN` is configured. It’s done safely, so if credentials are wrong or missing, the app still works — it just logs a warning.

## Input Validations

- I made sure both `account_id` and `amount` are present before trying to process a withdrawal.
- I also validated the amount format using Python’s `Decimal` class to avoid float precision issues.

## Final Notes

This solution focuses on:
- Delivering a working API endpoint with proper input validation and event publishing
- Keeping logic easy to read and follow
- Using good practices like environment configs and exception handling

Thanks for the opportunity to work on this. I kept it clean and focused on what matters most: clarity, correctness, and simplicity.
