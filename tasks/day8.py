# open up input list
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