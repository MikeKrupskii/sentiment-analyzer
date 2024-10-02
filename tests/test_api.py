import pytest
from httpx import AsyncClient
from httpx import ASGITransport
from main import app

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "model_type, request_body, expected_response",
    [
        ("llm", {"text": "I love broccoli"}, {"sentiment": "Positive"}),
        ("llm", {"text": "I tolerate broccoli"}, {"sentiment": "Neutral"}),

        ("sentiment_analysis", {"text": "I love broccoli"}, {"sentiment": "Very Positive"}),
        ("sentiment_analysis", {"text": "I tolerate broccoli"}, {"sentiment": "Negative"})
    ]
)
async def test_analyze_text(model_type, request_body, expected_response):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(f"/analyze-text/?model_type={model_type}", json=request_body)
    assert response.status_code == 200
    assert response.json() == expected_response
