import math
import pytest
from calculator import sqrt, factorial, ln, power

def test_sqrt():
    assert sqrt(9) == 3
    with pytest.raises(ValueError):
        sqrt(-1)

def test_factorial():
    assert factorial(6) == 720
    with pytest.raises(ValueError):
        factorial(-1)

def test_ln():
    assert pytest.approx(ln(math.e), rel=1e-9) == 1.0
    with pytest.raises(ValueError):
        ln(0)

def test_power():
    assert power(2, 3) == 8
    assert power(9, 0.5) == 3
