with open('input.txt') as f:
    for i in range(2):
        if i==0:
            arrival = int(f.readline().strip())
        else:
            departures_raw = f.readline().strip()
departures = [int(i) for i in departures_raw.split(',') if i != 'x']

offset = [(arrival//i)+1 for i in departures]
#Find the earliest timestamp greater than our arrival for all buses
tmp = ([x*offset[i] for i, x in enumerate(departures) if x*offset[i]>=arrival])
#Use the smallest timestamp found to compute result
print(min(tmp), departures[tmp.index(min(tmp))], departures[tmp.index(min(tmp))] * (min(tmp)-arrival))

#Part 2
new_dep = [int(i) for i in departures_raw.replace('x', '1').split(',')]
indexes = [new_dep.index(i) for i in new_dep if i!=1]
t = 0
step = new_dep[0]
max_set = 1
searching = True
while searching:
    t += step
    for i in indexes:
        #If current timestamp+bus offset is divisible by the bus ID
        #It means that the bus will leave at t+offset
        if (t+i) % new_dep[i] == 0:
            #If we found a solution for a new bus ID, we can start
            #incrementing the timestamp by the solution we found
            #times the new ID. This is because if we found a t such that
            #ID1*x=t and ID2*y=t+1, the next valid solution for both IDs
            #will be found at t+(ID1*ID2) for ID1 and (t+1)+(ID1*ID2) for ID2.
            #Hence we can skip checking all values between t and (t+(ID1*ID2))-1
            #Proof is in Number Theory / Chinese Remainder Theorem etc., quite
            #complicated math.
            if i>max_set:
                max_set = i
                # Since step initially is the first ID (first bus will always leave at multiples of ID)
                # we can just keep multiplying step by the new ID to update it correctly.
                step = step*new_dep[i]
            # if this is the last ID we have found a solution for all IDs, print timestap.
            if i == len(new_dep)-1: 
                print(t)
                searching = False
                break
            continue
        else:
            break