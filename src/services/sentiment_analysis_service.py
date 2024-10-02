from src.clients.huggingface_client import get_huggingface_client

async def analyze_sentiment(text: str, huggingface_client = None):
    if huggingface_client is None:
        huggingface_client = get_huggingface_client(llm=False)

    result = huggingface_client.send_request(text)

    # Result contains labels from 1 to 5 stars with respective scores
    # https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment
    label_map = {
        "1 star": "Very Negative",
        "2 stars": "Negative",
        "3 stars": "Neutral",
        "4 stars": "Positive",
        "5 stars": "Very Positive"
    }

    if isinstance(result, list) and isinstance(result[0], list):
        # Return the label with the highest score
        highest_confidence_label = max(result[0], key=lambda x: x["score"])["label"]
        sentiment = label_map.get(highest_confidence_label, "Unknown")
        return sentiment
    else:
        raise ValueError("Unexpected response structure from HuggingFace API")
