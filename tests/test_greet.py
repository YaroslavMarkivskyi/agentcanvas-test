from greeter import greet, shout


def test_greet() -> None:
    assert greet("Ada") == "Hello, Ada!"


def test_shout() -> None:
    assert shout("Ada") == "HELLO, ADA!"


def test_shout_to_nobody() -> None:
    assert shout("") == "HELLO!"
