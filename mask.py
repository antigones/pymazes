# generates a masked maze (size*size) with the Aldous-Broder algorithm from a square image
# the algorithm works under the *strong* assumption that the mask is assimilable to a graph as a single connected component

import numpy as np
import random as rd
import cv2

def masked_ald(grid,size,forbidden_idx_list, allowed_idx_list):
    output_grid = np.empty([size*3, size*3],dtype=str)
    output_grid[:] = '#'
    c = size*size # number of cells to be visited
    
    # define the entrance of the maze
    i,j = allowed_idx_list[0]

    while np.count_nonzero(grid) < c:
       
        # visit this cell
        w = i*3 + 1
        k = j*3 + 1
        grid[i,j] = 1
        output_grid[w,k] = ' '

        can_go = [1,1,1,1]
        # choose a random neighbour
        neighbour_idx = rd.randrange(4) # n,e,s,w

        if i == 0 or (i-1,j) in forbidden_idx_list:
            can_go[0] = 0
        if i == size-1 or (i+1, j) in forbidden_idx_list:
            can_go[2] = 0
        if j == 0 or (i,j-1) in forbidden_idx_list:
            can_go[3] = 0
        if j == size-1 or (i,j+1) in forbidden_idx_list:
            can_go[1] = 0

        
        if neighbour_idx == 0:
            # can carve n?
            if can_go[0]:
                # has been visited?
                if grid[i-1,j] == 0:
                    # carve n
                    output_grid[w-1,k] = ' '
                    output_grid[w-2,k] = ' '
                i -= 1
                    
        
        if neighbour_idx == 1:
            if can_go[1]:
                if grid[i,j+1] == 0:
                    # goto e
                    output_grid[w,k+1] = ' '
                    output_grid[w,k+2] = ' '
                j += 1
          
        if neighbour_idx == 2:
            if can_go[2]:
                if grid[i+1,j] == 0:
                    # goto s
                    output_grid[w+1,k] = ' '
                    output_grid[w+2,k] = ' '  
                i += 1
        

        if neighbour_idx == 3:
            # goto w
            if can_go[3]:
                if grid[i,j-1] == 0:
                    output_grid[w,k-1] = ' '
                    output_grid[w,k-2] = ' '
                j -= 1
            
    return output_grid

def image_to_matrix(img_path):
    # assume the image to be shaped as a square
    img = cv2.imread(img_path, 0)
    img[img == 255] = 1

    height, width = img.shape[:2]
    return img, height, width

def fill_output(size):
    filled_grid = np.empty([size*3, size*3],dtype=str)
    filled_grid[:] = '#'
    return filled_grid

def get_forbidden_idx(grid, size):
    return [(i,j) for i in range(size) for j in range(size) if grid[i,j] == 1]

def get_allowed_idx(grid, size):
    return [(i,j) for i in range(size) for j in range(size) if grid[i,j] == 0]    
    
   
grid, h, w = image_to_matrix('dino.png')
print(grid)
forbidden_idx_list = get_forbidden_idx(grid,h)
allowed_idx_list = get_allowed_idx(grid,h)

if len(allowed_idx_list) > 0:
    console_grid = masked_ald(grid,h,forbidden_idx_list,allowed_idx_list)

    for elm in console_grid:
        print(" ".join(elm))
else:
    print("no allowed entrance for the maze")


