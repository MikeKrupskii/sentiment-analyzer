import requests
from src.config import HUGGINGFACE_API_KEY, HUGGINGFACE_MODEL_URL

class HuggingFaceClient:
    def __init__(self):
        self.api_url = HUGGINGFACE_MODEL_URL
        self.headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

    def send_request(self, text: str):
        payload = {"inputs": text}
        response = requests.post(self.api_url, headers=self.headers, json=payload)

        if response.status_code != 200:
            raise ValueError(f"Failed to connect to HuggingFace API: {response.status_code}")

        return response.json()

def get_huggingface_client():
    return HuggingFaceClient()
