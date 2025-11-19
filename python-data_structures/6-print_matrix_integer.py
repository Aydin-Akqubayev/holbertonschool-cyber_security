#!/usr/bin/python3
def print_matrix_integer(matrix=""):
    result = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result += "{:d} ".format(matrix[i][j])
        result = result[:-1] + '\n'

    print(result[:-1])
