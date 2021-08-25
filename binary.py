# generates a square maze (size*size) with the binary tree technique

import numpy as np

def convertToN(x):
    if x[:-1] == 0:
        return 1

def toConsole(grid):
    output_grid = np.empty([size*3, size*3],dtype=str)
    output_grid[:] = '#'

    i = 1
    j = 1
    while i < (size*3):
        while j < (size*3):
            toss = grid[i//3,j//3]
            output_grid[i,j] = ' '
            if toss == 0 and j+2 < size*3:
                output_grid[i,j+1] = ' '
                output_grid[i,j+2] = ' '
            if toss == 1 and i-2 >=0:
                output_grid[i-1,j] = ' '
                output_grid[i-2,j] = ' '
            
            j = j + 3
            
        i = i + 3
        j = 1
        
    for elm in output_grid:
        print(" ".join(elm))


n=1
p=0.5
size=5

# 1 (head) N, 0 (tail) E
#np.random.seed(42)
grid = np.random.binomial(n,p, size=(size,size))

# fix first row and last column to avoid digging outside the maze external borders
first_row = grid[0]
first_row[first_row == 1] = 0
grid[0] = first_row
for i in range(1,size):
    grid[i,size-1] = 1
print('grid')
print(grid)

toConsole(grid)


