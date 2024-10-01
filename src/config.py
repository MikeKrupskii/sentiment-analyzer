from dotenv import load_dotenv
import os

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
HUGGINGFACE_MODEL_URL = os.getenv("HUGGINGFACE_MODEL_URL")

if not HUGGINGFACE_API_KEY or not HUGGINGFACE_MODEL_URL:
    raise ValueError("Missing HuggingFace configuration params in environment variables")
