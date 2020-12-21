tmp = {}
counter = []

with open('input.txt') as f:
    for line in f:
        line = line.strip().split(' (contains ')
        ingredients = line[0].split()
        allergens = line[1][:len(line[1])-1].split(', ')
        for i in ingredients:
            counter.append(i)
        for allergen in allergens:
            if allergen in tmp:
                tmp[allergen] = [i for i in tmp[allergen] if i in ingredients]
            else:
                tmp[allergen] = ingredients

#arbitrary number but it's enough to single out all ingredients
for i in range(5):
    for k in tmp:
        #Found the ingredient containing the allergen
        if len(tmp[k]) == 1:
            for j in tmp:
                if j != k and tmp[k][0] in tmp[j]:
                    #remove it from the other allergens
                    tmp[j].remove(tmp[k][0])

a = []
for el in list(tmp.values()):
    a.append(el[0])

#safe ingredients
counter = [i for i in counter if i not in a]
print(len(counter))

#list of unsafe ingredients ordered alphabetically by key
out = ''
for i, k in enumerate(sorted(tmp.keys())):
    out+=tmp[k][0]
    if i < len(tmp.keys())-1: out+=','
print(out)