from generator.prompt_builder import build_prompt
from generator.code_generator import generate_code
from generator.pr_formatter import format_pr

def main():
    task = input("Enter task: ")

    prompt = build_prompt(task)
    code = generate_code(prompt)
    output = format_pr(task, code)

    print("\n--- Generated PR ---\n")
    print(output)

if __name__ == "__main__":
    main()