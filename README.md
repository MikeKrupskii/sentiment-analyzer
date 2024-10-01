# Sentiment Analyzer

## Overview
This project provides a simple API for sentiment analysis. It uses a [Hugging Face model](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment) to classify the sentiment of text inputs as one of the following:
- Very Negative
- Negative
- Neutral
- Positive
- Very Positive

The sentiment analyzer can be run using either pip or Docker.

---

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

## Running the project

### 1. Using Docker
1. Build and run the Docker container:
```bash
docker compose up --build
```
2. Access the API via the following endpoint:
```bash
localhost:8000/analyze-sentiment/
```

### 2. Using Venv and Pip
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
http://127.0.0.1:8000/analyze-sentiment/
```

## Using the API
### Using tools like Postman/Insomnia
1. Set **Content-Type** header to **application/json**
2. URL: **localhost:8000/analyze-sentiment/**
3. Body example (JSON):
```bash
{
  "text": "I love broccoli!"
}
```
4. Example response:
```bash
{
  "sentiment": "Very Positive"
}
```

### Using curl directly in the Terminal
```bash
curl -X POST "localhost:8000/analyze-sentiment/"
 -H "Content-Type: application/json" -d '{"text": "I tolerate broccoli."}'
```

## Example Inputs and Expected Outputs
### 1. Very Negative:
- Input: "I hate broccoli."
- Expected Sentiment: "Very Negative"
### 2. Negative:
- Input: "I tolerate broccoli."
- Expected Sentiment: "Negative"
### 3. Neutral:
- Input: "Broccoli is on the menu."
- Expected Sentiment: "Neutral"
### 4. Positive:
- Input: "I like broccoli."
- Expected Sentiment: "Positive"
### 5. Very Positive:
- Input: "I love broccoli."
- Expected Sentiment: "Very Positive"

## Running Tests
Run tests using pytest command:
```bash
pytest
```