# generates a square maze (size*size) with Wilson's algorithm

import numpy as np
import random as rd

def wilson(grid:np.ndarray, size:int) -> np.ndarray:
    output_grid = np.empty([size*3, size*3],dtype=str)
    output_grid[:] = '#'
    c = size*size # number of cells to be visited

    # choose random cell
    i = rd.randrange(size)
    j = rd.randrange(size)
    grid[i,j] = 1

    visited = [[i,j]]
    visited_from = [0]

    while np.count_nonzero(grid) < c:
        
        if grid[i,j] == 1:
            #print('closing loop...')
            #print(visited)
            
            # already visited, close the loop (carve + empty visited)
            for i in range(len(visited)):
                ve = visited[i]
                vi = ve[0]
                vj = ve[1]
                #print('actually visiting '+str(vi)+" "+str(vj))
                #print('visited from: '+ str(visited_from[i]))
                grid[vi,vj] = 1
                w = vi*3 + 1
                k = vj*3 + 1
                output_grid[w,k] = ' '

                vf = visited_from[i]

                if vf == 1:
                    output_grid[w-1,k] = ' '
                    output_grid[w-2,k] = ' '
                if vf == 2:
                    output_grid[w,k+1] = ' '
                    output_grid[w,k+2] = ' '
                if vf == 3:
                    output_grid[w+1,k] = ' '
                    output_grid[w+2,k] = ' '
                if vf == 4:
                    output_grid[w,k-1] = ' '
                    output_grid[w,k-2] = ' '       

            visited.clear()
            visited_from.clear()
            i = rd.randrange(size)
            j = rd.randrange(size)
            #print('randomly jumped '+str(i)+","+str(j))
            visited.append([i,j])
            visited_from.append(0)
            # we just random-jumped there
            
        else:
            if [i,j] in visited:
                #print(str(i)+","+str(j)+' - erasing loop...')
                #print(visited)
                # erase the loops
                visited.clear()
                visited_from.clear()
         
            # visit a random cell
        
            visited.append([i,j])
            
            #print(grid)

            can_go = [1,1,1,1]

            if i == 0:
                can_go[0] = 0
            if i == size-1:
                can_go[2] = 0
            if j == 0:
                can_go[3] = 0
            if j == size-1:
                can_go[1] = 0
            
            neighbour_idx = np.random.choice(np.nonzero(can_go)[0]) # n,e,s,w

            if neighbour_idx == 0:
                # going there from s
                visited_from.append(1)
                i -= 1
                        
            if neighbour_idx == 1:
                visited_from.append(2)
                j += 1
            
            if neighbour_idx == 2:
                visited_from.append(3)
                i += 1
            
            if neighbour_idx == 3:
                visited_from.append(4) 
                j -= 1
            
    return output_grid

size=5

#np.random.seed(42)
grid = np.zeros(shape=(size,size))

console_grid = wilson(grid,size)

for elm in console_grid:
    print(" ".join(elm))


