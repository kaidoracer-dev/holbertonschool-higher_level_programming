#!/usr/bin/python3
"""Create class MyList"""


class MyList(list):
    """Define print_sorted """
    def print_sorted(self):
        """that prints the list, but sorted ascending sort"""
        print(sorted(self))
