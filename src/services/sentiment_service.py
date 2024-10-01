import requests
from src.clients.huggingface_client import get_huggingface_client

async def analyze_sentiment(text: str, huggingface_client = None):
    if huggingface_client is None:
        huggingface_client = get_huggingface_client()

    result = huggingface_client.send_request(text)
    print(result)

    if isinstance(result, list) and isinstance(result[0], list):
        # Result contains positive and negative labels with respective scores
        sentiment = max(result[0], key=lambda x: x["score"])["label"]
        return sentiment
    else:
        raise ValueError("Unexpected response structure from HuggingFace API")
