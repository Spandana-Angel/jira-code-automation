from groq_client import call_groq
from prompt_builder import build_test_prompt

def generate_tests(user_request: str) -> str:
    prompt = build_test_prompt(user_request)
    return call_groq(prompt)                             //test gen