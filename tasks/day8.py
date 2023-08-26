# open up input list
<<<<<<< HEAD
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



=======
inputFile = open(r"C:\Users\asyaa\Documents\adventOfCode\inputLists\day8Input.txt", "r")

# read the puzzle input
instructions = {}
for count, entry in enumerate(inputFile):
    instructions[count] = entry.split('\n')[0]

accValue = 0
def acc(value):
    """ just adds to the accumulator pot, return new accumulator value"""
    print("Acc current value is {0}" .format(accValue))
    #accValue += value

def noOperation():
    """ does nothing """

    pass

# go through the list
insCount = {i:0 for i in range(len(instructions))}

def executeInstruction(lineNumber):
    """ execute the line number 
    return the next one to execute
    """
    print("Executing line number {0}" .format(lineNumber))
    instruction = instructions[lineNumber]
    
    print("ACC VALUE IS {0}" .format(accValue))

    operator = instruction[:3]
    print("operator is {0}" .format(operator))

    if operator == "nop":
        nextLineToExecute = lineNumber + 1
    
    if operator in ["acc", "jmp"]:
        operatorValue = instruction.split(" ")[1]

    if operator == "acc":
        print(operatorValue)
        acc(operatorValue)
        nextLineToExecute = lineNumber + 1
    
    if operator == "jmp":
        nextLineToExecute += operatorValue

    return nextLineToExecute

newLineNumber = 0
def runInstructions(lineNumber=0):
    """ run instructions and stop if one instruction is executed more than once """
    print("Running instruction line number {0}" .format(lineNumber))
    if not lineNumber:
        lineNumber = 0

    instCounter = insCount[lineNumber] + 1
    while instCounter < 2:
        newLineNumber = executeInstruction(lineNumber)
        runInstructions(newLineNumber)

runInstructions()
>>>>>>> caddeddf2d83b5a0024fb68108368ba00f466a1b
