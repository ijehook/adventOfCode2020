
# puzzleInput = r"D:\adventOfCode2020\inputLists\day10InputSmall.txt"

from itertools import count


puzzleInput = r"C:\Users\asyaa\source\repos\adventOfCode2020\inputLists\day10Input.txt"

def start():
    # open up input list
    inputFile = open(puzzleInput, "r")

    # read the puzzle input
    puzzleInputList = []
    for entry in inputFile:
        puzzleInputList.append(int((entry.split('\n')[0])))

    return puzzleInputList

rules = [1, 2, 3]
puzzleInputList = [float(x) for x in set(sorted(start()))]
counterList = []
countDict={0.0:1}

class TreeNode(object):
    """ tree node class """
    def __init__(self, root, parent):
    
        self.rootNode = float(root)
        self.children = []
        self.parent = parent

        # add to the list of children any possibility of rules
        options = [root + rule for rule in rules]
        self.children = [child for child in puzzleInputList if child in options]

        print("{0} has {1} options: {2}" .format(self.rootNode, len(self.children),self.children))
        # countDict[str(root)]=len(self.children)
        if self.rootNode == 0:
            return
        countDict[self.rootNode]= countDict.get(self.rootNode -1, 0) + countDict.get(self.rootNode -2, 0) + countDict.get(self.rootNode -3, 0)
        print("countDict[{0}] : {1}" .format(self.rootNode,countDict[self.rootNode] ))
        #if puzzleInputList[-1] in self.children:
        if self.rootNode == puzzleInputList[-1]:
            print("!!! The last node has been added.")
            counterList.append(1)
            print("Count is {0}" .format(len(counterList)))
            

    def get(self):
        print("{0} ---> {1} --> {2}" .format(self.parent, self.rootNode, self.children))

def buildTree():
    # build the python tree
    startNode = TreeNode(root = 0.0, parent = 0)

    getTree(startNode)
    
       
        
def getTree(treeNode):
   
    for child in treeNode.children:
        print("looking at node {0}" .format(child))
        newNode = TreeNode(child, treeNode.rootNode)
     
        if counterList:
           return
           #pass
        getTree(newNode)

def run():
    """ 

    """

    buildTree()
    print("==== Final ")

    for x in countDict:
        #print(x + ":" + countDict[x])
        pass
    print(countDict[float(puzzleInputList[-1])])

        
    

   
run()


# we go through the adaptor list, adding them in if there are no extra choices
# if there are a few options, then that's where we branch out
# we save the list we have so far (this is the origin list)
# then we generate new remaining lists from there onwards

# recursive 


# part 2
# find how many steps it takes to get from one number to the next
#
