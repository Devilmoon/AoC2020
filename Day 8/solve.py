with open('input.txt') as f:
    instructions = [line.strip() for line in f.readlines()]

accumulator = 0
seen = []
i = 0
while True:
    if i in seen:
        print('repeat')
        print(accumulator)
        break
    else:
        seen.append(i)
    inst = instructions[i].split()
    if inst[0] == 'nop':
        i+=1
        continue
    elif inst[0] == 'acc':
        accumulator += int(inst[1])
        i+=1
        continue
    elif inst[0] == 'jmp':
        i+=int(inst[1])
        continue


# Part 2
jmps = [i for i in seen if instructions[i].split()[0] == 'jmp']
nops = [i for i in seen if instructions[i].split()[0] == 'nop']
checking = True
for n in jmps:
    accumulator = 0
    seen = []
    i = 0
    while checking:
        if i == len(instructions):
            print('Terminated')
            print(n, instructions[n])
            print("SOLUTION: {}".format(accumulator))
            checking=False
            break
        if i in seen:
            break
        else:
            seen.append(i)
        if i == n:
            i+=1
            continue
        inst = instructions[i].split()
        if inst[0] == 'nop':
            i+=1
            continue
        elif inst[0] == 'acc':
            accumulator += int(inst[1])
            i+=1
            continue
        elif inst[0] == 'jmp':
            i+=int(inst[1])
            continue