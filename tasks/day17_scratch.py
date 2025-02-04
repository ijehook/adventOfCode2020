import os
from typing import OrderedDict 

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

def createLayers(puzzleInputList):

	# iterate through the layers
	matrix = [ [0]* len(puzzleInputList[0]) for i in range(len(puzzleInputList)) ]

	rowNum = len(puzzleInputList[0])
	colNum = len(puzzleInputList)
	
	for y in range(colNum):
		for x in range(rowNum):

			#print(x, y)
			originalListItem = puzzleInputList[x][y]
			if originalListItem == "#":
				matrix[x][y] = 1
			else:
				matrix[x][y] = 0

	print(matrix)

def getNeighbours(x, y):

	index = [x, y, z]



def run():
	""" 
	"""

	puzzleInputList = start()
	print(puzzleInputList)

	createLayers(puzzleInputList)
	
run()