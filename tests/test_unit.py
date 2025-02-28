import pytest


@pytest.mark.parametrize("x, y, expected", [(1, 2, 3)])
def test_addition(x, y, expected):
    assert x + y == expected
