import openai
import os

def generate_response(prompt: str) -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a CIC-aware assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
