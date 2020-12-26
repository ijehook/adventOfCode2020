import sys
import math
from functools import reduce

# open up input list
inputFile = open(r"C:\Users\asyaa\Documents\adventOfCode\inputLists\day1Input.txt", "r")
inputList = []

# add each item in input list to list 
for x in inputFile:
    inputList.append(int(x.split('\n')[0]))

def findPairs(numNeeded): 
    for num in inputList:
        numExtra = numNeeded - num
        if numExtra < 0:
            next

        print('For the number {0}, the number needed is {1} to add up to {2}' .format(num, numExtra, numNeeded))

        if numExtra in inputList:
            if num not in numberPairs:
                
                numberPairs.append(num)
                numberPairs.append(numExtra)
                print('The number pairs adding up to {0} are {1}, {2}' .format(numNeeded, numberPairs[0], numberPairs[1]))
                break
                
    print('Number pairs is {0}' .format(numberPairs))
    return(numberPairs)
            
# find the three entries that add up to 2020 together 
numberPairs = []

for num in inputList:
    numNeeded = abs(2020 - num)
    print('For the number {0}, the number pairs need to add up to {1} to get 2020' .format(num, numNeeded))

    numberPairs = findPairs(numNeeded)
    
    if numberPairs:
        print("Number pairs found. The three numbers are {0}, {1}, {2}" .format(num, numberPairs[0], numberPairs[1]))
        finalNumbers = [num, numberPairs[0], numberPairs[1]]
        break


# final multiplication together 
mult = reduce((lambda x, y: x * y), finalNumbers)
add = reduce((lambda x, y: x + y), finalNumbers)

print("The final addition is {0}" .format(add))
print("The final multiplication is {0}" .format(mult))

