#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

    number = len(argv) - 1

    if number == 0:
        print("0 arguments.")

    if number == 1:
        print("1 argument:")

    if number > 1:
        print(f"{number} arguments:")

    if number > 0:
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
