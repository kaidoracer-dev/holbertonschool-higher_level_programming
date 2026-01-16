#!/usr/bin/python3
letters = ""
for i in range(ord('a'), ord('z') + 1):
    if chr(i) not in "qe":
        letters += chr(i)

print(letters, end="")
