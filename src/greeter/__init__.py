def greet(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"


def whisper(name: str) -> str:
    """Whisper a greeting."""
    if name:
        return f"hello, {name.lower()}..."
    return "hello..."
