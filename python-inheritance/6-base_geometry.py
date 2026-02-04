#!/usr/bin/python3
"""Create class"""


class BaseGeometry:
    """that raises an Exception with the message area() is not implemented"""
    def area(self):
        raise Exception("area() is not implemented")
