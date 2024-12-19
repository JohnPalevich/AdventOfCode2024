from collections import defaultdict
import re
from functools import cmp_to_key

test = "testInput/"
real = "input/"
day = "9.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    tot = 0 
    storage = []
    id = 0
    start = True
    for c in a[0]:
        if start:
            for i in range(int(c)):
                storage.append(id)
            id += 1
            start=False
        else:
            for i in range(int(c)):
                storage.append(".")
            start=True
    # print(storage)
    
    back = len(storage)-1
    for i in range(len(storage)):
        if storage[i] == ".":
            if back <= i:
                break
            tot += i * int(storage[back])
            # storage[i] = storage[back]
            storage[back] = "."
            back -= 1
            while storage[back] == ".":
                back -= 1
        else:
            tot += i * int(storage[i])
        # print(i, back, storage)
    return tot

def part2(a):
    tot = 0 
    storage = []
    id = 0
    start = True
    files = []
    spaces = []
    inds = defaultdict(list)
    for c in a[0]:
        if start:
            for i in range(int(c)):
                storage.append(id)
                inds[id].append(len(storage))
            files.append(int(c))
            id += 1
            start=False
        else:
            s = len(storage)
            for i in range(int(c)):
                storage.append(".")
            e = len(storage)
            if e-s!=0:
                spaces.append((s,e-s))
            start=True
    
    def fillSpace(file):
        fileLen = files[file]
        for i in range(len(spaces)):
            space = spaces[i]
            if space[1] >= fileLen and space[0] < inds[file][0]:
                # Move file
                for j in range(fileLen):
                    storage[space[0]+j] = file
                for v in inds[file]:
                    storage[v-1] = "."
                # Update spaces
                spaces.pop(i)
                if space[1] > fileLen:
                    spaces.insert(i,(space[0]+fileLen,space[1]-fileLen))                
                break
    
    for file in reversed(range(len(files))):
        fillSpace(file)
        
    for i in range(len(storage)):
        tot+= i*int(storage[i]) if storage[i] != "." else 0
    
    return tot

testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput))
print(part2(input))