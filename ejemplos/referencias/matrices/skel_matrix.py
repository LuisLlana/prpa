#!/usr/bin/python
# -*- coding: utf-8 -*-
# $Id: mat3.py,v 1.3 2012-02-14 14:01:43 luis Exp $

"""
Functions with some usual operation for real number matrices.
"""
from math import fabs, sqrt
def create_matrix(rows, cols):
    """Cretates a new matrix of zeros of size n x m

    @type rows: integer
    @type cols: integer
    @rtype: list of list of numbers
    @return: a matrix of size n x m containing zeros
    """
    matrix = [None]*rows
    i = 0
    while i < rows:
        matrix[i] = [0] * cols
        i = i+1
    return matrix

def copy(matrix):
    """Creates a copy of matriz a

    @type matrix: list of lists of numbers
    @param matrix: Non empty matrix of numbers
    @rtype: list of lists of numbers
    @return: a copy of matrix a
    """
    rows = len(matrix)
    cols = len(matrix[0])
    new = create_matrix(rows, cols)
    i = 0
    while i < rows:
        j = 0
        while j < cols:
            new[i][j] = matrix[i][j]
            j = j+1
        i = i+1
    return new

def repr_matrix(matrix):
    """
    Procedure to print a real number matrix
    @type matrix: list of lists of numbers
    """
    s = ''
    for row in matrix:
        for cell in row:
            s += "{0:.2f}".format(cell)
        s += '\n'

def transpose(matrix):
    """Function that transpose a funcion. This function does not
    return a new matrix but it modifies the original
    matrix.

    @type matrix: list of list of numbers
    @param matrix: non empy matrix
    """

def transpose_new(matrix):
    """Function that transpose a funcion. This function
    returns a new matrix. It does not modify the original on

    @type matrix: list of list of numbers
0    @param matrix: non empy matrix
    @rtype: list of list of numbers
    @return: a matrix containing the orifinal one.
    """


def mult(mat1, mat2):
    """Function that computes the product of matrices a and b

    @type a: list of lists of numbers
    @param a: non empty matrix of numbers of size n x p
    @type b: list of lists of numbers
    @param b: non empty matrix of numbers of size p x m
    @rtype: list of lists of numbers
    @return: a matrix of size m x n
    """

def add(mat1, mat2):
    """Function that computes the sum of matrices a and b

    @type a: list of lists of numbers
    @param a: non empty matrix of numbers of size n x m
    @type b: list of lists of numbers
    @param b: non empty matrix of numbers of size n x m
    @rtype: list of lists of numbers
    @return: a matrix of size n x m
    """


EPSILON = 1E-6
def are_equals_small(x, y):
    """
    Funtion to check the equality of real numbers if they are "small nunmbers"
    @type x: float
    @type y: float
    @rtype: boolean
    """
    return fabs(x-y) < EPSILON

def are_equals(x, y):
    """
    Function to check if two real numbers are equal
    @type x: float
    @type y: float
    @rtype: float
    """
    distance = sqrt(x**2+y**2)
    if distance < 1:
        return are_equals_small(x, y)
    else:
        return abs(x-y) < distance*EPSILON

def is_symmetric(matrix):
    """Computes wheather a is symmetric or not
    @type matrix: list of list of numbers
    @param matrix: non empty matrix of size n x n (square matrix)
    @rtype: boolean
    @return: returns true iff the matrix is symmetric
    """


def change_rows(matrix, col, row):
    """
    Transform m as follows. Change the rows 'col' and 'row' and change
    the sing of all elements in the final row 'col'. Note that this
    transformation preserves the determinant.
    @type matrix: list of list of numbers
    @param matrix: non empty matrix of size n x n (square matrix)
    @type col: int
    @param col: 0<=col<len(matrix)
    @type row: int
    @param row: 0<=row<len(matrix)
    """

def find_pivot(matrix, col):
    """
    This functions finds and element i such that m[i][col]!=0 with i>col.
    If such element does not exist, this function returns len(m).
    @type matrix: list of list of numbers
    @param matrix: non empty matrix of size n x n (square matrix)
    @type col: int
    @param col: 0<=col<len(matrix)
    @rtype: int
    """

def pivot(matrix, col):
    """
    Transform m as follows. The determinat of the final matrix
    is the same as the determinat of the transformed.
    After the transformation we have m[col][j]==0 for j>col

    @type matrix: list of list of numbers
    @param matrix: non empty matrix of size n x n (square matrix)
    @type col: int
    @param col: 0<=col<len(matrix)
    """

def determinant(matrix):
    """
    computes the determinat of a square matrix matrix:
    @type matrix: list of list of numbers
    @param matrix: non empty matrix of size n x n (square matrix)
    @rtype: number
    """
    # with this procedure the matrix will change.
    # since we do not want to change the original matrix
    # we need to operate over a copy.
    aux = copy(matrix)
    #.........

def main1():
    """
    Prueba 1
    """
    mat1 = [ [1, 2], [3, 4], [5, 6] ]
    print "c1-mat1:", mat1
    mat2 = transpose(mat1)
    print "c2-ma2", mat2

    mat3 = times(mat1, mat2)
    print "c3-mat3:", mat3
    print "c4:es simétrica mat3:", is_symmetric(mat3)
    aux = mat3[1][0]
    mat4 = mat3
    mat4[1][0] = 0
    print "c5:es simétrica mat3:", is_symmetric(mat3)
    print "c6:es simétrica mat4:", is_symmetric(mat4)
    mat3[1][0] = aux
    mat4 = copy(mat3)
    mat4[1][0] = 0
    print "c7:es simétrica mat3:", is_symmetric(mat3)
    print "c8:es simétrica mat4:", is_symmetric(mat4)

def main2():
    """
    Prueba 2
    """
    mat = [ [1, 2, 3], [6, 7, 8], [1, 1, 5] ]
    m_copy = copy(mat)
    print(repr_matrix(mat))
    print "-----------"
    pivot(mat, 0)
    print_matrix(mat)
    print "-----------"
    pivot(mat, 1)
    print(repr_matrix(mat))
    print "-----------"
    print determinant(m_copy)
    print(repr_matrix(m_copy))
