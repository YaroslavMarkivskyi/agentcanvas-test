from greeter import greet, shout, whisper


def test_greet() -> None:
    assert greet("Ada") == "Hello, Ada!"


def test_whisper() -> None:
    assert whisper("Ada") == "hello, Ada."


def test_shout() -> None:
    assert shout("Ada") == "HELLO, ADA!"


def test_shout_to_nobody() -> None:
    assert shout("") == "HELLO!"
