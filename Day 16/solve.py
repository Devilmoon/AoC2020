import re, itertools, operator, functools

rules = {}
tickets = []
with open('input.txt') as f:
    for line in f:
        #name : range or range is a field rule
        if re.match('^[a-z]+ *[a-z]*: [0-9]+-[0-9]+ or [0-9]+-[0-9]+$', line.strip()):
            rule = line.strip().split(': ')
            tmp = rule[1].split(' or ')[0].split('-') + rule[1].split(' or ')[1].split('-') 
            ranges = [int(r) for r in tmp]
            rules[rule[0]] = [i for i in range(ranges[0], ranges[1]+1)] + [j for j in range(ranges[2], ranges[3]+1)]
        #string of 20 numbers is a ticket
        elif re.match('^([0-9]+,*){20}$', line.strip()):
            tickets.append([int(i) for i in line.strip().split(',')])

# Part 1
nvalid = []
discard = []
#All allowed values for all fields
allowed = list(itertools.chain.from_iterable(rules.values()))
#Not using my own ticket
for i, ticket in enumerate(tickets[1:]):
    for val in ticket:
        if val not in allowed:
            #if one of the values is not allowed
            #ticket is invalid
            nvalid.append(val)
            discard.append(i)
            break
    continue
print(sum(nvalid))

#------------------------------------------------------
#Part 2
#helper to check if the values in the same field
#in all tickets conforms to a specific rule
def valid(f, r, rules):
    for v in f:
        if v not in rules[r]: return False
    return True

valid_tickets = [t for i, t in enumerate(tickets[1:]) if i not in discard]
#Build the fields, i.e. take single value from position x in all tickets
#to build field x
fields = []
for i in range(len(valid_tickets[0])):
    tmp = []
    for t in valid_tickets:
        tmp.append(t[i])
    fields.append(tmp)
#reason about the rules, if the values of all valid tickets for a specific field
#respect a given rule, that field might be the one described by that rule
#but not necessarily. More than one field might conform to one rule.
reason = {r:[] for r in rules}
for rule in rules:
    for i, field in enumerate(fields):
        if valid(field, rule, rules):
            reason[rule] += [i]

#Find the field of each rule
count = 0
while reason:
    #we found all rules
    if count==20: break
    for r in reason:
        #if a field is compatible with only one rule,
        #that rule's field is found
        if len(reason[r])==1:
            field = reason[r][0]
            rules[r] = field
            count+=1
            #remove the field from all other rules
            for _ in reason:
                if field in reason[_]: reason[_].remove(field)
            break

#compute final solution to part 2, multiply together the values of my ticket
#for the six fields that start with 'departure'
solution = []
for r in rules:
    if r.split(' ')[0] == 'departure': solution.append(tickets[0][rules[r]])

def prod(iterable):
    return functools.reduce(operator.mul, iterable, 1)

print(prod(solution))
