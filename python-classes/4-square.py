#!/usr/bin/python3
"""Define a class"""

class Square:
    def __init__(self, size=0):
        """Get the size"""
        self.size = size
    @property
    def size(self):
        """Get the size"""
        return self.__size
    @size.setter
    def size(self, value):
        """Set the size with checks"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """Return the area"""
        return self.__size * self.__size
