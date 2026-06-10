from dotenv import load_dotenv
import json
from services.summarizer import summarize_email


email_text = "Hi team, we need to finalize the payment gateway integration by Friday. Rahul will handle backend changes, and Priya should test the checkout flow on Android and iOS. Please share blockers by tomorrow evening."


try:
    result_text = summarize_email(email_text= email_text)
    result = json.loads(result_text)
    print(result["summary"])
except json.JSONDecodeError:
    print("AI returned invalid JSON")

except Exception as error:
    print(f"Something failed: {error}")


