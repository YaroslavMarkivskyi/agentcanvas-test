from greeter import greet, whisper


def test_greet() -> None:
    assert greet("Ada") == "Hello, Ada!"


def test_whisper() -> None:
    assert whisper("Ada") == "hello, ada..."


def test_whisper_to_nobody() -> None:
    assert whisper("") == "hello..."
