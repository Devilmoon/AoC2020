# First Part
valid = 0
with open("input.txt") as f:
    for line in f.readlines():
        bounds = line.split()[0].split('-')
        target = line.split()[1][0]
        password = line.split()[2]
        occurences = [i for i, x in enumerate(password) if x == target]
        if len(occurences) >= int(bounds[0]) and len(occurences) <= int(bounds[1]): valid+=1
print(valid)

# Second Part
valid = 0
with open("input.txt") as f:
    for line in f.readlines():
        indexes = line.split()[0].split('-')
        target = line.split()[1][0]
        password = line.split()[2]
        if bool(password[int(indexes[0])-1]==target) ^ bool(password[int(indexes[1])-1]==target): valid+=1
print(valid)
