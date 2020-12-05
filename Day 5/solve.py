from codetiming import Timer

@Timer(text="decoded in {:.10f} seconds")
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

@Timer(text="alt decoded in {:.10f} seconds")
def alternative_decode(bp):
    # 7 bits for 128 rows, 3 bits for 8 columns. A string of all Fs and Ls means row 0
    # column 0. Replace all the characters with 0 and 1 and translate to integer to get
    # everything we need.
    bp = bp.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1')
    return(int(bp[:7], 2), int(bp[-3:], 2), (int(bp[:7], 2)*8)+int(bp[-3:], 2))



passes = []
with open('input.txt') as f:
    for line in f.readlines():
        passes.append(line.strip())
max_sid = 0
max_sid_= 0
sids = []
for p in passes:
    r,c,sid = decode(p)
    r_,c_,sid_ = alternative_decode(p)
    sids.append(sid)
    if sid>max_sid: max_sid=sid
    if sid_>max_sid_: max_sid_=sid_
mine = [sid+1 for sid in sids if (sid+1 not in sids and sid+2 in sids)]

#Part 1
print(max_sid)
#same solution
print(max_sid_)
#Part 2
print(mine)