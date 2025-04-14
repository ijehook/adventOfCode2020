import os 

print(os.getcwd())

puzzleInput = r"{0}\inputLists\day17Input.txt" .format(str(os.getcwd()))

def start():
	# open up input list
	inputFile = open(puzzleInput, "r")

	# read the puzzle input
	puzzleInputList = []
	for entry in inputFile:
		puzzleInputList.append(str((entry.split('\n')[0])))

	return puzzleInputList


def getNeighbours(row, col, inputList, prevList, nextList):
	# gonna store a list of 2-deminsional matrixes 
	# eg [ [001],
	#      [100],
	#      [001], ...]
	
	# get the neighbours
	"""
	sideVals = [inputList[row][col+1], inputList[row][col-1]]
	downVals = [inputList[row+1][col-1], inputList[row+1][col], inputList[row+1][col+1]]
	upVals = [inputList[row-1][col-1], inputList[row-1][col], inputList[row-1][col+1]]

	prevSideVals = [prevList[row][col+1], prevList[row][col], prevList[row][col-1]]
	prevDownVals = [prevList[row+1][col-1], prevList[row+1][col], prevList[row+1][col+1]]
	prevUpVals = [prevList[row-1][col-1], prevList[row-1][col], prevList[row-1][col+1]]

	nextSideVals = [nextList[row][col+1], nextList[row][col], nextList[row][col-1]]
	nextDownVals = [nextList[row+1][col-1], nextList[row+1][col], nextList[row+1][col+1]]
	nextUpVals = [nextList[row-1][col-1], nextList[row-1][col], nextList[row-1][col+1]]
	"""
	# all sides
	leftSide = []
	centerSide = []
	rightSide = []

	# left side
	leftSideMain = []
	leftSideUp = []
	leftSideDown = []
	
	if col-1 != -1:
		leftSideMain = [inputList[row][col-1], inputList[row+1][col-1], inputList[row-1][col-1]]
		leftSideUp = [prevList[row][col-1], prevList[row+1][col-1], prevList[row-1][col-1]]
		leftSideDown = [nextList[row][col-1], nextList[row+1][col-1], nextList[row-1][col-1]]
		
	leftSide = leftSideMain + leftSideDown + leftSideUp

	neighboursList = leftSide + centerSide + rightSide
	
	active = 0
	inactive = 0
	print("Looking at {0}" .format(inputList[row][col]))
	
	if inputList[row][col] == "#":
		active = 1
	else:
		inactive = 1

	result = "#"
	if active:
		if neighboursList.count("#") == 2 or neighboursList.count("#") ==3:
			result = "#"
		else:
			result = "."

	if inactive:
		if neighboursList.count("#") == 3:
			result = "#"
		else:
			result = "."
	print("The result is {0}" .format(result))
	return result

def initPrevList(inputList):
	colLen = len(inputList[0])
	prevList = []
	for row in inputList:
		rowString = ""
		for col in range(colLen):
			val = "."
			rowString += val
		prevList.append(rowString)

	return prevList        

	#print(prevList)

def run():
	""" 
	"""

	puzzleInputList = start()
	print(puzzleInputList)
	
	prevList = initPrevList(puzzleInputList)
	nextList = initPrevList(puzzleInputList)

	print("The previous list is {0}" .format(prevList))
	print("The current list is {0}" .format(puzzleInputList))
	print("The next list is {0}" .format(nextList))

	z = 0
	for z in range(1):
		print("i is {0}" .format(z))
		rowLen = len(puzzleInputList)
		colLen = len(puzzleInputList[0])

		newList = []
		for row in range(rowLen):
			rowRes = ""
			for col in range(colLen):
				print("Row :{0}, Col: {1}" .format(row, col))
				print("Puzzle list is {0}" .format(puzzleInputList[row][col]))
				res = getNeighbours(row, col, puzzleInputList,  prevList, nextList)   
				rowRes += res
			newList.append(rowRes)
		print(newList)


	
run()
