#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """Return True if the object is an instance of the class or a
    subclass otherwise False"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
