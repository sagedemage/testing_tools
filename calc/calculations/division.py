""" This is the division calculation """
# It inherits the value A and value B from the calculation class """
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """The Division class """
    # This class has a get method that calculates the result of division.

    def get_result(self):
        """Get result of division"""
        try:
            result = self.value_a / self.value_b
        except ZeroDivisionError:
            result = None
        return result
