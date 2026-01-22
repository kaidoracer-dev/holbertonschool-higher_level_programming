#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    see = []
    for i in my_list:
        if i not in see:
            total += i
            see.append(i)
    return (total)
