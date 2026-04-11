def build_code_prompt(user_request: str) -> str:
    return f"""
You are a backend developer.
Generate clean working code for this requirement:

{user_request}

Return only code. No explanation.
"""

def build_test_prompt(user_request: str) -> str:
    return f"""
Generate test cases for this requirement:

{user_request}

Return only test code. No explanation.
"""