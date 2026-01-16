#!/usr/bin/env python3
def islower(c):
    code = ord(c)
    a = 97
    z = 122
    if ord(c) >= a and ord(c) <= z:
        return True
    else:
        return False
