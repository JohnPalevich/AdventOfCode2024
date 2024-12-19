from collections import defaultdict
import re
from functools import cmp_to_key

test = "testInput/"
real = "input/"
day = "8.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    tot = 0 
    d = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != ".":
                d[a[i][j]].append((i,j))
    antis = set()
    # print(d)
    for key in d.keys():
        points = sorted(d[key], key=lambda x: sum(x))
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                pos1 = points[i]
                pos2 = points[j]
                rD = pos1[0] - pos2[0]
                cD = pos1[1] - pos2[1]
                anti1 = (pos1[0]-2*rD, pos1[1]-2*cD)
                anti2 = (pos2[0]+2*rD, pos2[1]+2*cD)
                # print(pos1, pos2, anti1, anti2)
                if 0 <= anti1[0] < len(a) and 0 <= anti1[1] < len(a[0]):
                    antis.add(anti1)                        
                if 0 <= anti2[0] < len(a) and 0 <= anti2[1] < len(a[0]):
                    antis.add(anti2)
    # print(antis)
    # for i in range(len(a)):
    #     for j in range(len(a[0])):
    #         if a[i][j] == ".":
    #             if (i,j) in antis:
    #                 print("#", end="")
    #             else: print(".", end="")
    #         else:
    #             print(a[i][j], end="")
    #     print("")
    return len(antis)

def part2(a):
    tot = 0 
    d = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != ".":
                d[a[i][j]].append((i,j))
    antis = set()
    # print(d)
    for key in d.keys():
        points = sorted(d[key], key=lambda x: sum(x))
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                pos1 = points[i]
                pos2 = points[j]
                rD = pos1[0] - pos2[0]
                cD = pos1[1] - pos2[1]
                
                c = 1
                anti1 = (pos1[0]-c*rD, pos1[1]-c*cD)
                while 0 <= anti1[0] < len(a) and 0 <= anti1[1] < len(a[0]):
                    antis.add(anti1)
                    c += 1
                    anti1 = (pos1[0]-c*rD, pos1[1]-c*cD)
                if 0 <= anti1[0] < len(a) and 0 <= anti1[1] < len(a[0]):
                    antis.add(anti1)  
                
                c = 1
                anti2 = (pos2[0]+c*rD, pos2[1]+c*cD)
                while 0 <= anti2[0] < len(a) and 0 <= anti2[1] < len(a[0]):
                    antis.add(anti2)
                    c+= 1
                    anti2 = (pos2[0]+c*rD, pos2[1]+c*cD)

                # print(pos1, pos2, anti1, anti2)                      
                if 0 <= anti2[0] < len(a) and 0 <= anti2[1] < len(a[0]):
                    antis.add(anti2)
    return len(antis)

testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput))
print(part2(input))