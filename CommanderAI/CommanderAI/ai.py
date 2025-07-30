import os
import requests

GEMINI_API_URL = "https://api.generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText"

API_KEY = os.getenv("GEMINI_API_KEY")

def ask_gemini(prompt_text):
    headers = {"Content-Type": "application/json"}
    params = {"key": API_KEY}
    payload = {
        "prompt": {"text": prompt_text},
        "temperature": 0.2,
        "max_output_tokens": 300
    }
    resp = requests.post(GEMINI_API_URL, headers=headers, params=params, json=payload)
    resp.raise_for_status()
    return resp.json()["candidates"][0]["output"]
