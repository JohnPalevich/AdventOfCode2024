from collections import defaultdict
import re
from functools import cmp_to_key

test = "testInput/"
real = "input/"
day = "6.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    tot = 0
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    currDir = 0
    gLoc = (0,0)
    g = []
    inMaze = True
    for i in range(len(a)):
        line = a[i]
        if "^" in line:
            gLoc = (i, line.index("^"))
            line = line.replace("^", ".")
        g.append([c for c in line])
    
    vLocs = {gLoc}
    while inMaze:
        nLoc = (gLoc[0] + dirs[currDir][0], gLoc[1] + dirs[currDir][1])
        if 0 <= nLoc[0] < len(g) and 0 <= nLoc[1] < len(g[0]):
            if g[nLoc[0]][nLoc[1]] == "#":
                currDir  = (currDir + 1) % 4
                nLoc = (gLoc[0] + dirs[currDir][0], gLoc[1] + dirs[currDir][1])
            gLoc = nLoc
            vLocs.add(gLoc)
        else:
            inMaze = False
            
    
    
    
    return len(vLocs)

def explore(a):
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    currDir = 0
    gLoc = (0,0)
    g = []
    inMaze = True
    for i in range(len(a)):
        line = a[i]
        if "^" in line:
            gLoc = (i, line.index("^"))
            line = line.replace("^", ".")
        g.append([c for c in line])
    
    vLocs = set()
    while inMaze:
        nLoc = (gLoc[0] + dirs[currDir][0], gLoc[1] + dirs[currDir][1])
        if 0 <= nLoc[0] < len(g) and 0 <= nLoc[1] < len(g[0]):
            if g[nLoc[0]][nLoc[1]] == "#":
                currDir  = (currDir + 1) % 4
                # nLoc = (gLoc[0] + dirs[currDir][0], gLoc[1] + dirs[currDir][1])
                nLoc = gLoc
            gLoc = nLoc
            if (gLoc, currDir) in vLocs:
                return False
            vLocs.add((gLoc, currDir))
        else:
            inMaze = False
    
    return True


def part2(a):
    tot = 0
    vLocs = pt2(a)
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == "." and (i,j) in vLocs:
                c = a.copy()
                c[i] = c[i][:j] + "#" + c[i][j+1:]
                # for l in c:
                    # print(l)
                if not(explore(c)):
                    tot += 1
                    # for l in c:
                    #   print(l)
                    # print()
                
            # print()
        # break
                
    return tot

def pt2(a):
    tot = 0
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    currDir = 0
    gLoc = (0,0)
    g = []
    inMaze = True
    for i in range(len(a)):
        line = a[i]
        if "^" in line:
            gLoc = (i, line.index("^"))
            line = line.replace("^", ".")
        g.append([c for c in line])
    
    vLocs = {gLoc}
    while inMaze:
        nLoc = (gLoc[0] + dirs[currDir][0], gLoc[1] + dirs[currDir][1])
        if 0 <= nLoc[0] < len(g) and 0 <= nLoc[1] < len(g[0]):
            if g[nLoc[0]][nLoc[1]] == "#":
                currDir  = (currDir + 1) % 4
                nLoc = (gLoc[0] + dirs[currDir][0], gLoc[1] + dirs[currDir][1])
            gLoc = nLoc
            vLocs.add(gLoc)
        else:
            inMaze = False
            
    # print(vLocs)
    # for loc in vLocs:
    #     pLoc, pDir = loc
    #     # print(pDir, pLoc)
    #     nDir =  (pDir + 1) % 4
    #     # print(nDir, )
    #     nLoc = (pLoc[0] + dirs[pDir][0], pLoc[1] + dirs[pDir][1])
    #     if (nLoc,nDir) in vLocs:
    #         print(nLoc,nDir)
    #         tot+=1
    
    return vLocs



testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput))
print(part2(input))