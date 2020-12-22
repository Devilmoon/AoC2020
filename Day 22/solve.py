f = open('input.txt')
lines = f.readlines()
p1 = []
p2 = []
switch = False
for l in lines:
    if l.strip() == 'Player 1:':
        continue
    if l == '\n':
        continue
    if l.strip() == 'Player 2:':
        switch = True
        continue
    if not switch:
        p1.append(int(l.strip()))
    if switch:
        p2.append(int(l.strip()))
p1 = p1[::-1]
p2 = p2[::-1]


def play_part1(p1, p2):
    while p1 and p2:
        one = p1.pop()
        two = p2.pop()
        stack = [min(one,two), max(one,two)]
        if stack[1] == one:
            p1 = stack + p1
        else:
            p2 = stack + p2
    return p1, p2

def play_part2(p1, p2):
    rounds_1 = []
    rounds_2 = []
    while p1 and p2:
        if p1 in rounds_1 and p2 in rounds_2:
            return p1, []
        else:
            rounds_1.append([k for k in p1])
            rounds_2.append([j for j in p2])
        one = p1.pop()
        two = p2.pop()
        if len(p1) >= one and len(p2) >= two:
            p1_, _ = play_part2(p1[-one:], p2[-two:])
            if p1_:
                p1 = [two, one] + p1
            else:
                p2 = [one, two] + p2
        else:
            stack = [min(one,two), max(one,two)]
            if stack[1] == one:
                p1 = stack + p1
            else:
                p2 = stack + p2
    return p1, p2

def score(p1, p2):
    score = 0
    if p1:
        for i, val in enumerate(p1):
            score+= val*(i+1)
    elif p2:
        for i,val in enumerate(p2):
            score+= val*(i+1)
    return(score)

#p1, p2 = play_part1(p1,p2)
#print(p1, p2)
#print(score(p1, p2))

p1, p2 = play_part2(p1,p2)
print(p1, p2)
print(score(p1, p2))
