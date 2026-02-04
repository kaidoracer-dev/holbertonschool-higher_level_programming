#!/usr/bin/python3
"""Define class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Constructor with witdh and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return area"""
        return self.__width * self.__height

    def __str__(self):
        """Return the following rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
