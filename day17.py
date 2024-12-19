test = "testInput/"
real = "input/"
day = "17.txt"
from collections import Counter
import networkx as nx
import heapq
from heapq import _siftdown
from functools import cmp_to_key, lru_cache


def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    tot = []
    
    registers = {"a": int(a[0].split()[-1]), "b": int(a[1].split()[-1]), "c": int(a[2].split()[-1])}
    program = [int(v) for v in a[-1].split()[-1].split(",")]
    
    combo = {0:0, 1:1, 2:2, 3:3, 4:"a", 5:"b", 6:"c", 7:None}
    
    print(registers, program)
    
    def getCombo(operand):
        c = combo[operand]
        if type(c) is str:
            c = registers[c]
        return c
    
    pointer = 0
    i = 0
    while pointer < len(program)-1:
        print(tot)
        opcode = program[pointer]
        operand = program[pointer+1]
        print(pointer, opcode, operand, registers)
        shouldIncrease = True
        if opcode == 0:
            numer = registers["a"]
            denom = 2**getCombo(operand)
            registers["a"] = numer // denom
        elif opcode == 1:
            registers["b"] = registers["b"] ^ operand
        elif opcode == 2:
            registers["b"] = getCombo(operand) % 8
        elif opcode == 3:
            if registers["a"] != 0:
                pointer = operand
                shouldIncrease = False
        elif opcode == 4:
            registers["b"] = registers["b"] ^ registers["c"]
        elif opcode == 5:
            # print(operand)
            # print(getCombo(operand) % 8)
            tot.append(getCombo(operand) % 8)
        elif opcode == 6:
            numer = registers["a"]
            denom = 2**getCombo(operand)
            registers["b"] = numer // denom
        elif opcode == 7:
            numer = registers["a"]
            denom = 2**getCombo(operand)
            registers["c"] = numer // denom

        pointer += 2 if shouldIncrease else 0
        
        print(pointer,opcode, operand, registers, end="\n\n")

        i+=1
    
    return ",".join([str(v) for v in tot])

def part2(a):
    # Program: 2,4,1,3,7,5,4,7,0,3,1,5,5,5,3,0
    # 2,4: B = A % 8
    # 1,3: B = B XOR 3
    # 7,5: C = A // ( 2**B) == A >> B
    # 4,7: B = B XOR C
    # 0,3: A = A // (2 **3) == A >> 3
    # 1,5: B = B XOR 5
    # 5,5 = out(B % 8)
    # 3,0 = jnz(0)
    
    def getAB(a):
        b = a % 8
        b = b ^ 3
        c = a >> b
        b = b ^ c
        a = a >> 3
        b = b ^ 5
        out = b % 8
        return a, out
    
    def searchFor(a, remProg):
        if len(remProg) == 0:
            return a
        
        for i in range(8):
            tryA = (a << 3) + i
            ta, out = getAB(tryA)
            if ta == a and out == remProg[-1]:
                v = searchFor(tryA, remProg[:-1])
                if v:
                    return v
        return None
    
    program = [int(v) for v in a[-1].split()[-1].split(",")]
    a = 0
    a = searchFor(0, program)

    
    return a

testInput = getInput(test+day)
input = getInput(real+day)
# print(part1(testInput))
# print(part1(input))
# print(part2(testInput))
print(part2(input))