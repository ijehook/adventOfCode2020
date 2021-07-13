# open up input list
inputFile = open(r"C:\Users\asyaa\Documents\adventOfCode\inputLists\day7Input.txt", "r")

# create a dictionary. every key is the first bag of the rule, which has the contents
# for every key, add another dictionary of bag type : numer

"""
bagRules = {
    "bright_gray" = {
        "bright_gold_bags" : 2,
        "5_dull_lavender" : 5
    },
    "pale_olive" := {
        "bright_yellow" : 1,
        "mirrored_salmon" : 1
    }
}
"""
testRule = ["bright gray bags contain 2 bright gold bags, 5 dull lavender bags."]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

allBagDict = {}
for rule in inputFile:
    # first bag
    bagSplit = rule.split("bag")
    firstBag = bagSplit[0][:-1].replace(' ','_')
    bagTypes, bagNumbers= [],[]
    for number in numbers:
        for split in bagSplit[1:]:
            if split.count(number)> 0 :
                bagType = split.split(number)[1][1:-1].replace(' ','_')
                bagTypes.append(bagType)
                bagNumbers.append(number)
    allBagDict[firstBag] = {k:v for k,v in zip(bagTypes, bagNumbers)}

def findInstancesOfBag(findBag = None):
    hasBag = []
    for key in allBagDict:
        bagDict = allBagDict[key]
        for bag in bagDict:
            if findBag in bag:
                hasBag.append(key)
    
    return hasBag

bagsThatHaveShiny = findInstancesOfBag(findBag= "shiny_gold")
moreBags = []
for bag in bagsThatHaveShiny:
    print(bag)
    ret = True
    while ret:
        ret = findInstancesOfBag(findBag = bag)
        moreBags.extend(ret)

print(len(set(moreBags)) + len(set(bagsThatHaveShiny)))










