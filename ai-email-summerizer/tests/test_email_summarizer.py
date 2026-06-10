from app.models import EmailSummeryResponse

def test_email_response_schema():
    fake_ai_response = {
        "summary": "Meeting tomorrow",
        "priority": "high",
        "sentiment": "neutral",
        "action_items": [
            {
                "task": "Attend meeting",
                "owner": "Ram",
                "deadline": "Tomorrow"
            }
        ],
        "suggested_reply": "Thanks, I will join."
    }

    result = EmailSummeryResponse(**fake_ai_response)

    assert result.priority == "high"