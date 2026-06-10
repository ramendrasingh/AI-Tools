from unittest.mock import patch

from app.services.summarizer import summarize_email

def test_email_summarizer_without_ai():
    fack_response = {
        "summary": "Meeting tomorrow",
        "priority": "medium",
        "sentiment": "neutral",
        "action_items": [],
        "suggested_reply": "Thanks"
    }

    with patch(
        "app.services.summarizer.summarize_email",
        return_value=fack_response
    ):
        result = summarize_email(
            "schedule meeting tomorrow"
        )

        assert result["priority"] == "medium"