#!/usr/bin/python

def create(rows,cols):
    """
    This function creates a (rows x cols)-matrix. 
    """
    i=0
    matrix = []
    while i<rows:
        matrix.append([0] * cols)
        i+=1
    return matrix
    
    
def print_matrix(matrix):
    for row in matrix:
        for cell in row:
            print "{0:.2f}".format(cell) ,
        print
        
def fill(m):
    elem = 0
    i = 0
    rows = len(m)
    cols = len(m[0])
    while i<rows:
        j=0
        while j<cols:
            m[i][j]=elem
            elem+=1
            j+=1
        i+=1
    
def main():
    m = create(5,6)
    fill(m)
    print_matrix(m)
    
            
main()            
