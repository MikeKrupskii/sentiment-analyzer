import pytest
from src.services.sentiment_service import analyze_sentiment
from unittest.mock import MagicMock

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "mock_response, expected_sentiment",
    [
        ([{"label": "1 star", "score": 0.9}], "Very Negative"),
        ([{"label": "2 stars", "score": 0.9}], "Negative"),
        ([{"label": "3 stars", "score": 0.9}], "Neutral"),
        ([{"label": "4 stars", "score": 0.9}], "Positive"),
        ([{"label": "5 stars", "score": 0.9}], "Very Positive"),
    ]
)
async def test_analyze_sentiment(mock_response, expected_sentiment):
    mock_client = MagicMock()
    mock_client.send_request.return_value = [mock_response]

    sentiment = await analyze_sentiment("Test text", huggingface_client=mock_client)
    assert sentiment == expected_sentiment
