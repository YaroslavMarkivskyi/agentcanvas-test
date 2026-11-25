from greeter import farewell, greet


def test_greet() -> None:
    assert greet("Ada") == "Hello, Ada!"


def test_farewell() -> None:
    assert farewell("Ada") == "Goodbye, Ada!"
