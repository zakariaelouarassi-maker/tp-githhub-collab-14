from src.calculator import add, subtract, puissance

def test_add(): 
    assert add(2, 3) == 5 

def test_subtract():
    assert subtract(5, 2) == 3

def test_puissance():
    assert puissance(2, 3) == 8
    assert puissance(5, 0) == 1
    assert puissance(2, -1) == 0.5 