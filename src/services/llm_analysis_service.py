from src.clients.huggingface_client import get_huggingface_client

async def analyze_with_llm(text: str, huggingface_client=None):
    if huggingface_client is None:
        huggingface_client = get_huggingface_client(llm=True)

    system_prompt = (
        "You are an expert assistant in sentiment analysis. "
        "You will analyze the emotional tone of the user's input and classify it returning a single sentiment label."
    )
    user_prompt = f"User Input: {text}\n"
    assistant_prompt = "Assistant:"
    full_prompt = f"{system_prompt}\n{user_prompt}{assistant_prompt}"

    result = huggingface_client.send_request(full_prompt)
    response = result[0]['generated_text'].strip()

    if assistant_prompt in response:
        sentiment = response.split(assistant_prompt)[-1].strip()
    else:
        sentiment = "Unknown"

    return sentiment
