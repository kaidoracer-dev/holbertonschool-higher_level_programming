#!/usr/bin/python3
"""Define class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define Square"""
    def __init__(self, size):
        """Initialize Square with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Return string representation"""
        return "[Square] {}/{}".format(self.__size, self.__size)
