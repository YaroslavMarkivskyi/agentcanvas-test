def greet(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"


def goodbye(name: str) -> str:
    """Say goodbye to someone by name."""
    if name:
        return f"Goodbye, {name}!"
    return "Goodbye!"
