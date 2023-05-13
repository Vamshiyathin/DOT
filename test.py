from calculator import Calculator

def test_addition():
    calculator = Calculator()
    assert calculator.add(2, 3) == 4
    
def test_subtraction():
    calculator = Calculator()
    assert calculator.subtract(5, 3) == 4
    
def test_multiplication():
    calculator = Calculator()
    assert calculator.multiply(2, 3) == 6
    
def test_division():
    calculator = Calculator()
    assert calculator.divide(6, 3) == 2
    
def test_divide_by_zero():
    calculator = Calculator()
    try:
        calculator.divide(6, 0)
    except ValueError as e:
        assert str(e) == 'Cannot divide by zero'
