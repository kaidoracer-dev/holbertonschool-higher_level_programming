#!/usr/bin/python3
"""Define class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """Define Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
