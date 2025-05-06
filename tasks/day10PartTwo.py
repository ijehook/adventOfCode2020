
# puzzleInput = r"D:\adventOfCode2020\inputLists\day10InputSmall.txt"

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
print("TESTING")


class TreeNode(object):
    """ tree node class """
    def __init__(self, root, parent):
    
        self.rootNode = root
        self.children = []
        self.parent = parent

        # add to the list of children any possibility of rules
        options = [root + rule for rule in rules]
        self.children = [child for child in puzzleInputList if child in options]

        if puzzleInputList[-1] in self.children:
            print("!!! The last node has been added.")
            counterList.append(1)
            print("Count is {0}" .format(len(counterList)))

    def get(self):
        print("{0} ---> {1} --> {2}" .format(self.parent, self.rootNode, self.children))

def buildTree():
    # build the python tree
    startNode = TreeNode(root = 0, parent = 0)
    
    print("startNode = {0}" .format(startNode))
    print("startNode.children = {0}" .format(startNode.children))
    print("startNode.rootNode = {0}" .format(startNode.rootNode))

    getTree(startNode)
    
       
        
def getTree(treeNode):
   
    for child in treeNode.children:
        newNode = TreeNode(child, treeNode.rootNode)
        getTree(newNode)


def run():
    """ 

    """

    buildTree()
    print("==== Final ")
    print(len(counterList))
    

   
run()


# we go through the adaptor list, adding them in if there are no extra choices
# if there are a few options, then that's where we branch out
# we save the list we have so far (this is the origin list)
# then we generate new remaining lists from there onwards

# recursive 

