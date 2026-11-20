import pytest
from math_module import factorial, is_even


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1


@pytest.mark.parametrize("n, expected", [(2, 2), (3, 6), (4, 24), (10, 3628800)])
def test_factorial_parametrized(n, expected):
    assert factorial(n) == expected


def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)


def test_factorial_wrong_type_raises():
    with pytest.raises(TypeError):
        factorial(2.5)


@pytest.mark.parametrize("n, expected", [(0, True), (1, False), (2, True), (-3, False), (-4, True), (1001, False)])
def test_is_even(n, expected):
    assert is_even(n) is expected


def test_is_even_wrong_type_raises():
    with pytest.raises(TypeError):
        is_even("4")
