with open('input.txt') as f:
    adapters = [int(a.strip()) for a in f.readlines()]

# Part 1
adapters = [0] + sorted(adapters)
prior = adapters[0]
diff = {1: 0, 2: 0, 3: 1}
for a in adapters[1:]:
    if a-3 <= prior:
        diff[a-prior]+=1
        prior = a
print(diff, diff[1]*diff[3])

#Part 2
#The idea is to count the possible ways to get to each adapters based on the previous ones
#To get to 0 we always have 1 path, and then start counting the others.
possible = [1] + [0 for a in adapters[1:]]
for i, a in enumerate(adapters):
    for j in range(i-3, i):
        #If any of the three previous adapters are usable with the current adapter, then 
        #we add the possible ways to get to the previous adapter to the current one, since 
        #all combinations leading to adapters[j] can also lead to adapters[i]
        if a - adapters[j] <= 3:
            possible[i] += possible[j]
#How many combinations lead to the last adapter (and the phone)
print(possible[-1])