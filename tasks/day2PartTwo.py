# open up input list
inputFile = open(r"C:\Users\asyaa\Documents\adventOfCode\inputLists\day2Input.txt", "r")
inputList = []

validPasswordsCount = 0

for entry in inputFile:
    policy = entry.split(':')[0]
    password = ((entry.split(':')[1]).split('\n')[0]).strip()
    
    print(" === Password is {0}, policy is {1}" .format(password, policy))

    keyLetter = policy[-1]
    upperLowerBounds = policy[:-1]

    secondPosition = int(upperLowerBounds.split('-')[1]) 
    firstPosition = int(upperLowerBounds.split('-')[0]) 

    # does the key letter exist?
    if keyLetter in password:
        print('This key letter {0} exists in password {1}' .format(keyLetter, password))

        firstPos, secondPos = 0, 0
        # does the key letter exist in either position?
        if len(password)  >= firstPosition:
            if password[firstPosition - 1] == keyLetter:
                print('Key letter {0} exists in first position of {1}' .format(keyLetter, firstPosition))
                firstPos = 1
        if len(password) >= secondPosition:
            if password[secondPosition - 1] == keyLetter:
                print('Key letter {0} exists in second position of {1}' .format(keyLetter, secondPosition))
                secondPos = 1

        if firstPos + secondPos > 0 and firstPos + secondPos <2:
            print("Success! This password is valid.")
            validPasswordsCount += 1

        else:
            print('The key letter is in neither positions of {0} or {1}, or in both.' .format(firstPosition, secondPosition))
    else:
        print('This key letter {0} does not exist in password {1}' .format(keyLetter, password))
        
print("The number of valid passwords are {0}" .format(validPasswordsCount))

