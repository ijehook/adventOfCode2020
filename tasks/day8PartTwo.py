puzzleInput = r"D:\adventOfCode2020\inputLists\day8Input.txt"
def start():
    # open up input list
    inputFile = open(puzzleInput, "r")

    # read the puzzle input
    instList = []
    for count, entry in enumerate(inputFile):
        instList.append((entry.split('\n')[0], count))

    return instList

class ProcessList(object):
    """ """

    def __init__(self, list):
        self.list = list
        self.accumulatorList = []
        self.tallyDict= {x[1]:0 for x in list}

    def acc(self, value):
        """ append the given value into the accumulator list pot
        :param int value: number to appen into pot
        """
        self.accumulatorList.append(value)

    def calculateAccumulator(self):
        totalAcc = sum(self.accumulatorList)
        print("Total accumulator is {0}" .format(totalAcc))

    def runCode(self, lineNo):
        """ exectue the given line number instruction from the puzzle input
        :param int lineNo: line number to execute from the puzzle input/instList
        :ret: next line number to execute
        :rtype: int
        """
        instruction = self.list[lineNo]
        cmd = instruction[0]

        #print(" == EXEC ==")
        #print("{0}: {1}" .format(lineNo, cmd))

        operation = cmd[:3]
        arg = cmd.split(" ")[1]

        if operation == "nop":
            nextLine = lineNo + 1

        if operation == "acc":
            self.acc(int(arg))
            nextLine = lineNo + 1

        if operation == "jmp":
            nextLine = lineNo + int(arg)
            
        #print("Returning {0}" .format(nextLine))
        return nextLine

    def run(self, lineNo):
        """ """   
        self.tallyDict[lineNo] = self.tallyDict[lineNo] + 1
        
        if self.tallyDict[lineNo] == 2:
            #print(" THIS COMMAND HAS BEEN EXECUTED TWICE")
            #self.calculateAccumulator()
            try:
                raise RuntimeError()
            except Exception as e:
                pass

        newCounter = self.runCode(lineNo)
        if newCounter == len(self.list):
            print("!!! This is the final instruction being run!!!")
            self.calculateAccumulator()
            raise RuntimeError
        return newCounter

    def process(self):
        counter = 0
        for inst in self.list:
            if counter == len(self.list) - 1:
                print("Last instruction being run")
                
            counter = self.run(counter)

def createLists(originalList):
    # (lineNumber, 0) for every instruction in orinal list
    tallyAmmendDict= {x[1]:0 for x in originalList}

    listOfLists = []
    for inst in originalList:
        newInstList = []
        inputFile = open(puzzleInput, "r")
        for count, entry in enumerate(inputFile):
            newInstList.append((entry.split('\n')[0], count))
        
        # has this instruction been changed before?
        cmd = inst[0]
        instNo = inst[1]
        changeCount = tallyAmmendDict[instNo]
        if changeCount:
            continue
        
        # change the instruction, if possible 
        operation = cmd[:3]
        arg = cmd.split(" ")[1]

        if operation == "nop":
            newInst = cmd.replace("nop", "jmp")

        if operation == "acc":
            newInst = cmd
            continue

        if operation == "jmp":
            newInst = cmd.replace("jmp", "nop")

        # increment changeCount
        tallyAmmendDict[instNo] = 1
        
        # swap out the old instruction for the new one and append it into the newInstList
        newInstList[instNo] = (newInst, instNo)
        
        listOfLists.append(newInstList)

    return listOfLists

def runLists(listOfLists):
    # go through all the lists
    
    for count, list in enumerate(listOfLists):
        print("Going through {0} list" .format(count))
        listObject = ProcessList(list)
        result = listObject.process()
        

originalList = start()
listOfLists = createLists(originalList)
runLists(listOfLists)




