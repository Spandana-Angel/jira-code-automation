import os
from groq import Groq

def call_groq(prompt: str) -> str:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "You are a code generation assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content (groq)