import json
from app.services.summarizer import summarize_email

def test_priority_classification():
    with open(
        "evaluation_data/email_cases.json"
        ) as file:
            cases = json.load(file)

            for case in cases:
              result = summarize_email(case["email"])
              assert (result["priority"]) == case["expected_priority"]