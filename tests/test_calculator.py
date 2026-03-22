import pytest
from src.calculator import divide
from src.calculator import add, subtract, power

def test_add(): 
    assert add(2, 3) == 5 

def test_subtract():
    assert subtract(5, 2) == 3

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5
# Cas limite
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)
def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -1) == 0.5 