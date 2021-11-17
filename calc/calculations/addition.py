""" This is the addition calculation """
# It inherits the value A and value B from the calculation class """
from calc.calculations.calculation import Calculation


# This is how you extend the Addition class with Calculation
class Addition(Calculation):
    """The Addition class """
    # This class has a get method that calculates the result of addition.

    def get_result(self):
        """Get result of addition"""
        # Arrange and Act
        result = self.value_a + self.value_b
        # Assert
        return result
