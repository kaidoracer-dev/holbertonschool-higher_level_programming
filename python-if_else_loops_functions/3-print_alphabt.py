#!/usr/bin/python3
letters = [
    chr(i)
    for i in range(ord('a'), ord('z') + 1)
    if chr(i) not in "qe"
]

print("{}".format("".join(letters)), end="")