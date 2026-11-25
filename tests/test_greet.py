from greeter import greet, shout


def test_greet() -> None:
    assert greet("Ada") == "Hello, Ada!"


def test_shout() -> None:
    assert shout("ada") == "HELLO, ADA!"
