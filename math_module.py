"""Простий математичний модуль для демонстрації юніт-тестування."""


def factorial(n: int) -> int:
    """Повертає n! для цілого n >= 0."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n має бути цілим числом")
    if n < 0:
        raise ValueError("факторіал від'ємного числа не визначений")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_even(n: int) -> bool:
    """Повертає True, якщо число парне."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n має бути цілим числом")
    return n % 2 == 0
