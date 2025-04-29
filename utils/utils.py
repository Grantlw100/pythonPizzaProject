import threading
import time



size_list = ["S","M","L"]
yesOrNo = "Please enter \"Y\" for yes and \"N\" for no.\n"
option_list = ["Y","N"]
break_line = "\n"+("-"*80)
new_order = ("#"*120)
testArray = [["S", "M", "L"], ["Y", "N"]]

def errorMessage(value):
    break_line = "\n"+("-"*80)
    print(f"\nYou entered {value} which was an invalid input. Please try again.\n")
    print(break_line)


def inputMessage(value):
    break_line = "\n"+("-"*80)
    print(break_line)
    print(f"\nWould you like to {value} your order?")



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
        except (KeyboardInterrupt, EOFError, UnboundLocalError, TypeError) as e:
            print("\nInvalid input. Please try again.")
            return None
        
def inputYesOrNo(message):
    value = ""
    yesOrNo = "Please enter \"Y\" for yes and \"N\" for no.\n"
    option_list = ["Y","N"]
    break_line = "\n"+("-"*80)
    print(break_line)
    while True:
        try:
            value = input(message+yesOrNo).strip().upper()
            while value not in option_list:
                errorMessage(value)
                value = input(message+yesOrNo).strip().upper()
            return value
        except (KeyboardInterrupt, EOFError, UnboundLocalError, TypeError) as e:
            print("\nInvalid input. Please try again.")
            return None


def inputSplits():
    split_order = inputYesOrNo("split")
    break_line = "\n"+("-"*100)
    print(break_line)
    if split_order == "Y":
        splits = input("\nHow many ways would you like to split this order? (MAX 5 WAYS)\n")
        while not splits.isdigit() or 5 >= int(splits) <= 0:
            errorMessage(splits)
            print(break_line)
            splits = input("\nHow many ways would you like to split this order with a maximum of 5?")
        if splits == 0:
            splits =1
    else: 
        splits = 1
    return int(splits)

def inputInt():
    break_line = "\n"+("-"*100)
    print(break_line)
    splits = input("\nHow many test would you like to run? (MAX 10 TESTS)\n")
    while not splits.isdigit() or int(splits) >= 10 or int(splits) <= 0:
        errorMessage(splits)
        print(break_line)
        splits = input("\nHow many tests would you like to run???")
    if splits == 0:
        splits =1
    return int(splits)

def calculateGratuity(subtotal):
    break_line = "\n"+("-"*80)
    tip_input = 0.00
    print(break_line)
    while True:
        try:
            tip_input = input("\nEnter the tip as a dollor amount: 1 or 1.00 or 1.0 \n\nOr as a decimal percentage: .15 = 15%, .2 = 20%, 0.25 = 25%.\n")
            while not tip_input.isdigit() or 5 >= int(tip_input) <= 0:
                errorMessage(tip_input)
                print(break_line)
                tip_input = input("\nEnter the tip as a dollor amount: 1 or 1.00 or 1.0 \n\nOr as a decimal percentage: .15 = 15%, .2 = 20%, 0.25 = 25%.\n")
            
        except (KeyboardInterrupt, EOFError, UnboundLocalError, TypeError) as e:
            print("\nInvalid input. Please try again.")
            return None
        # If the gratuity was a flat amount add it to the total
        if tipAmount == "":
            tipAmount = .15;
        else:
            tipAmount = float(tipAmount);
            
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
 \\__/ /((%& FREDDIES %&))  
_/\~v~/\__`-._#%&O#&%_.-'   
` |\F/|`- \ `-."".-'
  |.| |    \ /`./      WE
  |.| |  \  `  /    HOPE YOU 
  |.| |   \   / ENJOY YOUR ORDER
-----------------------------------
Thank you for ordering at Freddies!
{new_order}
"""


