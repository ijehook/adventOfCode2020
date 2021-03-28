# open up input list
inputFile = open(r"C:\Users\asyaa\Documents\adventOfCode\inputLists\day4Input.txt", "r")

# make a dictionary for every entry 
passportDict = {
    "byr" : None,
    "iyr" : None,
    "eyr" : None,
    "hgt" : None,
    "ecl" : None,
    "pid" : None,
    "cid" : None
}

attrList = ['byr', 'iyr', 'eyr', 'hgt', 'ecl', 'pid']
# split all passport entries by the blank line
passportEntries, passportEntriesRaw = [], []

# count the number of '' in input list
numberOfPassportEntries = 0
lineIndent = [-1]

for count, entry in enumerate(inputFile):
    passportEntriesRaw.append(entry.split('\n')[0])
    if entry == '\n':
        numberOfPassportEntries += 1
        lineIndent.append(count)
lineIndent.append(len(passportEntriesRaw))

numberOfPassportEntries += 1

print("Number of passports is {0}" .format(numberOfPassportEntries))
print("Count of passports is {0}" .format(lineIndent))

# store list in between spaces
passportEntries = []

def storeInBetweenSpaces(start, end, list = passportEntriesRaw):
    entry = ''
    for index in range(start + 1 , end):
        entry += ' ' + passportEntriesRaw[index]
    
    passportEntries.append(entry)

for count, start in enumerate(lineIndent):
    if start != lineIndent[-1]:
        storeInBetweenSpaces(start, lineIndent[count + 1])

# find the number of valid passports 
invalidPassports = []
# for passport in passportEntries:
#     for attr in attrList:
#         if attr not in passport:
#             print('Attr {0} is missing from {1}' .format(attr, passport))
#             invalidPassports.append(passport)

validPassports = 0
ValidTerms = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
for passport in passportEntries:
    if all(x in passport for x in ValidTerms):
        validPassports += 1

numberOfInvalidPassports = len(set(invalidPassports))

for passport in set(invalidPassports):
    passportEntries.remove(passport)

#print("Number of valid passports are {0}" .format(numberOfValidPassports))

for passport in passportEntries:
    print(passport)

print(validPassports)