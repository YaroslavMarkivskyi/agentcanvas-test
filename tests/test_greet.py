from greeter import cheer, cheer_twice, greet, shout, whisper_twice


def test_greet() -> None:
    assert greet("Ada") == "Hello, Ada!"


def test_cheer() -> None:
    assert cheer("Ada") == "Hooray, Ada!"


def test_cheer_to_nobody() -> None:
    assert cheer("") == "Hooray!"


def test_cheer_twice() -> None:
    assert cheer_twice("Ada") == "Hooray, Ada! Hooray, Ada!"


def test_shout() -> None:
    assert shout("ada") == "HELLO, ADA!"


def test_whisper_twice() -> None:
    assert whisper_twice("Ada") == "hello, ada... hello, ada..."


def test_whisper_twice_to_nobody() -> None:
    assert whisper_twice("") == "hello... hello..."
