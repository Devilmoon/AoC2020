import itertools

#Part 1
mem = {}
mask = ''
with open('input.txt') as f:
    for line in f:
        data = line.strip().split(' = ')
        if data[0] == 'mask':
            mask = data[1]
        else:
            value = list(format(int(data[1]), '036b'))
            for i, char in enumerate(mask):
                if char != 'X': value[i] = char
            mem[data[0].split('[')[1][:-1]] = int('0b'+''.join([i for i in value]), 2)
print(sum(mem.values()))

#Part 2
mem = {}
mask = ''
with open('input.txt') as f:
    for line in f:
        data = line.strip().split(' = ')
        if data[0] == 'mask':
            mask = data[1]
        else:
            #Convert memory address mem[xxx] in 36 bit binary address 
            value = list(format(int(data[0].split('[')[1][:-1]), '036b'))
            #mask rules
            for i, char in enumerate(mask):
                if char == '1': value[i] = '1'
                elif char == 'X': value[i] = 'X'
            # X can be either 0 or 1, generate all combinations
            r = mask.count('X')
            comb = list(map(list, list(itertools.product(['0','1'], repeat=r))))
            addresses = []
            #generate all possible addresses when substituting X
            for l in comb:
                a = []
                counter = 0
                for c in value:
                    if c=='X':
                        #keep track of the X we are changing
                        a.append(l[counter])
                        counter+=1
                    else:
                        a.append(c)
                addresses.append(a)
            for a in addresses:
                #convert binary address to decimal, save input data
                mem[int('0b'+''.join([i for i in a]), 2)] = int(data[1])
print(sum(mem.values()))

# Alternative solution to Part 2
# Recursive generator which replaces one X at a time
# generating all possible addresses given a mask with Xs in it
# idea stolen from a comment online :) works wonderfully
def get_addresses(m):
    if 'X' in m:
        for r in ('0', '1'):
            yield from get_addresses(m.replace('X', r, 1))
    else:
        yield m

mem = {}
mask = ''
with open('input.txt') as f:
    for line in f:
        data = line.strip().split(' = ')
        if data[0] == 'mask':
            mask = data[1]
        else:
            #Convert memory address mem[xxx] in 36 bit binary address 
            value = list(format(int(data[0].split('[')[1][:-1]), '036b'))
            #mask rules
            for i, char in enumerate(mask):
                if char == '1': value[i] = '1'
                elif char == 'X': value[i] = 'X'
            for a in get_addresses(''.join([c for c in value])):
                #convert binary address to decimal, save input data
                mem[int('0b'+''.join([i for i in a]), 2)] = int(data[1])
print(sum(mem.values()))

for a in get_addresses('XXXX'):
    print(a)