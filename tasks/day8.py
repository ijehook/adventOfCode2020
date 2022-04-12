# open up input list
inputFile = open(r"D:\adventOfCode2020\inputLists\day8Input.txt", "r")

# read the puzzle input
instList = []
for count, entry in enumerate(inputFile):
    instList.append((entry.split('\n')[0], count))

accumulatorList = []
def acc(value):
    """ append the given value into the accumulator list pot
    :param int value: number to appen into pot
    """
    accumulatorList.append(value)


def runCode(lineNo):
    """ exectue the given line number instruction from the puzzle input
    :param int lineNo: line number to execute from the puzzle input/instList
    :ret: next line number to execute
    :rtype: int
    """
    instruction = instList[lineNo]
    cmd = instruction[0]

    print(" == EXEC ==")
    print("{0}: {1}" .format(lineNo, cmd))

    operation = cmd[:3]
    arg = cmd.split(" ")[1]


    if operation == "nop":
        nextLine = lineNo + 1

    if operation == "acc":
        acc(int(arg))
        nextLine = lineNo + 1

    if operation == "jmp":
        nextLine = lineNo + int(arg)
        
    print("Returning {0}" .format(nextLine))
    return nextLine


def calculateAccumulator():
    totalAcc = sum(accumulatorList)
    print("Total accumulator is {0}" .format(totalAcc))
    
calculateAccumulator()

tallyDict= {x[1]:0 for x in instList}

def run(lineNo):
    """"""
    print("Line number is {0}" .format(lineNo))
    tallyDict[lineNo] = tallyDict[lineNo] + 1
    if tallyDict[lineNo] == 2:
        print(" THIS COMMAND HAS BEEN EXECUTED TWICE")
        calculateAccumulator()
        raise RuntimeError()

    newCounter = runCode(lineNo)

    return newCounter

counter = 0
for inst in instList:
    print("Counter is {0}" .format(counter))
    counter = run(counter)


for k in tallyDict:
    print("{0}:{1}" .format(k, tallyDict[k]))



