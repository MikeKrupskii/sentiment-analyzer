from dotenv import load_dotenv
import os

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
SENTIMENT_ANALYSIS_MODEL_URL = os.getenv("SENTIMENT_ANALYSIS_MODEL_URL")
LLM_CHAT_COMPLETION_MODEL_URL = os.getenv("LLM_CHAT_COMPLETION_MODEL_URL")

if not HUGGINGFACE_API_KEY:
    raise ValueError("HuggingFace API key is missing from environment variables.")

if not SENTIMENT_ANALYSIS_MODEL_URL and not LLM_CHAT_COMPLETION_MODEL_URL:
    raise ValueError("At least one HuggingFace model URL must be set in environment variables.")
