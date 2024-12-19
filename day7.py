from collections import defaultdict
import re
from functools import cmp_to_key

test = "testInput/"
real = "input/"
day = "7.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def recur(goal, curr, rem):
    if curr > goal:
        return False
    if rem == []:
        return goal == curr
    return recur(goal, curr+rem[0], rem[1:]) or recur(goal, curr*rem[0], rem[1:])

def part1(a):
    tot = 0 
    for line in a:
        parts = line.split()
        goal = int(parts[0][:-1])
        values = [int(v) for v in parts[1:]]
        if recur(goal, values[0], values[1:]):
            tot += goal
    return tot

def recur2(goal, curr, rem):
    if curr > goal:
        return False
    if rem == []:
        return goal == curr
    return recur2(goal, curr+rem[0], rem[1:]) or recur2(goal, curr*rem[0], rem[1:]) or recur2(goal, int(str(curr)+str(rem[0])), rem[1:])

def part2(a):
    tot = 0 
    for line in a:
        parts = line.split()
        goal = int(parts[0][:-1])
        values = [int(v) for v in parts[1:]]
        if recur2(goal, values[0], values[1:]):
            tot += goal
    return tot

testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput))
print(part2(input))