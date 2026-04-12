from groq_client import call_groq
from prompt_builder import build_code_prompt

def generate_code(user_request: str) -> str:
    prompt = build_code_prompt(user_request)
    return call_groq(prompt)