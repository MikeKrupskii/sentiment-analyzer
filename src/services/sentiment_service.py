import requests
from src.config import HUGGINGFACE_API_KEY

async def analyze_sentiment(text: str):
    url = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

    payload = {"inputs": text}

    response = requests.post(url, headers=headers, json=payload)

    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")

    result = response.json()

    if isinstance(result, list) and isinstance(result[0], list):
        # Result contains positive and negative labels with respective scores
        sentiment = max(result[0], key=lambda x: x["score"])["label"]
        return sentiment
    else:
        raise ValueError("Unexpected response structure from HuggingFace API")