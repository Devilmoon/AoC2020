from copy import deepcopy

b = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip()
        row = []
        for char in line:
            if char=='L': row.append(0)
            elif char=='.': row.append(-1)
        b.append(row)
b2 = deepcopy(b)

# Part 1
def count_occupied(r,c, board):
    count = 0
    adjacent = [(r-1, c),(r, c-1),(r+1, c),(r, c+1),(r-1, c-1),(r+1, c+1),(r-1, c+1),(r+1, c-1)]
    for a in adjacent:
        if 0<=a[0]<len(board) and 0<=a[1]<len(board[0]):
            if board[a[0]][a[1]] == 1  : count+=1
    return count

change = True
while change:
    change = False
    new_board = deepcopy(b)
    for r in range(len(b)):
        for c in range(len(b[0])):
            if b[r][c] == 0:
                if count_occupied(r,c,b) == 0: 
                    new_board[r][c] = 1
                    change = True
            elif b[r][c] == 1:
                if count_occupied(r,c,b) >= 4:
                    new_board[r][c] = 0
                    change = True
    b = deepcopy(new_board)

final = 0
for r in range(len(b)):
    for c in range(len(b[0])):
        if b[r][c] == 1: final+=1
print(final)


#Part 2
def count_occupied_updated(r, c, board):
    count = 0
    found = [0]*8
    seats = [0,1]

    for x in range(1, len(board)):
        if found[0] and found[1] and found[2]: break
        if r-x >= 0:
            if board[r-x][c] in seats and not found[0]: 
                count += board[r-x][c]
                found[0] = 1
        if c-x >= 0:
            if board[r][c-x] in seats and not found[1]: 
                count += board[r][c-x]
                found[1] = 1
        if (r-x >= 0 and c-x >= 0):
            if board[r-x][c-x] in seats and not found[2]: 
                count += board[r-x][c-x]
                found[2] = 1

    for x in range(1, len(board)):
        if found[3] and found[4] and found[5]: break
        if r+x < len(board):
            if board[r+x][c] in seats and not found[3]: 
                count += board[r+x][c]
                found[3] = 1
        if c+x < len(board[0]):
            if board[r][c+x] in seats and not found[4]: 
                count += board[r][c+x]
                found[4] = 1
        if (r+x < len(board) and c+x < len(board[0])):
            if board[r+x][c+x] in seats and not found[5]: 
                count += board[r+x][c+x]
                found[5] = 1

    for x in range(1, len(board)):
        if (r-x >= 0 and c+x < len(board[0])):
            if board[r-x][c+x] in seats and not found[6]: 
                count += board[r-x][c+x]
                found[6] = 1
        if (r+x < len(board) and c-x >= 0):
            if board[r+x][c-x] in seats and not found[7]: 
                count += board[r+x][c-x]
                found[7] = 1
    return count

change = True
while change:
    change = False
    new_board2 = deepcopy(b2)
    for r in range(len(b2)):
        for c in range(len(b2[0])):
            if b2[r][c] == 0:
                if count_occupied_updated(r,c, b2) == 0: 
                    new_board2[r][c] = 1
                    change = True
            elif b2[r][c] == 1:
                if count_occupied_updated(r,c, b2) >= 5:
                    new_board2[r][c] = 0
                    change = True
    b2 = deepcopy(new_board2)

final = 0
for r in range(len(b2)):
    for c in range(len(b2[0])):
        if b2[r][c] == 1: final+=1
print(final)