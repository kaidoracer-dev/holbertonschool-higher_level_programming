#!/usr/bin/python3
"""Define class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """Define Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the following square description"""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
