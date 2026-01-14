#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("%d is positive" % random.randint(-10, 10))
if number == 0: 
    print("%d is zero" % random.randint(-10, 10))
if number < 0:
    print("%d is negative" % random.randint(-10, 10))