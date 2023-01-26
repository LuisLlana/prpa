#!/usr/bin/python

def create(rows,cols):
    """
    Attempt to create a (rows x cols)-matrix. This attempt is
    incorrect because of memory  sharing.
    """
    return ([[0] * cols]) * rows
    
    
def print_matrix(matrix):
    for row in matrix:
        for cell in row:
            print cell ,
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
            
            
