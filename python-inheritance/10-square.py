#!/usr/bin/python3
"""Define class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define Square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
