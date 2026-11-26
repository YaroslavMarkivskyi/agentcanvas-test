def greet(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"


def shout(name: str) -> str:
    """Shout a greeting."""
    if name:
        return f"HELLO, {name.upper()}!"
    return "HELLO!"
