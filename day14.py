from collections import defaultdict, Counter
import re
from functools import cmp_to_key, lru_cache
from time import sleep

test = "testInput/"
real = "input/"
day = "14.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a, width, height):
    tot = 1
    locs = defaultdict(int)
    v = 100
    for l in a:
        x,y = [int(v) for v in l.split()[0][2:].split(",")]
        xV,yV = [int(v) for v in l.split()[1][2:].split(",")]
        # print(x,y,xV,yV)
        pos = ((x+100*xV)%width,(y+100*yV)%height)
        locs[pos] += 1
    q = [0,0,0,0]
    quad = 0
    for i in range(height):
        if i == height // 2:
            quad = 2
        else:
            for j in range(width):
                if j == width // 2:
                    quad+=1
                else:
                    if (j,i) in locs.keys():
                        q[quad] += locs[(j,i)]
            quad -=1
    print(q)
    for v in q:
        tot *= v
    display(locs,height, width, True)

    return tot

def display(locs, height, width, quads):
    for i in range(height):
        if i == height // 2 and quads:
            print()
        else:
            for j in range(width):
                if j == width // 2 and quads:
                    print(" ", end ="")
                else:
                    if (j,i) in locs.keys():
                        print(locs[(j,i)], end="")
                    else:
                        print(".", end="")
            print()

def part2(a, width, height):
    tot = 1
    locs = defaultdict(int)
    v = 100
    bots = []
    for l in a:
        x,y = [int(v) for v in l.split()[0][2:].split(",")]
        xV,yV = [int(v) for v in l.split()[1][2:].split(",")]
        # print(x,y,xV,yV)
        bots.append((x,y,xV,yV))
    
    for i in range(10_000):
        seen = set()
        for j in range(len(bots)):
            x,y,xV,yV = bots[j]
            pos = (x+xV,y+yV)
            while pos[0] > width or pos[0] < 0 or pos[1] > height or pos[1] < 0:
                pos = (pos[0]%width,pos[1]%height)
            seen.add(pos)
            bots[j] = (pos[0],pos[1],xV,yV)
        for bot in bots:
                locs[bot[:2]] +=1
        print(i+1)
        sleep(0.1)
        display(locs,height, width, False)

        if len(seen) == len(bots):
            for bot in bots:
                locs[bot[:2]] +=1
            # print(locs)
            display(locs,height, width, False)
            return i+1
        locs = defaultdict(int)
    locs = defaultdict(int)
    
    

testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput, 11, 7))
print(part1(input, 101, 103))
# print(part2(testInput))
print(part2(input, 101, 103))