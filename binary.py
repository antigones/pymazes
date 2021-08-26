# generates a square maze (size*size) with the binary tree technique

import numpy as np


def toConsole(grid):
    output_grid = np.empty([size*3, size*3],dtype=str)
    output_grid[:] = '#'
    result = [(i, j) for i in range(size) for j in range(size)]
    print(result)
    i = 0
    j = 0
    while i < size:
        w = i*3 + 1
        while j < size:
            k = j*3 + 1
            toss = grid[i,j]
            output_grid[w,k] = ' '
            if toss == 0 and k+2 < size*3:
                output_grid[w,k+1] = ' '
                output_grid[w,k+2] = ' '
            if toss == 1 and w-2 >=0:
                output_grid[w-1,k] = ' '
                output_grid[w-2,k] = ' '
            
            j = j + 1
            
        i = i + 1
        j = 0
        
    for elm in output_grid:
        print(" ".join(elm))


n=1
p=0.5
size=5

# 1 (head) N, 0 (tail) E
np.random.seed(42)
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


