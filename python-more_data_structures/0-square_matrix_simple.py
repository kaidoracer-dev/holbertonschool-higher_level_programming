#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_line = []
        for x in i:
            new_line.append(x * x)
        new_matrix.append(new_line)

    return (new_matrix)
