from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.models import EmailRequest
from app.models import EmailSummeryResponse
from app.services.summarizer import summarize_email

app = FastAPI(
    title="AI Email Summarizer API",
    description="AI service to summarize emails and extract action items",
    version="1.0.0"
)

@app.get("/")
def healthCheck():
    return {
        "status": "running",
        "service": "Email summarizer service"
    }

@app.post("/summarize")
def summerize(request: EmailRequest):
    try:
       
       if not request.email.strip:
           raise HTTPException(
               status_code=400,
               detail="email canot be emmpty"
           )
       result = summarize_email(request.email)
       return EmailSummeryResponse(**result)
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


