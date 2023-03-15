#!/usr/bin/python3
# Nice22
def square_matrix_map(matrix=[]):
    return (list(map(lambda r: list(map(lambda x: x**2, r)), matrix)))
