from pathlib import Path


def test_readme_ends_with_license_line() -> None:
    readme = Path("README.md").read_text(encoding="utf-8").splitlines()
    assert readme[-1] == "Licensed under the MIT License."
