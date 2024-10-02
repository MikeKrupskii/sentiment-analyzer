from fastapi import APIRouter, Query
from src.services.sentiment_analysis_service import analyze_sentiment
from src.services.llm_analysis_service import analyze_with_llm
from pydantic import BaseModel

router = APIRouter()

class SentimentRequest(BaseModel):
    text: str

@router.post("/analyze-text/", response_model=dict)
async def analyze_text_route(
    request: SentimentRequest,
    model_type: str = Query("llm", enum=["sentiment_analysis", "llm"])) -> dict:
    text = request.text

    if model_type == "sentiment_analysis":
        sentiment = await analyze_sentiment(text)
    else:
        sentiment = await analyze_with_llm(text)

    return {"sentiment": sentiment}
