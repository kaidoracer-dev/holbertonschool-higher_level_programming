#!/usr/bin/python3
"""Define class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define Square"""
    def __init__(self, size):
        """Define Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Return area of the square"""
        return self.size * self.size

    def __str__(self):
        return "[square] {}/{}".format(self.__size, self.__size)
