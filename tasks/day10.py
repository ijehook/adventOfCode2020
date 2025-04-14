
# puzzleInput = r"D:\adventOfCode2020\inputLists\day10Input.txt"
puzzleInput = r"C:\Users\asyaa\source\repos\adventOfCode2020\inputLists\day10Input.txt"

def start():
    # open up input list
    inputFile = open(puzzleInput, "r")

    # read the puzzle input
    puzzleInputList = []
    for entry in inputFile:
        puzzleInputList.append(int((entry.split('\n')[0])))

    return puzzleInputList


def run():
    """ 

    """

    # sort the adapters
    puzzleInputList = set(sorted(start()))
    
    # accepted differences
    rules = [1, 2, 3]
    differenceList = []

    #go through each adapter in the list. add in to the used adaptor list, if it passes the rules 
    outputJolt = 0
    for adaptor in puzzleInputList:
        # find the difference between the adaptor and the output jolt
        difference = float(adaptor) - float(outputJolt)
        print("Difference is {0}" .format(difference))
        if difference not in rules:
            continue
        
        differenceList.append(difference)
        outputJolt += difference
    # appending the final difference for the device
    differenceList.append(3)

    # number of 1 and 3 jolt differences
    oneJoltDifferences = differenceList.count(1)
    threeJoltDifferences = differenceList.count(3)

    answer = oneJoltDifferences * threeJoltDifferences
    print("The answer is {0}" .format(answer))
run()


