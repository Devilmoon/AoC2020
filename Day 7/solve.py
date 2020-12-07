import re, string
rules = {}
with open('input.txt') as f:
    for line in f.readlines():
        bags = line.strip().split('contain')
        #Remove punctuation and strip whitespace for each type of bag
        rules[bags[0].strip()] = [b.translate(str.maketrans('', '', string.punctuation)).strip() for b in bags[1].split(',')]

#Part 1
#Could also be done recursively?
ans = set()
tmp = ['shiny gold']
while True:
    if tmp != []:
        for el in tmp: ans.add(el)
        tmp = []
    else:
        break
    for _ in ans:
        for bag in rules.keys():
            for b in rules[bag]:
                if re.findall('({})'.format(_), b):
                    if bag[:-5] in ans: continue
                    tmp.append(bag[:-5])
#There's also shiny gold in there, so -1
print(len(ans)-1)

#Part 2
def recurse(key, last=1):
    solution = 0
    #When it's 1 bag instead of n bags
    if key[-1]!='s': key+='s'
    for b in rules[key]:
        if b == 'no other bags':
            return 0
        else:
            tmp = (int(b[0]) * last)
            solution += tmp + recurse(b[2:], tmp)
    return solution

print(recurse('shiny gold bags'))


