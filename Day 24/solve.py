#Part 1
#Using cube coordinates, cfr. https://www.redblobgames.com/grids/hexagons/#coordinates
moves = {'e': (1,-1,0), 'w': (-1,1,0), 'se': (0,-1,1), 'sw': (-1,0,1), 'ne': (1,0,-1), 'nw': (0,1,-1)}
map_ = {(0,0,0): 1}

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        out = []
        i=0
        for _ in range(len(line)):
            if i == len(line):
                break
            if line[i] == 'e' or line[i] =='w':
                out.append(line[i])
                i+=1
            else:
                out.append(line[i:i+2])
                i+=2
        x = (0,0,0) #center tile
        for dir_ in out:
            x = tuple([x[i]+moves[dir_][i] for i,_ in enumerate(x)])
            if x not in map_:
                map_[x] = 1 #white
        map_[x] = int(not map_[x]) #flip the reached tile


print(len([i for i in list(map_.values()) if i==0]))

#Part 2
#Return the no. of black adjacent tiles
def adj(tile, map):
    new = []
    count = 0
    for m in moves:
        a = tuple([tile[i]+moves[m][i] for i,_ in enumerate(tile)])
        if a not in map:
            new.append(a)
            continue
        else:
            if map[a]==0: count+=1
    return count, new

def flip(map):
    #use a set to avoid double tiles
    tiles = set()
    new_t = []
    for t in map:
        #get number of black adj. for each tile
        #and new tiles to be added to the map
        b, new = adj(t, map)
        if map[t] == 0:
            if b == 0 or b > 2:
                tiles.add(t)
        else:
            if b == 2: 
                tiles.add(t)
        for n in new:
            new_t.append(n)
    #add all new tiles to the map (as white)
    #if any have 2 black adjacents mark them for flipping
    for nt in new_t:
        map[nt] = 1
        b, _ = adj(nt, map)
        if b == 2: tiles.add(nt)
    #flip all marked tiles
    for tile in tiles:
        map[tile] = int(not map[tile])

for _ in range(100):
    flip(map_)
    #print('Day {}: {}'.format(_+1, len([i for i in list(map_.values()) if i==0])))
print(len([i for i in list(map_.values()) if i==0]))

