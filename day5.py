from collections import defaultdict
import re
from functools import cmp_to_key

test = "testInput/"
real = "input/"
day = "5.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    tot = 0
    before = defaultdict(set)
    after = defaultdict(set)
    updates = []
    for line in a:
        if "|" in line:
            ps = line.split("|")
            before[ps[0]].add(ps[1])
            after[ps[1]].add(ps[0])
        elif "," in line:
            updates.append(line.split(","))
    
    for update in updates:
        save = True
        for i in range(len(update)):
            pre = update[:i]
            post = update[i+1:]
            page = update[i]
            for p in pre:
                if page in after[p]:
                    save = False
                    break
            for p in post:
                if page in before[p]:
                    save = False
                    break
        if save:
            # print(update, int(update[len(update)//2]))
            tot += int(update[len(update)//2])
                
        
    return tot


def part2(a):
    tot = 0
    before = defaultdict(set)
    after = defaultdict(set)
    updates = []
    for line in a:
        if "|" in line:
            ps = line.split("|")
            before[ps[0]].add(ps[1])
            after[ps[1]].add(ps[0])
        elif "," in line:
            updates.append(line.split(","))
    
    incorrectPages = []
    for update in updates:
        save = True
        for i in range(len(update)):
            pre = update[:i]
            post = update[i+1:]
            page = update[i]
            for p in pre:
                if page in after[p]:
                    save = False
                    break
            for p in post:
                if page in before[p]:
                    save = False
                    break
        if not save:
            incorrectPages.append(update)
    
    def customSort(a, b):
        if a in after[b]:
            return -1
        else:
            return 1
    
    letter_cmp_key = cmp_to_key(customSort)
    for update in incorrectPages:
        update.sort(key=letter_cmp_key)
        tot += int(update[len(update)//2])
    return tot



testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput))
print(part2(input))