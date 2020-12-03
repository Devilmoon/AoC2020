map_ = []
with open("input.txt") as f:
    for line in f.readlines():
        row = []
        for char in line.strip():
            if char=='.': row.append(0)
            else: row.append(1)
        map_.append(row*3000)

t1 = t2 = t3 = t4 = t5 = 0
s1 = s2 = s3 = s4 = 0
# 0,0 is open and first pass is on 2,1 
s5=1

for r in range(len(map_)):
    if map_[r][s1]==1: 
        t1+=1
    if map_[r][s2]==1: 
        t2+=1
    if map_[r][s3]==1: 
        t3+=1
    if map_[r][s4]==1: 
        t4+=1
    if (r+1) % 2 == 0 and r+1 < len(map_):
        if map_[r+1][s5]==1: 
            t5+=1
        s5+=1
    s1+=1
    s2+=3
    s3+=5
    s4+=7

print("First Part: " + str(t2))
print("Second Part: " + str(t1*t2*t3*t4*t5))