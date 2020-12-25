keys = {}
with open('input.txt') as f:
    for line in f:
        keys[int(line.strip())] = 0

counter = 1
subject = 7
value = 1
while 0 in keys.values():
    value = value * subject
    value = value % 20201227
    if value in keys:
        keys[value] = counter
    counter += 1

#print(keys)

def break_key(key, loop):
    subject = key
    value = 1
    for _ in range(loop):
        value = value * subject
        value = value % 20201227
    return value

k = list(keys)
ek1 = break_key(k[0], keys[k[1]])
ek2 = break_key(k[1], keys[k[0]])

print(ek1,ek2)