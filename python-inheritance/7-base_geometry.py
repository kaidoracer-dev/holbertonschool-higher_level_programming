#!/usr/bin/python3
"""Create class"""


class BaseGeometry:
    """that raises an Exception with the message area() is not implemented"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """return typeError if the walue in not an int and
        ValueError if value is less or equal to 0 """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
