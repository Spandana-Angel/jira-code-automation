from generator import generate_code
from test_generator import generate_tests

def main():
    user_request = "Add a login API with email and password using FastAPI"

    print("Generating code...")
    code = generate_code(user_request)
    print(code)

    print("\nGenerating tests...")
    tests = generate_tests(user_request)
    print(tests)

if __name__ == "__main__":
    main()                                    