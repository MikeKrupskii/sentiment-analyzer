from fastapi import APIRouter
from src.services.sentiment_service import analyze_sentiment

router = APIRouter()

@router.post("/analyze-sentiment/")
async def analyze_sentiment_route(request: dict):
    text = request["text"]
    sentiment = await analyze_sentiment(text)
    return {"sentiment": sentiment}
