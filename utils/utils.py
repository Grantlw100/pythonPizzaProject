import threading
import time
import random

#######################################################################################################################################################################################################
#
#               # UTILITIES
#   # This is the main entry point for the Freddies Pizzeria Console Ordering application.
#
#######################################################################################################################################################################################################


input_array =  [ "add Pepperoni to", "add Extra Cheese to", "add a soda to", "add FredSticks to", "add more Freddies Pizzas to", "split", "add delivery or pick-up to"]

beginField = (">"*100)
endField = ("<"*100)
fullField = ("#"*100)
breakField = "\n\n\n"
breakLine = ("-"*100)
testTopBrackt =f"{("\\")*100}\n{("/")*100}"
testBottomBracket =f"{("/")*100}\n{("\\")*100}"
orderTopBracket = f"{">"*100}\n{">"*100}"
orderBottomBracket = f"{"<"*100}\n{"<"*100}"

topField = fullField + "\n" + beginField
bottomField = endField + "\n" + fullField + "\n"



size_list = ["S","M","L"]
yesOrNo = "Please enter \"Y\" for yes and \"N\" for no.\n"
option_list = ["Y","N"]
break_line = "\n"+("-"*80)
new_order = ("#"*120)
testArray = [["S", "M", "L"], ["Y", "N"]]

def errorMessage(value):
    break_line = "\n"+("-"*80)
    print(f"\nINVALID INPUT: {value}\nPLEASE TRY AGAIN\n")
    print(break_line)


def inputPizzaMessage(value):
    break_line = "\n"+("-"*80)
    returnString = f"\nWould you like to {value} your order?"
    return returnString


def inputPizzaSize():
    size_list = ["S","M","L"]

    value = ""
    break_line = "\n"+("-"*80)
    print(break_line)
    while True:
        try:
            value = input("What size pizza suits your appetite? \nPlease enter a size for your Freddies' Pizza.\nOptions include:\nS for Small, M for Medium, and L for Large.\n").strip().upper()
            while value not in size_list:
                errorMessage(value)   
                value = input("What size pizza suits your appetite? \nPlease enter a size for your Freddies' Pizza.\nOptions include:\nS for Small, M for Medium, and L for Large.\n").strip().upper()
                print(value)
            return value
        except (EOFError, UnboundLocalError, TypeError) as e:
            print(f"\nInvalid input {e} Please try again.")
            continue
        
def inputYesOrNo(message):
    value = ""
    yesOrNo = "Please enter \"Y\" for yes and \"N\" for no.\n"
    option_list = ["Y","N"]
    break_line = "\n"+("-"*80)
    print(break_line)

    inputPizzaMessage = message+yesOrNo
    while True:
        try:
            value = input(message+yesOrNo).strip().upper()
            while value not in option_list:
                errorMessage(value)
                value = input(message+yesOrNo).strip().upper()
            return value
        except (EOFError, UnboundLocalError, TypeError) as e:
            errorMessage(e)
            continue


def inputPizzaYesOrNo(message):
    value = ""
    yesOrNo = "Please enter \"Y\" for yes and \"N\" for no.\n"
    consoleRequest = inputPizzaMessage(message)
    consoleRequest += f"\n{yesOrNo}"
    option_list = ["Y","N"]
    break_line = "\n"+("-"*80)
    print(break_line)

    while True:
        try:
            value = input(consoleRequest).strip().upper()
            while value not in option_list:
                errorMessage(value)
                value = input(consoleRequest).strip().upper()
            return value
        except (EOFError, UnboundLocalError, TypeError) as e:
            errorMessage(e)
            continue
        

def inputSplits():
    split_order = inputPizzaYesOrNo("split")
    break_line = "\n"+("-"*100)
    print(break_line)
    if split_order == "Y":
        value = input("\nHow many ways would you like to split this order? (MAX 5 WAYS)\n")
        while not value.isdigit() or 5 >= int(value) <= 0:
            errorMessage(value)
            print(break_line)
            value = input("\nHow many ways would you like to split this order with a maximum of 5?")
        if value == 0:
            value =1
    else: 
        value = 1
    return int(value)

def inputInt(message):
    break_line = "\n"+("-"*100)
    print(break_line)
    while True:
        try:
            value = int(input(message).strip())
        except (ValueError, EOFError, UnboundLocalError, TypeError) as e:
            errorMessage(e)
            continue
        return int(value)


def inputFloat(message):
    break_line = "\n"+("-"*100)
    print(break_line)
    while True:
        try:
            value = float(input(message).strip())
            return value
        except (ValueError, EOFError, UnboundLocalError, TypeError) as e:
            errorMessage(e)
            continue



def calculateGratuity(subtotal):
    break_line = "\n"+("-"*80)
    tipAmount = 0

    getFloatMessage = "Please enter a tip as a dollar amount ($5) or ($5.50) or as a decimal for a percentage (.03 = 3%)"
    tipAmount = inputFloat(getFloatMessage)
    # If the gratuity was a flat amount add it to the total
        
    # calculate and add gratuity rate
    if tipAmount >= 1:
        return tipAmount
    elif tipAmount <= .15:
        return subtotal * .15
    else:
        tipAmount = tipAmount * subtotal
        return  round(tipAmount, 2)
            


def delayed_print(message, delay):
    """Prints a message to the console after a specified delay."""
    time.sleep(delay)
    print("\n"+("*"*120))
    print(message)
    print(("*"*120)+"\n")

def start_delayed_message(message, delay):
  """Starts a thread to print a message after a delay."""
  thread = threading.Thread(target=delayed_print, args=(message, delay))
  thread.daemon = True  # Allow the program to exit even if the thread is running
  thread.start()


  
# print Freddies' Welcome Message (See end for more nnotes)
pizza_intro =f"""
\n  
{new_order}
Welcome to                     ._
                              ,(  `-.
    Freddies                ,': `.   `.
        Pizza Ordering    ,` *   `-.   \\
            Console App ,'  ` :+  = `.  `.
                       ,~  (o):  .,   `.  `.
                     ,'  ; :   ,(__) x;`.  ;
                   ,'  :'  itz  ;  ; ; _,-'
                 .'O ; = _' C ; ;'_,_ ;
               ,;  _;   ` : ;'_,-'   i'
             ,` `;(_)  0 ; ','       :
           .';6     ; ' ,-'~
         ,' Q  ,& ;',-.'
       ,( :` ; _,-'~  ;
     ,~.`c _','
   .';^_,-' ~       WHERE...
 ,'_;-''                IF IT AIN'T FRESH
,,~                        IT AIN'T FREDDIES
                    

Order a Large pizza Freddies' way for a $5 discount! 
        (with extra cheese and pepperoni)
{new_order}
"""

pizza_outro = f"""
\n
{new_order}
     IF IT AINT FRESH                   
UuUuUuUuU   IT AINT ... 
mm O  O |    _______    
m ___~*~|.-''#O&#o%#``-.   
 \\\\__/ /((%& FREDDIES %&))  
_/\\~v~/\\__`-._#%&O#&%_.-'   
` |\\F/|`- \\ `-."".-'
  |.| |    \\ /`./      WE
  |.| |  \\  `  /    HOPE YOU 
  |.| |   \\   / ENJOY YOUR ORDER
-----------------------------------
Thank you for ordering at Freddies!
{new_order}
"""

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
            
