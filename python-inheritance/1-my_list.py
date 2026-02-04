#!/usr/bin/python3
"""Create class MyList"""


class MyList(list):

    def print_sorted(self):
        """that prints the list, but sorted ascending sort"""
        listcopy = sorted(self)
        print(listcopy)
