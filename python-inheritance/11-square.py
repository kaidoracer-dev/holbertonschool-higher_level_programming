#!/usr/bin/python3
"""import the file 9-rectangle.py"""
Rectangle = __import__('9-rectangle').Rectangle
"""Create a class"""


class Square(Rectangle):
    def __init__(self, size):
        """Define Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the following square description"""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
