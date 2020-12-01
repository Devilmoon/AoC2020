expenses = []
with open("input.txt") as f:
    for i in f.readlines(): expenses.append(int(i.strip()))
expenses = sorted(expenses)

#First part
for e in expenses:
    if 2020-e in expenses:
        print(e*(2020-e), e, 2020-e)
        break

#Second part
for i, e in enumerate(expenses):
    for e_ in expenses[i+1:]:
        if 2020-e-e_ in expenses:
            print(e*e_*(2020-e-e_), e, e_, 2020-e-e_)
            break
