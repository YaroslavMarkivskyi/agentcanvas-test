def greet(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"


def whisper(name: str) -> str:
    """Greet someone quietly."""
    if name:
        return f"hello, {name.lower()}..."
    return "hello..."


def whisper_twice(name: str) -> str:
    """Greet someone quietly twice."""
    greeting = whisper(name)
    return f"{greeting} {greeting}"


def shout(name: str) -> str:
    """Greet someone loudly."""
    return f"HELLO, {name.upper()}!"


def cheer(name: str) -> str:
    """Cheer someone on."""
    if name:
        return f"Hooray, {name}!"
    return "Hooray!"


def cheer_twice(name: str) -> str:
    """Cheer someone on twice."""
    greeting = cheer(name)
    return f"{greeting} {greeting}"
