import pytest
from unittest.mock import MagicMock
from src.services.llm_analysis_service import analyze_with_llm
from fastapi import HTTPException


@pytest.mark.asyncio
async def test_analyze_with_llm_positive():
    mock_client = MagicMock()
    mock_client.send_request.return_value = [
        {'generated_text': 'Assistant: Positive'}
    ]

    sentiment = await analyze_with_llm("I love broccoli", huggingface_client=mock_client)

    assert sentiment == "Positive"

@pytest.mark.asyncio
async def test_analyze_with_llm_busy_model():
    mock_client = MagicMock()
    mock_client.send_request.side_effect = [
        ValueError("Model too busy, unable to get response in less than 60 second(s)"),
        ValueError("Model too busy, unable to get response in less than 60 second(s)"),
        [{'generated_text': 'Assistant: Neutral'}]
    ]

    sentiment = await analyze_with_llm("I love broccoli", huggingface_client=mock_client, retries=3, backoff=1)

    assert sentiment == "Neutral"

@pytest.mark.asyncio
async def test_analyze_with_llm_model_too_busy():
    mock_client = MagicMock()
    mock_client.send_request.side_effect = ValueError(
        "Model too busy, unable to get response in less than 60 second(s)")

    with pytest.raises(HTTPException) as exception_info:
        await analyze_with_llm("I love broccoli", huggingface_client=mock_client, retries=2, backoff=1)

    assert exception_info.value.status_code == 503
    assert exception_info.value.detail == "Service too busy or unavailable"

@pytest.mark.asyncio
async def test_analyze_with_llm_other_error():
    mock_client = MagicMock()
    mock_client.send_request.side_effect = ValueError("Test error occurred")

    with pytest.raises(HTTPException) as excinfo:
        await analyze_with_llm("I love broccoli", huggingface_client=mock_client)

    assert excinfo.value.status_code == 500
    assert excinfo.value.detail == "Test error occurred"
