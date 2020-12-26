# open up input list
inputFile = open(r"C:\Users\asyaa\Documents\adventOfCode\inputLists\day2Input.txt", "r")
inputList = []

validPasswordsCount = 0

for entry in inputFile:
    policy = entry.split(':')[0]
    password = (entry.split(':')[1]).split('\n')[0]
    
    print(" === Password is {0}, policy is {1}" .format(password, policy))

    keyLetter = policy[-1]
    upperLowerBounds = policy[:-1]

    upperLimit = float(upperLowerBounds.split('-')[1])
    lowerLimit = float(upperLowerBounds.split('-')[0])

    # does the key letter exist?
    if keyLetter in password:
        print('This key letter {0} exists in password {1}' .format(keyLetter, password))

        # are the lower and upper bounds respected?
        count = password.count(keyLetter)
        if count >= lowerLimit and count <= upperLimit:
            print('Success! The key letter count is {0}, the policy is {1}-{2}' .format(count, lowerLimit, upperLimit))
            validPasswordsCount += 1
        else:
            print('The key letter count is {0}, the policy is {1}-{2}' .format(count, lowerLimit, upperLimit))
    else:
        print('This key letter {0} does not exist in password {1}' .format(keyLetter, password))
        
print("The number of valid passwords are {0}" .format(validPasswordsCount))

