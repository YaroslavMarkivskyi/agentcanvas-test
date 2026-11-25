from greeter import goodbye, greet


def test_greet() -> None:
    assert greet("Ada") == "Hello, Ada!"


def test_goodbye() -> None:
    assert goodbye("Ada") == "Goodbye, Ada!"


def test_goodbye_without_name() -> None:
    assert goodbye("") == "Goodbye!"
