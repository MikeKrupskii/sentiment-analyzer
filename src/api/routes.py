from fastapi import APIRouter
from src.services.sentiment_service import analyze_sentiment
from pydantic import BaseModel

router = APIRouter()

class SentimentRequest(BaseModel):
    text: str

@router.post("/analyze-sentiment/", response_model=dict)
async def analyze_sentiment_route(request: SentimentRequest) -> dict:
    text = request.text
    sentiment = await analyze_sentiment(text)
    return {"sentiment": sentiment}
