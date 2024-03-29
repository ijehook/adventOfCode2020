import math

# open up input list
inputFile = open(r"C:\Users\asyaa\Documents\adventOfCode\inputLists\day7Input.txt", "r")

# read the puzzle input
bagRules = []
for count, entry in enumerate(inputFile):
    bagRules.append(entry.split('\n')[0])

# make a dictionary
bagDictionary = {}
for rule in bagRules:
    bagContents = rule.split("bag")
    dictKey = bagContents[0].replace(" ", "")
    bagDictionary[dictKey] = {}

    bagWithin = []
    for bc in bagContents[1:]:
        if bc == "s.":
            continue
        
        bag = bc.replace(" ", "")
        bag = bag.replace("scontain", "")
        bag = bag.replace("s,", "")
        bag = bag.replace(",", "")
        bag = bag.replace(".", "")
        
        if bag:
            bagWithin.append(bag)

    bagWithinDict = {}
    for bw in bagWithin:
        if bw == "noother":
            bagDictionary[dictKey] = {}
            continue
        bagNumber = int(bw[0][0])
        bagType = str(bw[1:])
        bagWithinDict[bagType] = bagNumber
    
    if bagWithinDict:
        bagDictionary[dictKey] = bagWithinDict

def countContainingBag(bagType = ""):
    bagsContainingType = []
    for bag in bagDictionary:
        if bagType in bagDictionary[bag]:
            countContainingBag(bag)
            bagsContainingType.append(bag)
            bagset.add(bag)

    return 


bagset = set()
countContainingBag("shinygold")
print("Part 1: The amount of different coloured bags that can hold a shiny gold bag: " + str(len(bagset)))

#print(bagDictionary)

#print(bagDictionary)

bagsWithin = []
def bagsInBag(bagType):
    # find bags within 
    bagContents = bagDictionary[bagType]
    bagsList = []
    for bag in bagContents:
        for i in range(bagDictionary[bagType][bag]):
            bagsList.append(bag)
    
    return bagsList

def findB(bagType):
    for bag in bagDictionary[bagType]:
        for i in range(bagDictionary[bagType][bag]):
            x = bagsInBag(bag)
            findB(bag)
            bagsWithin.append(x)

findB("shinygold")
print(len(bagsWithin))

def countBagsWithin(bagColor):
    count = 0
    for bag in bagDictionary[bagColor]:
        count += bagDictionary[bagColor][bag] + countBagsWithin(bag) * bagDictionary[bagColor][bag]
    return count

print(countBagsWithin(bagColor="shinygold"))

for bag in bagDictionary:
    print(bag)