# generates a square maze (size*size) with the Wilson algorithm

import numpy as np
import random as rd

size=10

#np.random.seed(42)
grid = np.zeros(shape=(size,size))

def wilson(grid,size):
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
            # choose a random neighbour
            neighbour_idx = rd.randrange(4) # n,e,s,w

            if i == 0:
                can_go[0] = 0
            if i == size-1:
                can_go[2] = 0
            if j == 0:
                can_go[3] = 0
            if j == size-1:
                can_go[1] = 0

            if neighbour_idx == 0:
                # can carve n?
                if can_go[0]:
                    # has been visited?
                    # going there from s
                    visited_from.append(1)
                   
                    i = i - 1
                        
            
            if neighbour_idx == 1:
                if can_go[1]:
                    visited_from.append(2)
                    
                    j = j + 1
            
            if neighbour_idx == 2:
                if can_go[2]:
                    visited_from.append(3)
                   
                    i = i + 1
            

            if neighbour_idx == 3:
                # goto w
                if can_go[3]:
                    visited_from.append(4)
                   
                    j = j - 1
            
    return output_grid

console_grid = wilson(grid,size)

for elm in console_grid:
    print(" ".join(elm))


