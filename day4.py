from collections import Counter
import re

test = "testInput/"
real = "input/"
day = "4.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    tot = 0
    g = []
    dirs = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
    for line in a:
        g.append([c for c in line])
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == "X":
                dirsCopy = [v for v in dirs]
                restC = "MAS"
                for k in range(len(restC)):
                    for loc in dirsCopy.copy():
                        v = k+1
                        nloc = [i + v*loc[0], j+ v*loc[1]]
                        if 0 <= nloc[0] < len(g) and 0 <= nloc[1] < len(g[0]) and g[nloc[0]][nloc[1]] == restC[k]:
                            continue
                        else:
                            dirsCopy.remove(loc)
                tot += len(dirsCopy)
    return tot


def part2(a):
    tot = 0
    g = []
    dirs = [(1,1), (1,-1), (-1,1), (-1,-1)]
    for line in a:
        g.append([c for c in line])
    mases = set()
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == "M":
                dirsCopy = [v for v in dirs]
                restC = "AS"
                for k in range(len(restC)):
                    for loc in dirsCopy.copy():
                        v = k+1
                        nloc = [i + v*loc[0], j+ v*loc[1]]
                        if 0 <= nloc[0] < len(g) and 0 <= nloc[1] < len(g[0]) and g[nloc[0]][nloc[1]] == restC[k]:
                            continue
                        else:
                            dirsCopy.remove(loc)
                for loc in dirsCopy:
                    mases.add(((i,j), loc))
    
    for i in range(len(g)):
        for j in range(len(g[0])):
            options = [((0,0),(1,1)),((0,2),(1,-1)),((2,0),(-1,1)),((2,2),(-1,-1))]
            c = 0
            for option in options:
                v = ((i+option[0][0], j+option[0][1]), option[1])
                if v in mases:
                    c+=1
            
            if c == 2:
                tot+=1
                
    return tot


testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput))
print(part2(input))