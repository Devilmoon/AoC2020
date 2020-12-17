import numpy as np
from copy import deepcopy

matrix = [[[0 for k in range(8)] for j in range(8)] for i in range(8)]
matrix4d = [[[[0 for k in range(8)] for j in range(8)] for i in range(8)] for w in range(8)]
with open('input.txt') as f:
    for i,line in enumerate(f):
        matrix[1][i] = ([0 if _=='.' else 1 for _ in line.strip()])
        matrix4d[1][1][i] = ([0 if _=='.' else 1 for _ in line.strip()])

matrix = np.array(matrix)

#function to check the number of active neighbors
def active_n(m, p, pad):
    #use a padded matrix so that we should always hit a 
    #known position
    n_m = np.pad(m, pad_width=([1,1], [1,1], [1,1]), mode='constant')
    actives = 0
    #The neighbors are all the adjacent in the same dimension
    #and all the adjacent + upper/lower neighbor in the other two
    for d in [-1,0,1]:
        for r in [-1,0,1]:
            for c in [-1,0,1]:
                if (p[0]+d+1, p[1]+r+1, p[2]+c+1) == (p[0]+1, p[1]+1, p[2]+1):
                    continue
                try:
                    if n_m[(p[0]+d)+1][(p[1]+r)+1][(p[2]+c)+1] == 1:
                        actives+=1
                except IndexError:
                    pass
    return actives

for cycle in range(6):
    mid = 1+cycle
    if cycle>0:
        new_matrix = np.pad(matrix, pad_width=([1,1], [1,1], [1,1]), mode='constant')
        shift_d=1
    else:
        #the matrix is already 3D
        new_matrix = np.pad(matrix, pad_width=([0,0], [1,1], [1,1]), mode='constant')
        shift_d=0
    for d in range(mid, new_matrix.shape[0]):
        for r in range(new_matrix.shape[1]):
            for c in range(new_matrix.shape[2]):
                pos = (d,r,c)
                #If looking at the previous matrix, the positions are shifted by one
                #since we pad each axis
                if shift_d: shift_pos = (d-1,r-1,c-1)
                else: shift_pos = (d,r-1,c-1)
                try:
                    if matrix[shift_pos[0]][shift_pos[1]][shift_pos[2]] == 1:
                        if active_n(matrix, shift_pos, shift_d) == 2 or active_n(matrix, shift_pos, shift_d) == 3:
                            new_matrix[pos[0]][pos[1]][pos[2]] = 1
                        else : new_matrix[pos[0]][pos[1]][pos[2]] = 0
                    else:
                        if active_n(matrix, shift_pos, shift_d) == 3:
                            new_matrix[pos[0]][pos[1]][pos[2]] = 1
                        else:
                            new_matrix[pos[0]][pos[1]][pos[2]] = 0
                except IndexError:
                    if active_n(matrix, shift_pos, shift_d) == 3:
                        new_matrix[pos[0]][pos[1]][pos[2]] = 1
                    else:
                        new_matrix[pos[0]][pos[1]][pos[2]] = 0
    #The dimensions are repeating, where the first is equal to the last
    #the second to the second-to-last, etc. until the mid point
    for d in range(mid):
        new_matrix[d] = new_matrix[new_matrix.shape[0]-1-d]
    matrix = deepcopy(new_matrix)

actives = 0
for d in range(matrix.shape[0]):
    for r in range(matrix.shape[1]):
        for c in range(matrix.shape[2]):
            if matrix[d][r][c]==1: actives+=1
print(actives)



#Part 2
#Switch to a dictionary because easier to manage
matrix4d = np.array(matrix4d)
dict4d = {}
#probably overkill
for w in range(-10,10):
    for d in range(-10,10):
        for r in range(-10,10):
            for c in range(-10,10):
                dict4d[(w,d,r,c)]=0
for r in range(matrix4d.shape[2]):
    for c in range(matrix4d.shape[3]):
        dict4d[(0,0,r,c)] = matrix4d[1][1][r][c]
print(dict4d)

def active_n_4d(m, p, new_pos):
    #Same idea as before but if we find a new position we add it 
    #to a list of positions to be added to the dictionary 
    actives = 0
    for w in [-1,0,1]:
        for d in [-1,0,1]:
            for r in [-1,0,1]:
                for c in [-1,0,1]:
                    if (p[0]+w, p[1]+d, p[2]+r, p[3]+c) == (p[0], p[1], p[2], p[3]):
                        continue
                    try:
                        if m[((p[0]+w), (p[1]+d), (p[2]+r), (p[3]+c))] == 1:
                            actives+=1
                    except KeyError:
                        new_pos.append( ( (p[0]+w), (p[1]+d), (p[2]+r), (p[3]+c) ) )
    return actives

new_pos = []
for cycle in range(6):
    new_dict = deepcopy(dict4d)
    for v in new_pos:
        if v not in new_dict: new_dict[v] = 0
    new_pos = []
    for k in new_dict:
        try:
            if dict4d[k] == 1:
                if active_n_4d(dict4d, k, new_pos) == 2 or active_n_4d(dict4d, k, new_pos) == 3:
                    new_dict[k] = 1
                else : 
                    new_dict[k] = 0
            else:
                if active_n_4d(dict4d, k, new_pos) == 3:
                    new_dict[k] = 1
                else:
                    new_dict[k] = 0
        except KeyError:
            if active_n_4d(dict4d, k, new_pos) == 3:
                new_dict[k] = 1
            else:
                new_dict[k] = 0
    dict4d = deepcopy(new_dict)

actives = 0
for k in dict4d:
    actives+=dict4d[k]
print(dict4d)
print(actives)
