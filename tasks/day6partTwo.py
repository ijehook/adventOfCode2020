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
    # find the number of groups
    # combine all group into one string
    # duplicate a sort set
    # count the occurences from each item in the set against the combined
    # string, if any are the same number of the group members, then increment
    grpMembers = len(groupList)
    stringSet = set(''.join(groupList))
    stringComb= ''.join(groupList)
    cnt = 0
    for q in stringSet:
        print("checking for {0} in {1}" .format(q, stringComb))
        no = stringComb.count(q)
        if no == grpMembers:
            cnt +=1 
    
    return cnt

allGroupCount = 0
for grp in groupInput:
    cnt = count(grp)
    allGroupCount += cnt
print(allGroupCount)





