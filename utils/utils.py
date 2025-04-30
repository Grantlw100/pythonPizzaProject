import threading
import time

#######################################################################################################################################################################################################
#
#               # UTILITIES
#   # This is the main entry point for the Freddies Pizzeria Console Ordering application.
#
#######################################################################################################################################################################################################



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
    consoleRequest += yesOrNo
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
_/\\~v~/\__`-._#%&O#&%_.-'   
` |\F/|`- \ `-."".-'
  |.| |    \ /`./      WE
  |.| |  \  `  /    HOPE YOU 
  |.| |   \   / ENJOY YOUR ORDER
-----------------------------------
Thank you for ordering at Freddies!
{new_order}
"""
