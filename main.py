def send_hello(name: str | None):
    if not name:
        raise ValueError("The name cannot be empty.")

    return f"Hello {name}"


print(send_hello())
