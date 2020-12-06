#Part 1
s = 0
with open("input.txt") as f:
    group = ''
    for line in f.readlines():
        if line.strip() != '': group+=line.strip()
        else:
            s+= len(set(group))
            group=''
    if group!='': s+= len(set(group))
print(s)

#Part 2
s = 0
with open("input.txt") as f:
    newgroup = True
    for line in f.readlines():
        if line.strip() != '' and newgroup: 
            group = list(line.strip())
            newgroup = False
        elif line.strip() != '':
            group = [c for c in group if c in list(line.strip())]
        else:
            s+= len(group)
            group = []
            newgroup = True
    if group != []: s+= len(group)
print(s)