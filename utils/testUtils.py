from .utils import errorMessage
import random



def generateBackupChance(inputArray):
    wrongChoiceArray = ["S", "M", "L", "Y", "N", "s", "m", "l", "1", "return", "continue", " ", "^c", "^q", "&", "0"]
    inputFromChance = ""
    
    if random.randint(1, 3) == 3 and inputArray[0] == "S":
        integer = random.randint(0, 2)
        inputFromChance = inputArray[integer]
        integer = 0
    elif random.randint(1, 3) == 3 and inputArray[0] == "Y":
        integer = random.randint(0, 1)
        inputFromChance = inputArray[integer]
        integer = 0
    else:
        inputFromChance = wrongChoiceArray[random.randint(0, len(wrongChoiceArray)-1)]
    print(f"INPUT VALUE: \"{inputFromChance}\"")
    return inputFromChance


def generateRightChance(inputArray):
    inputFromChance = ""
    if inputArray[0] == "S":
        integer = random.randint(0, 2)
        inputFromChance = inputArray[integer]
        integer = 0
    elif inputArray[0] == "Y":
        integer = random.randint(0, 1)
        inputFromChance = inputArray[integer]
        integer = 0
    returnValue = inputFromChance
    print(f"\nINPUT VALUE: \"{inputFromChance}\"\n")
    inputFromChance = ""
    return returnValue



def generateChance(inputArray):
    wrongChoiceArray = [KeyboardInterrupt, EOFError, UnboundLocalError, TypeError, "g", "\\", "%", "?", "s", "^c", "^q", "l", "return", "continue","x", "", None]
    randomInt = random.randint(1, 3)
    print("GENERATING WRONG TEST INPUT")
    inputFromChance = ""
    
    if randomInt == 3 and inputArray[0] == "S":
        integer = random.randint(0, 2)
        inputFromChance = inputArray[integer]
        integer = 0
    elif randomInt == 3 and inputArray[0] == "Y":
        integer = random.randint(0, 1)
        inputFromChance = inputArray[integer]
        integer = 0
    else:
        inputFromChance = wrongChoiceArray[random.randint(0, len(wrongChoiceArray)-1)]
    randomInt = 0
    returnValue = inputFromChance
    print(f"\nINPUT VALUE: \"{inputFromChance}\"\n")
    inputFromChance = ""
    return returnValue



def generateTestInputs(testArray, testType):
    print(f"\nGENERATING TEST INPUTS FROM INPUT ARRAY: {testArray}")
    value = ""
    option_list = ["Y","N"]
    pizza_list = ["S", "M", "L"]
    break_line = "\n"+("-"*80)
    endLoop = False
    print(break_line)
    while endLoop == False:
        if testType == "wrong" and testArray[0] == "Y":
            try:
                value = generateChance(testArray)
                while value not in option_list:
                    errorMessage(value)
                    value = generateChance(testArray)
                return value
            except (KeyboardInterrupt, EOFError, UnboundLocalError, TypeError) as e:
                print("\nInvalid input. Please try again.")
                continue
        elif testType == "wrong" and testArray[0] == "S":
            try:
                value = generateChance(testArray)
                while value not in pizza_list:
                    errorMessage(value)
                    value = generateChance(testArray)
                return value
            except (KeyboardInterrupt, EOFError, UnboundLocalError, TypeError) as e:
                print("\nInvalid input. Please try again.")
                continue
        elif testType == "right" and testArray[0] == "Y":
            try:
                value = generateRightChance(testArray)
                while value not in option_list:
                    errorMessage(value)
                    value = generateRightChance(testArray)
                return value
            except (KeyboardInterrupt, EOFError, UnboundLocalError, TypeError) as e:
                print("\nInvalid input. Please try again.")
                continue
        elif testType == "right" and testArray[0] == "S":
            try:
                value = generateRightChance(testArray)
                while value not in pizza_list:
                    errorMessage(value)
                    value = generateRightChance(testArray)
                return value
            except (KeyboardInterrupt, EOFError, UnboundLocalError, TypeError) as e:
                print("\nInvalid input. Please try again.")
                continue
            
