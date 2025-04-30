from utils.Utils import inputYesOrNo, inputInt
from utils.TestFunctions import runFreddiesTest, topField, bottomField, testBottomBracket, testTopBrackt, orderBottomBracket, orderTopBracket

def week5Test():
    input = inputYesOrNo("Would you like to run tests with PROPER inputs?")
    if input == "Y":
        inputMessage = "\nHow many test would you like to run? (MAX 10 TESTS)\n\nHow many tests would you like to run???"
        testsToRun = inputInt(inputMessage)
        print(topField)
        print("@"*100)
        print("\t\t\t\tBEGIN TESTS")
        print("@"*100)
        print(bottomField)
        number = 0
        while number < testsToRun:
            value = ""
            try:
                value = runFreddiesTest(number, "right")
            except (EOFError, AttributeError, UnboundLocalError, TypeError) as e:
                print(orderTopBracket)
                print(f"\t\t\t\tTEST NUMBER: {number + 1} \t\tEND LAST ORDER")
                print(orderBottomBracket)
                print("--ERROR--"*11)
                print(f"\n\t\t\tTHIS INPUT BROKE THE SYSTEM:\t\t\t\t\t\"{e}\"\n")
                print("--ERROR--"*11)
                print(testBottomBracket)
                print(f"\t\t\t\tEND TEST NUMBER: {number+1}: FAILED")
                print(testBottomBracket)
            number+=1
        print(topField)
        print("@"*100)
        print("END PROPER INPUT TESTS")
        print("@"*100)
        print(bottomField)

    input = inputYesOrNo("Would you like to run tests with IMPROPER inputs?")
    if input == "Y":
        inputMessage = "\nHow many test would you like to run? (MAX 10 TESTS)\n\nHow many tests would you like to run???"
        testsToRun = inputInt(inputMessage)
        number = 0
        while number < testsToRun:
            value = 0
            try:
                value = runFreddiesTest(number, "wrong")
            except (EOFError, AttributeError, UnboundLocalError, TypeError) as e:
                print(orderTopBracket)
                print(f"\t\t\t\tTEST NUMBER: {number + 1} \t\tEND LAST ORDER")
                print(orderBottomBracket)
                print("-- ERROR --"*10)
                print(f"\n\t\t\tTHIS INPUT BROKE THE SYSTEM:\n\t\t\t\t\t\"{e}\"\n")
                print(testBottomBracket)
                print(testTopBrackt)
                print(f"\t\t\t\tEND TEST NUMBER: {number+1}")
                print(testTopBrackt+"\n\n\n\n")
                print(testBottomBracket)
            number+=1
        print(topField)
        print("@"*100)
        print("END IMPROPER INPUT TESTS")
        print("@"*100)
        print(bottomField)

    print(" :) "*25)
    print("\t\t\t\t\tHave a good day!")
    print(" :) "*25)
