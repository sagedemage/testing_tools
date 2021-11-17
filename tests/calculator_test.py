"""Import the calculator class"""
from calc.calculator import Calculator


def test_calculator_add():
    """Testing addition method"""
    # Adding two numbers
    assert Calculator.add_number(2, 3) == 5


def test_calculator_subtract():
    """Testing subtraction method"""
    # Subtracting two numbers
    assert Calculator.subtract_number(10, 5) == 5


def test_calculator_multiply():
    """Testing the multiplication method"""
    # Multiplying two numbers
    assert Calculator.multiply_number(3, 2) == 6


def test_calculator_divide():
    """Testing division method"""
    # Dividing two numbers
    assert Calculator.divide_number(4, 2) == 2


def test_calculator_divide_by_zero():
    """Testing division by zero"""
    # pylint: disable=unused-argument, redefined-outer-name
    # Dividing two numbers
    assert Calculator.divide_number(2, 0) is None
