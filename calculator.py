import math

def sqrt(x: float) -> float:
    if x < 0:
        raise ValueError("sqrt: input must be >= 0")
    return math.sqrt(x)

def factorial(x: int) -> int:
    x = int(x)
    if x < 0:
        raise ValueError("factorial: input must be non-negative integer")
    return math.factorial(x)

def ln(x: float) -> float:
    if x <= 0:
        raise ValueError("ln: input must be > 0")
    return math.log(x)

def power(x: float, b: float) -> float:
    return x ** b
