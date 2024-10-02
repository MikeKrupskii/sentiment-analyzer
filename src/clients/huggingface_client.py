import requests
from src.config import HUGGINGFACE_API_KEY, SENTIMENT_ANALYSIS_MODEL_URL, LLM_CHAT_COMPLETION_MODEL_URL

class HuggingFaceClient:
    def __init__(self, llm=False):
        self.api_url = LLM_CHAT_COMPLETION_MODEL_URL if llm else SENTIMENT_ANALYSIS_MODEL_URL
        self.headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

    def send_request(self, text: str):
        payload = {"inputs": text}
        response = requests.post(self.api_url, headers=self.headers, json=payload)

        if response.status_code != 200:
            raise ValueError(f"Failed to connect to HuggingFace API: {response.status_code}")

        return response.json()

def get_huggingface_client(llm=False):
    return HuggingFaceClient(llm=llm)
