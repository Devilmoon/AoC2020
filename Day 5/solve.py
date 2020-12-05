def decode(bp):
    row = bp[:7]
    col = bp[-3:]
    row_lower, row_upper = 0, 127
    col_lower, col_upper = 0, 7
    for char in row:
        if char=='F':
            row_upper = ((row_upper+row_lower))//2
        else:
            row_lower = ((row_upper+row_lower)+1)//2
    for char in col:
        if char=='L':
            col_upper = ((col_upper+col_lower))//2
        else:
            col_lower = ((col_upper+col_lower)+1)//2
    sid = (row_lower*8)+col_lower
    return (row_lower, col_lower, sid)



passes = []
with open('input.txt') as f:
    for line in f.readlines():
        passes.append(line.strip())
max_sid = 0
sids = []
for p in passes:
    r,c,sid = decode(p)
    sids.append(sid)
    if sid>max_sid: max_sid=sid
mine = [sid+1 for sid in sids if (sid+1 not in sids and sid+2 in sids)]

#Part 1
print(max_sid)
#Part 2
print(mine)