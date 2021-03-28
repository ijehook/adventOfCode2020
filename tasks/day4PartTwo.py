import re

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

#print("Number of passports is {0}" .format(numberOfPassportEntries))
#print("Count of passports is {0}" .format(lineIndent))

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

invalidPassports = []
validPassports = 0
validPassportEntries = []
ValidTerms = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
for passport in passportEntries:
    if all(x in passport for x in ValidTerms):
        validPassports += 1
        validPassportEntries.append(passport)
print("Valid passports are {0}" .format(validPassports))
for p in validPassportEntries:
    print(p)

def byrCheck(passportEntry):
    """ check for birth year regulations """
    # find byr section
    terms = passportEntry.split(' ')
    byrValue= [term.split(':')[1] for term in terms if "byr" in term] or None

    if byrValue:
        byrValue = int(byrValue[0])
    else:
        return False

    if byrValue>=1920 and byrValue <= 2002:
        return True
    else:
        return False

def iyrCheck(passportEntry):
    """ check for issue year regulations """
    # find iyr section
    terms = passportEntry.split(' ')
    iyrValue= [term.split(':')[1] for term in terms if "iyr" in term] or None
    
    if iyrValue:
        if int(iyrValue[0])>=2010 and int(iyrValue[0]) <= 2020:
            return True
        else:
            return False

    else:
        return False

def eyrCheck(passportEntry):
    """ check for expiry year regulations """
    # find byr section
    terms = passportEntry.split(' ')
    eyrValue= [term.split(':')[1] for term in terms if "eyr" in term] or None
    
    if eyrValue:
        eyrValue = int(eyrValue[0])
    else:
        return False

    if eyrValue>=2020 and eyrValue <= 2030:
        return True
    else:
        return False

def hgtCheck(passportEntry):
    """ check for expiry year regulations """
    # find byr section
    terms = passportEntry.split(' ')
    hgtValue= [term.split(':')[1] for term in terms if "hgt" in term] or None

    if hgtValue:
        hgtValue = hgtValue[0]
    else:
        return False

    regex = re.compile('^[0-9]+[a-zA-Z]{2}\Z', re.I)
    match = regex.match(hgtValue)

    if hgtValue[-2:] == 'cm':
        inCentimeters = True
        if int(hgtValue[:-2]) >= 150 and int(hgtValue[:-2]) <= 193:
            return True
        else:
            return False
    

    if hgtValue[-2:] == 'in':
        inInches = True
        if int(hgtValue[:-2]) >= 59 and int(hgtValue[:-2]) <= 76:
            return True
        else:
            return False
    
    return False

def hclCheck(passportEntry):
    """ hair colour check. must start with a # and exactly six character 0-9 or a-f """
    terms = passportEntry.split(' ')
    hclValue= [term.split(':')[1] for term in terms if "hcl" in term] or None

    if hclValue:
        hclValue = hclValue[0]
        regex = re.compile('^#+[0-9a-f]{6}\Z', re.I)
        match = regex.match(hclValue)
        return bool(match)

    else:
        return False

def eclCheck(passportEntry):
    """ valid eye colours are amb blu brn gry grn hzl oth"""
    validEyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    terms = passportEntry.split(' ')
    eclValue= [term.split(':')[1] for term in terms if "ecl" in term] or None

    if eclValue:
        eclValue = eclValue[0]
        if eclValue in validEyes:
            return True
        else:
            return False
    else:
        return False

def pidCheck(passportEntry):
    """ a nine-digit number, including leading zeroes """

    terms = passportEntry.split(' ')
    pidValue= [term.split(':')[1] for term in terms if "pid" in term] or None

    if pidValue:
        pidValue = pidValue[0]
        regex = re.compile('[0-9]{9}\Z', re.I)
        match = regex.match(pidValue)
        return bool(match)
    else:
        return False

newValidPassports = 0
for passport in validPassportEntries:
    
    byrCheckPass = byrCheck(passport)
    iyrCheckPass = iyrCheck(passport)
    eyrCheckPass = eyrCheck(passport)
    hgtCheckPass = hgtCheck(passport)
    hclCheckPass = hclCheck(passport)
    eclCheckPass = eclCheck(passport)
    pidCheckPass = pidCheck(passport)
    print(hgtCheckPass)
    if all([byrCheckPass, iyrCheckPass, eyrCheckPass, hgtCheckPass, hclCheckPass, eclCheckPass, pidCheckPass]):
        newValidPassports += 1

print(newValidPassports)
