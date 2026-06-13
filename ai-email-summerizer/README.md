AI Email Summarizer

# AI Email Summarizer

AI-powered email assistant that summarizes emails, extracts action items, detects priority, analyzes sentiment, and suggests replies.



## 🚀 Live Demo
[<Streamlit URL>/demo](https://ai-tools-cssz8kir7kwmc6le7domwz.streamlit.app)

API:
[<Render URL>/docs](https://ai-email-summarizer-api.onrender.com/docs)

# Screenshot 

<img width="883" height="770" alt="image" src="https://github.com/user-attachments/assets/d2daef85-e739-437d-ad9c-bd76e3a8c1d8" />


## Problem

Professionals receive hundreds of emails and spend time identifying:

- What is important?
- What requires action?
- Who owns each task?
- What response should be sent?

Manual email processing reduces productivity.


## Solution

This AI assistant automatically extracts:
- Email summary
- Priority classification
- Sentiment
- Action items
- Suggested reply

using Large Language Models.

## Architecture

User
 ↓
Streamlit UI
 ↓
FastAPI Backend
 ↓
AI Provider Layer
 ↓
LLM Model

## Tech Stack

Backend:
- Python
- FastAPI
- Pydantic
- uv

AI:
- LLM APIs
- GitHub Models
- Gemini
- Prompt Engineering
- Structured JSON Output

Testing:
- Pytest
- AI Evaluation Tests

Deployment:
- Render
- Streamlit Cloud

## Features

✔ Email summarization  
✔ Priority detection  
✔ Sentiment analysis  
✔ Action item extraction  
✔ Suggested response generation  
✔ Multiple AI provider support  
✔ API-first architecture  

## AI Engineering Concepts

Implemented:

- Prompt engineering
- Model abstraction
- Structured output parsing
- LLM evaluation
- AI quality testing
- Provider switching

## Run Locally

Install:
uv sync

Start API:
uv run uvicorn app.api:app --reload

Start UI:
uv run streamlit run streamlit_app.py

