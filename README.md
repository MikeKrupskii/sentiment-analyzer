# Sentiment Analyzer

## Overview
This project provides a simple API for sentiment analysis.
It uses two different models to analyze the input text.

### bert-base-multilingual-uncased-sentiment [model](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment)
This Model is designed specifically for sentiment analysis   and returns one of the 5 following labels:
- Very Negative
- Negative
- Neutral
- Positive
- Very Positive

To use this model, add an optional parameter **model_type=sentiment_analysis** to your query

### gemma-2-27b-it [model](https://huggingface.co/google/gemma-2-27b-it)
This is a general chat completion LLM Model from Google that returns a sentiment analysis based on specific system and user prompts.


## Setup

### Prerequisites
Before starting, ensure you have the following:
- Python 3.9 or higher installed (if using the non-Docker method)
- Docker and Docker Compose installed (if using Docker)
- Hugging Face API key (will be sent via email)
- Free port **8000**

### 1. Clone the repository

```bash
git clone https://github.com/MikeKrupskii/sentiment-analyzer.git
cd sentiment-analyzer
```
### 2. Copy .env.template to .env
```bash
cp .env.template .env
```

### 3. Add the Hugging Face API Key to the .env
```bash
HUGGINGFACE_API_KEY=put_your_key_here
```

## Running the project - two options

### Option 1: Docker
1. Build and run the Docker container:
```bash
docker compose up --build
```
2. Access the API via the following endpoint:
```bash
localhost:8000/analyze-text/
```

### Option 2: Using Venv and Pip
1. Set up a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the FastAPI server:
```bash
uvicorn main:app --reload
```
4. Access the API via the following endpoint:
```bash
http://127.0.0.1:8000/analyze-text/
```

## Using the API
### Using tools like Postman/Insomnia
1. Set **Content-Type** header to **application/json**
2. Endpoint: **localhost:8000/analyze-text/**
3. Optional parameter: **localhost:8000/analyze-text?model_type=sentiment_analysis** OR **model_type=llm**(set by default if no parameter is specified)
4. Body example (JSON):
```bash
{
  "text": "I love broccoli!"
}
```
4. Example response:
```bash
{
  "sentiment": "Positive"
}
```

### Using curl directly in the Terminal
```bash
curl -X POST "localhost:8000/analyze-text/"
 -H "Content-Type: application/json" -d '{"text": "I tolerate broccoli."}'
```

## Example Inputs and Expected Outputs
### 1. "I hate broccoli"
- Expected result from LLM model: "Hate"
- Expected result from sentiment analysis model: "Very Negative"
### 2. "I tolerate broccoli"
- Expected result from LLM model: "Neutral"
- Expected result from sentiment analysis model: "Negative"
### 3. "Broccoli is on the menu"
- Expected result from LLM model: "Neutral"
- Expected result from sentiment analysis model: "Neutral"
### 4. "I like broccoli"
- Expected result from LLM model: "Positive"
- Expected result from sentiment analysis model: "Positive"
### 5. "I love broccoli"
- Expected result from LLM model: "Positive"
- Expected result from sentiment analysis model: "Very Positive"

## Running Tests
Run tests using pytest command:
```bash
pytest
```
