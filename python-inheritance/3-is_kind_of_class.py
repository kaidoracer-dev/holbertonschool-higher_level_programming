#!/usr/bin/python3
"""Define is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Return True if the object is an instance of the class or a
    subclass otherwise False"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
