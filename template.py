test = "testInput/"
real = "input/"
day = "1.txt"
from collections import *
from functools import*

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    tot = 0
    return tot

def part2(a):
    tot = 0
    return tot


testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
# print(part2(testInput))
# print(part2(input))