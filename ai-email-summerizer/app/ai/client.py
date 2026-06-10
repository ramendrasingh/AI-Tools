from dotenv import load_dotenv
import os
from openai import OpenAI
from app.ai.provider import BASE_URL

def get_ai_client():
    load_dotenv(override=True)
    api_key = _get_api_key()
    if not api_key:
        raise ValueError("Missing GITHUB_TOKEN")

    client = OpenAI(
        base_url=BASE_URL,
        api_key=api_key
    )
    return client

def _get_api_key():
    if BASE_URL.__contains__("github"):
        return os.getenv("GITHUB_TOKEN")
    elif BASE_URL.__contains__("openrouter"):
        return os.getenv("OPENROUTER_API_KEY")
    elif BASE_URL.__contains__("googleapis"):
        return os.getenv("GEMINI_API_KEY")
    else:
        ""