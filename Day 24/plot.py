import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np

def plot_hex(m):
    coord = list(m.keys())
    colors = [['Black'] if m[c]==0 else ['White'] for c in coord]
    #labels = [['yes'],['no'],['yes'],['no'],['yes'],['no'],['no']]

    # Horizontal cartesian coords
    hcoord = [c[0] for c in coord]

    # Vertical cartersian coords
    vcoord = [2. * np.sin(np.radians(60)) * (c[1] - c[2]) /3. for c in coord]

    lim = max(max(hcoord), max(vcoord))
    fig, ax = plt.subplots(figsize=(20,20))
    plt.xlim(-(lim+5),lim+5)
    plt.ylim(-(lim+5),lim+5)
    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')

    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    plt.axis('off')

    # Show ticks in the left and lower axes only
    #ax.xaxis.set_ticks_position('bottom')
    #ax.yaxis.set_ticks_position('left')
    #ax.set_aspect('equal')

    # Add some coloured hexagons
    for x, y, c in zip(hcoord, vcoord, colors):
        color = c[0].lower()  # matplotlib understands lower case words for colours
        hex = RegularPolygon((x, y), numVertices=6, radius=2. / 3., 
                            orientation=np.radians(30), 
                            facecolor=color, alpha=1, edgecolor='black')
        ax.add_patch(hex)
        # Also add a text label
        #ax.text(x, y+0.2, l[0], ha='center', va='center', size=20)

    # Also add scatter points in hexagon centres
    #ax.scatter(hcoord, vcoord, c=[c[0].lower() for c in colors], alpha=0.5)

    plt.show()

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
plot_hex(map_)

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
        #map[nt] = 1
        b, _ = adj(nt, map)
        if b == 2:
            map[nt] = 1
            tiles.add(nt)
    #flip all marked tiles
    for tile in tiles:
        map[tile] = int(not map[tile])


for _ in range(100):
    flip(map_)
    #print('Day {}: {}'.format(_+1, len([i for i in list(map_.values()) if i==0])))
print(len([i for i in list(map_.values()) if i==0]))
plot_hex(map_)

'''
for _ in range(1000):
    flip(map_)
print(len([i for i in list(map_.values()) if i==0]))
#plot_hex(map_)
'''