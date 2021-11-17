""" content of calculator.py """
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division


class Calculator:
    """Calculator class"""

    @staticmethod
    def add_number(value1, value2):
        """Add as many times to the first number"""
        addition = Addition.create(value1, value2)
        return addition.get_result()

    @staticmethod
    def subtract_number(value1, value2):
        """Subtract as many times to the first number"""
        subtraction = Subtraction.create(value1, value2)
        return subtraction.get_result()

    @staticmethod
    def multiply_number(value, values: tuple):
        """Multiply as many times to the first number"""
        multiplication = Multiplication.create(value, values)
        return multiplication.get_result()

    @staticmethod
    def divide_number(value, values: tuple):
        """Divide as many times to the first number"""
        division = Division.create(value, values)
        return division.get_result()
