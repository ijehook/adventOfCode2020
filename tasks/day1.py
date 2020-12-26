import sys
import math
from functools import reduce

# open up input list
inputFile = open(r"C:\Users\asyaa\Documents\adventOfCode\inputLists\day1Input.txt", "r")
inputList = []

# add each item in input list to list 
for x in inputFile:
    inputList.append(float(x.split('\n')[0]))

# find two entries that add up to 2020 together 
numberPairs = []
for num in inputList:
    num = int(num)
    numNeeded = abs(2020 - num)

    print('For the number {0}, the number needed is {1}' .format(num, numNeeded))

    if numNeeded in inputList:
        if num not in numberPairs:
            print('The num needed {0} exists!' .format(numNeeded))
            numberPairs.append(num)
            numberPairs.append(numNeeded)

print('The number pairs are {0}' .format(numberPairs))

# final multiplication together 
mult = reduce((lambda x, y: x * y), numberPairs)
print("The final multiplication is {0}" .format(int(mult)))

# test

