from functools import reduce

# open up input list
inputFile = open(r"C:\Users\asyaa\Documents\adventOfCode\inputLists\day3Input.txt", "r")
inputRow = []

# get 2d array size
columns = 0
rows  = 0
for entry in inputFile:
    inputRow.append(entry.split('\n')[0])

    if columns < len(entry.split('\n')[0]):
        columns = len(entry.split('\n')[0])

    rows += 1
    
# initialize two dimensional array
print("Number of rows {0}, number of columns {1}" .format(rows, columns))

#geologyArray = [[0 for x in range(rows)] for y in range(columns + 1)]
geologyArray = [[0]*columns]*rows 

# converting input into array
for row, rowInput in enumerate(inputRow):  
    geologyArray[row] = rowInput * 500

# traverse down the slope
treesList = []
t1, t2, t3, t4, t5 = (1, 1), (3, 1), (5, 1), (7, 1), (1, 2)

def findTrees(rightInc, downInc):
    right, down= 0, 0
    numberOfTrees = 0
    while down < rows - 1:
        right += rightInc
        down += downInc

        charFound = geologyArray[down][right] 
        
        if charFound == '#':
            numberOfTrees += 1
    
    print("Total number of trees is {0}" .format(numberOfTrees))
    return numberOfTrees

for traversal in [t1, t2, t3, t4, t5]:
    numberOfTrees = findTrees(*traversal)
    treesList.append(numberOfTrees)

print('Trees list is {0}' .format(treesList))
print('Trees mult is {0}' .format(reduce((lambda x, y: x * y), treesList)))




