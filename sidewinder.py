# generates a square maze (size*size) with the sidewinder technique

import numpy as np
import random as rd

def carve_maze(grid:np.ndarray, size:int) -> np.ndarray:
    output_grid = np.empty([size*3, size*3],dtype=str)
    output_grid[:] = '#'
    
    i = 0
    j = 0

    while i < size:
        w = i*3 + 1
        previous_l = []
        while j < size:
            k = j*3 + 1
            toss = grid[i,j]
            output_grid[w,k] = ' '
            if toss == 0 and k+2 < size*3:
                output_grid[w,k+1] = ' '
                output_grid[w,k+2] = ' '
                previous_l.append(j)
            if toss == 1:
                # it's impossible to carve outside after preprocessing
                # look back, choose a random cell
                if grid[i,j-1] == 0:
                    # reaching from 0
                    # mandatory to be sure that previous_l has at least one element
                    # if we are coming from a list of previous cells, choose one and...
                    r = rd.choice(previous_l)
                    k = r * 3 + 1
                   
                # ...just carve north
                # this just carve north if this is the first element of the row (1 element loop)
                output_grid[w-1,k] = ' '
                output_grid[w-2,k] = ' '
                previous_l = []
            
            j += 1
            
        i += 1
        j = 0
        
    return output_grid

def preprocess_grid(grid:np.ndarray, size:int) -> np.ndarray :
    # fix first row and last column to avoid digging outside the maze external borders
    first_row = grid[0]
    first_row[first_row == 1] = 0
    grid[0] = first_row
    for i in range(1,size):
        grid[i,size-1] = 1
    return grid

def maze_to_string(output_grid: np.ndarray) -> str:
    s = ""
    for elm in output_grid:
        s+=" ".join(elm)+"\n"
    return s


def main():
    n=1
    p=0.5
    size=5

    # 1 (head) N, 0 (tail) E
    #np.random.seed(42)
    grid = np.random.binomial(n,p, size=(size,size))
    processed_grid = preprocess_grid(grid, size)
    output = carve_maze(processed_grid, size)
    output_string = maze_to_string(output)
    print(output_string)

if __name__ == '__main__':
    main()
    
