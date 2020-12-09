class Breaks ( Exception ):
    pass

XMAS = []

with open('input.txt') as f:
    for line in f.readlines(): XMAS.append(int(line.strip()))

#Part 1
window = 0
target = 0
for n in XMAS[25:]:
    preamble = XMAS[window:25+window]
    window+=1
    found=False
    try:
        for i, el in enumerate(preamble):
            for _ in preamble[i+1:]:
                if el+_ == n and el!=_:
                    raise Breaks
    except Breaks:
        found=True
    if not found:
        target = n
        print(n)
        break

#Part 2
for i, n in enumerate(XMAS):
    tmp = n
    for j, m in enumerate(XMAS[i+1:]):
        tmp+=m
        if tmp == target:
            upper = i+j+1
            clist = XMAS[i:upper+1]
            #Sum smallest+biggest
            clist = sorted(clist)
            print(clist[0]+clist[-1])
        elif tmp > target:
            break

