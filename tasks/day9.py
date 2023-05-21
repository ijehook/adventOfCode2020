from opcode import hasjabs


puzzleInput = r"D:\adventOfCode2020\inputLists\day9Input.txt"

def start():
    # open up input list
    inputFile = open(puzzleInput, "r")

    # read the puzzle input
    puzzleInputList = []
    for entry in inputFile:
        puzzleInputList.append(int((entry.split('\n')[0])))

    return puzzleInputList


def calculateAllSumOutcomes(listOfNumbers=[]):
    """ generate a list of all possible sum outcomes from given list of numbers
    
    :param list[int] listOfNumbers: list of numbers to generate outcomes from
    :ret: list of possible outcomes
    :rtype: list[int] 
    """

    listOfOutcomes = []

    for number in listOfNumbers:
        newList = [num for num in listOfNumbers]
        newList.remove(number)
        
        for num in newList:
            val = number +  num

            # numbers in pair must be different
            if number == num:
                continue
            
            # calculate the sum
            if val not in listOfOutcomes:
                listOfOutcomes.append(val)

    return listOfOutcomes


def run(preambleLength=25):
    """ find the first number entry that does not follow the XMAS convention
    
    :param int preambleLength: the preamble length
    :ret: the first number entry that does not follow the XMAS convention
    :rtype: int

    """

    # run a function for each number entry (from after the preamble length)
    # calculate all possible outcomes form previous numbers of preamble 
    # compare the number entry against list of all possible outcomes

    puzzleInputList = start()
    
    # get the preamble array 
    # start= 5, preambleList = [0:5]
    # start = 6, preambleList = [1:6]
    # start = 7, preambleList = [2:7]

    counter = preambleLength
    for counter in range(counter, len(puzzleInputList)):
        valueToCheck = puzzleInputList[counter]
    
        preambleStart = counter - preambleLength
        preambleEnd = counter 
        preambleList = puzzleInputList[preambleStart:preambleEnd]
        possibleOutcomes = calculateAllSumOutcomes(preambleList)

        # check the value against all possible outcomes
        if valueToCheck not in possibleOutcomes:
            print("{0} This value is not in the possible outcome of preamble!" .format(valueToCheck))
            return valueToCheck


run()
