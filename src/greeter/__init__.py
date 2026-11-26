def greet(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"


def whisper(name: str) -> str:
    """Return a quiet greeting in lowercase."""
    if name:
        return f"hello, {name.lower()}..."
    return "hello..."
