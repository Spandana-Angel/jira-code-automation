def build_prompt(task, mode="code"):
    if mode == "code":
        return f"Write Python code for: {task}. Only return code."
    elif mode == "test":
        return (
            f"Write Python unit tests for the code generated for: {task}. "
            f"Use unittest. Only output valid Python test code."
        )