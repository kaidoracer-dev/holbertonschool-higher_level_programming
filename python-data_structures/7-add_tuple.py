#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 0:
        a = tuple_a[0]
    else:
        a = 0
    if len(tuple_a) > 1:
        a1 = tuple_a[1]
    else:
        a1 = 0
    if len(tuple_b) > 0:
        b = tuple_b[0]
    else:
        b = 0
    if len(tuple_b) > 1:
        b2 = tuple_b[1]
    else:
        b2 = 0
    a + b
    a1 + b2

    return (a + b, a1 + b2)
