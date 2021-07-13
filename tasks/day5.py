import math

# open up input list
inputFile = open(r"C:\Users\asyaa\Documents\adventOfCode\inputLists\day5Input.txt", "r")

# read the puzzle input
boardingPasses = []
for count, entry in enumerate(inputFile):
    boardingPasses.append(entry.split('\n')[0])

def getSeatId(rowNo, colNo):
    """ get the seat ID from the boarding pass number
    :param str boardingPass: boardingPass to generate unique seat ID from
    :ret: seat ID
    :rtype: int """

    seatID = rowNo * 8 + colNo
    return seatID

def getRowAndSeatNumber(boadingPass):
    """ get row number form boardingPass 
    :param str boardingPass: boardingPass to get row number from
    :ret: row number
    :rtype: int """

    rowInfo = boadingPass[:-3]
    colInfo = boadingPass[-3:]

    # row info
    for count, rowLtr in enumerate(rowInfo):
        if count == 0:
            lower, upper = 0, 128
        section = rowInfo[count]
        upper, lower = rowFind(section, upper, lower)
    
    finalSection = rowInfo[-1]
    if finalSection == "F":
        rowNo = lower
    if finalSection == "B":
        rowNo = upper - 1

    # column info
    for count, colLtr in enumerate(colInfo):
        if count == 0:
            lower, upper = 0, 8
        section = colInfo[count]
        
        upper, lower = rowFind(section, round(upper), round(lower))
        #print("section is {0}, lower: {1}, upper: {2}" .format(section,lower, upper))

    finalSection = colInfo[-1]
    if finalSection == "L":
        colNo = lower 
    if finalSection == "R":
        colNo = upper - 1

    #print("Row number is {0}, column is {1}" .format(rowNo, colNo))
    return rowNo, colNo
    
        
def rowFind(section, upper, lower):
    """ docstring """
    half = (upper + lower) / 2
    if section == "F" or section == "L":
        # lower stays the same, upper changes to half
        lower = lower
        upper = half
   
    if section == "B" or section == "R":
        # upper stays the same, lower changes to half
        lower = half
        upper = upper
    
    #print("Section = {2}, Lower is {0} and upper is {1}" .format(lower, upper, section))
    return upper, lower

test = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
seatIDList = []
for bpass in boardingPasses:
    rowNo, colNo = getRowAndSeatNumber(bpass)
    seatID = getSeatId(rowNo, colNo)
    seatIDList.append(seatID)

seatIDList.sort()
for count, id in enumerate(seatIDList[1:-1]):
   diff = id - seatIDList[count]
   if diff != 1:
    print("diff is {0}" .format(diff))
    print("seat ID before :{0}, seat ID after {1}" .format(id, seatIDList[count]))


