import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_analyze_sentiment_route_positive():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/analyze-sentiment/", json={"text": "I love broccoli"})
    assert response.status_code == 200
    assert response.json() == {"sentiment": "Very Positive"}

@pytest.mark.asyncio
async def test_analyze_sentiment_route_negative():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/analyze-sentiment/", json={"text": "I hate broccoli"})
    assert response.status_code == 200
    assert response.json() == {"sentiment": "Very Negative"}
