from app.ai.client import get_ai_client
from app.ai.prompts import EMAIL_SUMMARY_PROMPT
from app.ai.provider import MODEL
import json
from app.core.logger import get_logger

logger = get_logger("Summerizer")

def summarize_email(email_text: str) -> str:
    logger.info("Starting email summarization")
    response = get_ai_client().chat.completions.create(
           model=MODEL,
           messages=[
            {
            "role": "user",
            "content": EMAIL_SUMMARY_PROMPT + "\n\nEmail:\n" + email_text
            }
        ]
    )
    result_text = response.choices[0].message.content
    result_text = (result_text.replace("```json", "").replace("```", "").strip())
    if result_text is None:
        raise ValueError("AI returned empty response")
    
    try:
      result = json.loads(result_text)
      return result
    except:
       raise ValueError("There is problme in json response")  

    
    
    