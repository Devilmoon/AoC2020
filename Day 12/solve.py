with open('input.txt') as f:
    moves = [line.strip() for line in f.readlines()]

#Part 1
compass = ['E', 'S', 'W', 'N']
trans = {0:0, 90:1, 180:2, 270:3, 360:4}
current = 'E'
#+N/-S
NS = 0
#+E/-W
EW = 0

for move in moves:
    action = move[0]
    unit = int(move[1:])
    if action == 'N':
        NS+=unit
    elif action == 'S':
        NS-=unit
    elif action == 'E':
        EW+=unit
    elif action == 'W':
        EW-=unit
    elif action == 'F':
        if current == 'N':
            NS+=unit
        elif current == 'S':
            NS-=unit
        elif current == 'E':
            EW+=unit
        elif current =='W':
            EW-=unit
    elif action == 'R':
        pos = compass.index(current)
        shift = trans[unit]
        current = compass[(pos+shift) % 4]
    elif action == 'L':
        pos = compass.index(current)
        shift = trans[unit]
        current = compass[(pos-shift) % 4]
print(NS, EW, abs(NS)+abs(EW))

#Part 2
compass = ['E', 'S', 'W', 'N']
trans = {0:0, 90:1, 180:2, 270:3, 360:4}
#+N/-S
waypoint_NS = 1
#+E/-W
waypoint_EW = 10
NS = 0
EW = 0

for move in moves:
    action = move[0]
    unit = int(move[1:])
    if action == 'N':
        waypoint_NS+=unit
    elif action == 'S':
        waypoint_NS-=unit
    elif action == 'E':
        waypoint_EW+=unit
    elif action == 'W':
        waypoint_EW-=unit
    elif action == 'F':
        NS= NS + (unit*waypoint_NS)
        EW= EW + (unit*waypoint_EW)
    elif action in ['R', 'L']:
        tmp_NS = 0
        tmp_EW = 0
        tmp_wp = []
        waypoint = []
        if waypoint_NS >= 0: waypoint.append('N')
        else: waypoint.append('S')
        if waypoint_EW >= 0: waypoint.append('E')
        else: waypoint.append('W')
        for w in waypoint:
            pos = compass.index(w)
            shift = trans[unit]
            if action == 'R':
                new = (pos+shift) % 4
            else:
                new = (pos-shift) % 4
            if new % 4 == 4: continue
            if w in ['N', 'S'] and compass[new] in ['N', 'S']:
                tmp_NS = -waypoint_NS
            elif w in ['N', 'S'] and compass[new] in ['E', 'W']:
                if w == 'N' and compass[new]=='E': tmp_EW = waypoint_NS
                elif w == 'N' and compass[new]=='W': tmp_EW = -waypoint_NS
                elif w == 'S' and compass[new]=='E': tmp_EW = -waypoint_NS
                elif w == 'S' and compass[new]=='W': tmp_EW = waypoint_NS
            elif w in ['E', 'W'] and compass[new] in ['E', 'W']:
                tmp_EW = -waypoint_EW
            elif w in ['E', 'W'] and compass[new] in ['N', 'S']:
                if w == 'E' and compass[new] == 'N': tmp_NS = waypoint_EW
                elif w == 'E' and compass[new] == 'S': tmp_NS = -waypoint_EW
                elif w == 'W' and compass[new] == 'N': tmp_NS = -waypoint_EW
                elif w == 'W' and compass[new] == 'S': tmp_NS = waypoint_EW
        waypoint = tmp_wp
        waypoint_NS = tmp_NS
        waypoint_EW = tmp_EW
print(NS, EW, abs(NS)+abs(EW))