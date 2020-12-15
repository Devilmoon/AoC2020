with open('input.txt') as f:
    start = f.read().strip().split(',')

mem = {}
for i, val in enumerate(start):
    mem[int(val)] = [i+1]

last = int(start[-1])

for turn in range(len(start)+1, 30000001):
    if last not in mem:
        mem[last] = [turn-1]
        last = 0
        if turn==2020 or turn==30000000: print(last)
    else:
        mem[last].append(turn-1)
        last = mem[last][-1] - mem[last][-2]
        if turn==2020 or turn==30000000: print(last)

'''
Memory efficient alternative, doesn't seem faster

for turn in range(len(start)+1, 30000001):
    if last not in mem:
        mem[last] = turn-1
        last = 0
        if turn==2020 or turn==30000000: print(last)
    else:
        tmp = turn - mem[last] - 1
        mem[last] = turn-1
        last = tmp
        if turn==2020 or turn==30000000: print(last)
'''

'''
Seems equivalent to the for loop implementation but wrong asnwer?

playing = False
turn = len(start)+1
last = int(start[-1])

while playing:
    if turn == 2020 and last not in mem:
        print(0)
        playing=False
        break
    elif turn == 2020 and last in mem:
        print(mem[last][-1] - mem[last][-2])
        playing = False
        break
    if last not in mem:
        mem[last] = [turn-1]
        last = 0
        turn += 1
    else:
        mem[last].append(turn-1)
        last = mem[last][-1] - mem[last][-2]
        turn += 1
'''