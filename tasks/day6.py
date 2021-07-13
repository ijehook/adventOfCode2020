import math

# open up input list
inputFile = open(r"C:\Users\asyaa\Documents\adventOfCode\inputLists\day6Input.txt", "r")

# read the puzzle input
groupInput = []
groupBuffer = []
for count, entry in enumerate(inputFile): 
    if entry == "\n":
        groupInput.append(groupBuffer)
        groupBuffer = []
    else:
        groupBuffer.append(entry.split('\n')[0])
groupInput.append(groupBuffer)   

def count(groupList):
    # count all from group 
    # combine all group into one string
    # sort/set it 
    string = ''.join(set(''.join(groupList)))
    cnt = len(string)
    return cnt

allGroupCount = 0
for grp in groupInput:
    cnt = count(grp)
    allGroupCount += cnt
print(allGroupCount)





