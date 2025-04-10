
# puzzleInput = r"D:\adventOfCode2020\inputLists\day9Input.txt"
puzzleInput = r"C:\Users\asyaa\source\repos\adventOfCode2020\inputLists\day9Input.txt"

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

def findContiguosSet(invalidNumber):
    """ 
    keep going through a puzzleInput[number:number+i] until the sum of that number is bigger than
    the invalid number.
    """
    startIndex = 0
    endIndex = 1
    outcome = 0

    puzzleInputList = start()

    foundSet = False
    while foundSet == False:
        if outcome > invalidNumber:
            startIndex += 1
        if outcome < invalidNumber:
            endIndex += 1
        print("Looking under inputList[{0}:{1}]" .format(startIndex, endIndex))
        outcome = getListIndices(puzzleInputList, startIndex, endIndex)
        print("Outcome is {0}" .format(outcome))
        if outcome == invalidNumber:
            foundSet = True

    print("List indices found.")
    # get all the numbers in that list
    contiguosSet = puzzleInputList[startIndex:endIndex]
    minimum = min(puzzleInputList[startIndex:endIndex])
    maximum = max(puzzleInputList[startIndex:endIndex])
    sum = minimum + maximum

    print("Min is {0}, max is {1}" .format(minimum, maximum))
    print("Sum is {0}" .format(sum))


def getListIndices(list, start, end):
    outcome = sum(list[start:end])
    return outcome





# start with start 0, end 1 for list indices
# if the outcome of the sum is more than the invalid number, add to the start index 
# if the outcome of the sum is less than the invalid number, add to the end index
   


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
        print(preambleStart, preambleLength)

        # check the value against all possible outcomes
        if valueToCheck not in possibleOutcomes:
            print("{0} This value is not in the possible outcome of preamble!" .format(valueToCheck))

            invalidNumber = valueToCheck
            print("Invalid Number is {0}" .format(invalidNumber))
            #return valueToCheck
 
        
    # find a contiguous set of at least two numbers in your list which sum to the invalid number
    findContiguosSet(invalidNumber)


run()

