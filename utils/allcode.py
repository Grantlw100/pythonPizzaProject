#######################################################################################################################################################################################################
#
#               # Freddies Pizzeria Console Application Main
#   # This is the main entry point for the Freddies Pizzeria Console Ordering application.
#
#######################################################################################################################################################################################################


# import receipt generator
import random
from datetime import datetime, date
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
    print(break_line)

    getFloatMessage = "\nHow many test would you like to run? (MAX 10 TESTS)\n"
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


cheese = inputFloat("cheese")
print(cheese)

cheese2 = inputInt("Chees2")
print(cheese2)



#######################################################################################################################################################################################################
#
#               # TEST UTILITIES
#   # This is the main entry point for the Freddies Pizzeria Console Ordering application.
#
#######################################################################################################################################################################################################





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
            


#############################################################################################################################################################
#
#               # Order Generator
#   # This is where the order is created for the rest of the program to use
#
#############################################################################################################################################################



yesOrNo = "Please enter \"Y\" for yes and \"N\" for no.\n"
option_list = ["Y","N"]
break_line = "\n"+("-"*80)
input_array =  [ "add Pepperoni to", "add Extra Cheese to", "add a soda to", "add FredSticks to", "add more Freddies Pizzas to", "add delivery or pick-up to",]


def errorMessage(value):
    try:
        print(f"\nYou entered {value} which was an invalid input. Please try again.\n")
    except (ValueError, EOFError, UnboundLocalError, TypeError) as e:
        print(f"An error occurred: {e}. Please try again.")


def inputMessage(value):
    print(break_line)
    print(f"\nWould you like to {value} your order?")


def createPizza():
    pizza_string = ""
    pizza_extra = [0,0]
    pizza_price = 0.00
    topping_pepperoni = ""
    topping_extra_cheese  = ""
    extra_soda  = ""
    extra_breadsticks = ""
    continue_order_valid = ""

    pizza_size = inputPizzaSize()
    topping_pepperoni = inputPizzaYesOrNo(input_array[0])
    topping_extra_cheese  = inputPizzaYesOrNo(input_array[1])
    continue_order_valid = inputPizzaYesOrNo(input_array[4])
    


    # Base Price of Pizza
    if pizza_size == "S":
        pizza_price += 15.00
        pizza_string += pizza_size + " "
    elif pizza_size == "M":
        pizza_price += 20.00
        pizza_string += pizza_size + " "
    elif pizza_size == "L":
        pizza_price += 25.00
        pizza_string = pizza_size + " "
        

    if topping_pepperoni == "Y" and pizza_price >= 20:
        pizza_price += 3.00
        pizza_string += topping_pepperoni + " "
    elif topping_pepperoni == "Y":
        pizza_price += 2.00
        pizza_string += topping_pepperoni + " "
    else:
        pizza_string += topping_pepperoni + " "

    # Add Extra Cheese to Pizza
    if topping_extra_cheese == "Y":
        pizza_price += 1.00
        pizza_string += topping_extra_cheese + ""
    else: 
        pizza_string += topping_extra_cheese + ""

    
    if extra_soda == "Y":
        pizza_price += 2.00
        pizza_extra[0] += 1 

    if extra_breadsticks == "Y":
        pizza_price += 5.00
        pizza_extra[1] += 1

    if pizza_size == "L" and topping_pepperoni == "Y" and topping_extra_cheese == "Y":
        pizza_price = 25.00


    
    if continue_order_valid == "Y":
        continue_order = True
    else:
         continue_order = False
    return pizza_price, pizza_string, continue_order, pizza_extra







def deliverOrder():
    timer = 10
    receiving = "We just received your order and have summoned the great and powerful Freddies to bring your pizza to life"  
    making = "Freddies himself is shakin and bakin your order."  
    baking = "Freddies just popped that baby in the oven."  
    boxing = "Order all boxed up and ready to go!"  
    moving = "WE ARE COMING IN HOT AND FAST!!!"  
    arriving = "ITS HERE ITS HERE YOUR ORDER IS HERE"   
    waiting = "YOUR ORDER IS BIG CHILLIN & WAITING FOR YOU HERE AT FREDDIES"
    receiptOrderItemsDeliveryFee = ""
    
    
    deliver_order = inputPizzaYesOrNo(input_array[5])
        
    # Example usage:
    if deliver_order == "Y":
        receiptOrderItemsDeliveryFee += f"\n\t+ $5.00 delivery fee \n"
        start_delayed_message(receiving, timer)
        start_delayed_message(making, timer*2)
        start_delayed_message(baking, timer*3.5)
        start_delayed_message(boxing, timer*5.0)
        start_delayed_message(moving, timer*6.0)
        start_delayed_message(arriving, timer*7.5)
    else: 
        start_delayed_message(receiving, timer)
        start_delayed_message(making, timer*2.5)
        start_delayed_message(baking, timer*3.5)
        start_delayed_message(waiting, timer*4.5)
    return deliver_order, receiptOrderItemsDeliveryFee



def addExtras():
    soda_count = 0
    stick_count = 0
    extras_value = 0.00

    
    extra_soda  = inputPizzaYesOrNo(input_array[2])
    extra_breadsticks = inputPizzaYesOrNo(input_array[3])


    if extra_soda == "Y":
        soda_count = inputInt("How many sodas would you like to add?")
        extras_value += (soda_count * 2.00)

    if extra_breadsticks == "Y":
        stick_count = inputInt("How many orders of FredSticks would you like to add?")
        extras_value += (stick_count * 5.00)

    return soda_count, stick_count, extras_value






#############################################################################################################################################################
#
#               # RECEIPT Generator
#   # This is where the order is created for the rest of the program to use
#
#############################################################################################################################################################



break_line = ("-"*120)
# create receipt function
def createReceipt(order_name, order_id, order_items, base_price, split_amount):    
    # Calculate paid values
    subtotal = base_price
    tax = round(base_price * 0.07, 2)
    tip = calculateGratuity(subtotal)
    total = round(base_price + tax + tip, 2)
    
    split_bill = ""
    billing = ""
    if( split_amount >= 2):
        split_price = total / float(split_amount)
        billing = f"VISA: XXXX-XXXX-XXXX-{random.randint(1000, 9999)}\n"*split_amount
        split_bill = f"TOTAL SPLIT x{split_amount}:    ${split_price:.2f}"
    else:
        billing += f"VISA: XXXX-XXXX-XXXX-{random.randint(1000, 9999)}"

        

    
    
    
    # Time and date
    today = date.today()
    current_time = datetime.now().time()

    # Generate random IDs
    
    batch = random.randint(10000000, 99999999)
    appr = random.randint(10000000, 99999999)
    if order_items.find("Congrats"):
        Congratulaions = f"\nYou got an extra $5 in savings on your Big Freds' Big Discount Pie!\n"
        
    # Print Dynamic Receipt
    receipt = f"""
{break_line}
    Here is your receipt {order_name}
{break_line}

    If it ain't fresh it ain't...
    Freddies'
           (_)             
     _ __  __ __________ _ 
    | '_ \\| ||_  /_  / _` |
    | |_) | |/ / / / (_| |
    | .__/|_/___/___\\__,_|
    | |                   
    |_|     

    Freddies Pizzeria, 
    1234 Bipple Bopple Way Ct, 
    Glip Glop City, FL, 98765

    SALE 
    {today}       {current_time.isoformat(timespec='seconds')} 
    NAME:            {order_name} 
    ORDER:           {order_id} 
    BATCH:           {batch} 
    APPR:            {appr} 
    {billing}
    Order:
    {order_items}
    SUBTOTAL:          ${base_price:.2f}
    TAX:               ${tax:.2f}
    TIP:               ${tip:.2f}
    TOTAL:             ${total:.2f}
    {split_bill}
    """

    print(receipt + "\n\n" + Congratulaions)
    




def createReceiptItems(order_list, soda_count, bread_stick_count ):
    receiptOrder = ""    
    receiptOrderItemsBS = f" $15.00 \n"
    receiptOrderItemsBM = f" $20.00 \n"
    receiptOrderItemsBL = f" $25.00 \n"
    receiptOrderItemsC = f"\t + $2.00 - Ad Pepp \n\t + $1.00 - sz chrg \n"
    receiptOrderItemsCS = f"\t + $2.00 - Ad Pepp\n"
    receiptOrderItemsD = f"\t + $1.00 - Ex Chss\n"
    receiptOrderItemsE = f"\t - $5.00 - Discount \n"
    receiptOrderItemsF = "\tAdd-ons\n"
    receiptOrderItemsEnd = ""
    if soda_count > 1:
        receiptOrderItemsF += f"\t + $2.00 ad soda x {soda_count}\n"
    elif soda_count == 1:
        receiptOrderItemsF += f"\t + $2.00 ad soda \n"
    if bread_stick_count > 1:
        receiptOrderItemsF += f"\t + $5.00 frdstik x {bread_stick_count}\n"
    elif bread_stick_count == 1:
        receiptOrderItemsF += f"\t + $5.00 frdstik\n"

    if soda_count == 0 and bread_stick_count == 0:
        receiptOrderItemsF = ""

    pizza_list = order_list.split("endOfPizza")
    # create copy of pizza list do not have to tamper with original pizza list
    pizza_list_copy = pizza_list.copy()

    for pizza in set(pizza_list):  # set() ensures we only loop over unique pizzas
        if pizza == "":
            continue

        count = pizza_list_copy.count(pizza)  # count occurrences

        pizza_size = pizza[0]
        receiptOrderItemsA = f"\t{count} X {pizza_size} Pizza "

        match pizza:
            case "S N N":
                receiptOrderItemsEnd  = receiptOrderItemsA + receiptOrderItemsBS
            case "S N Y":
                receiptOrderItemsEnd  = receiptOrderItemsA + receiptOrderItemsBS + receiptOrderItemsD
            case "S Y N":
                receiptOrderItemsEnd  = receiptOrderItemsA + receiptOrderItemsBS + receiptOrderItemsCS
            case "S Y Y":
                receiptOrderItemsEnd  = receiptOrderItemsA + receiptOrderItemsBS + receiptOrderItemsCS + receiptOrderItemsD
            case "M N N":
                receiptOrderItemsEnd  = receiptOrderItemsA + receiptOrderItemsBM 
            case "M N Y":
                receiptOrderItemsEnd  = receiptOrderItemsA + receiptOrderItemsBM + receiptOrderItemsD
            case "M Y N":
                receiptOrderItemsEnd  = receiptOrderItemsA + receiptOrderItemsBM + receiptOrderItemsC
            case "M Y Y":
                receiptOrderItemsEnd  = receiptOrderItemsA + receiptOrderItemsBM + receiptOrderItemsC + receiptOrderItemsD
            case "L N N":
                receiptOrderItemsEnd  = receiptOrderItemsA + receiptOrderItemsBL
            case "L N Y":
                receiptOrderItemsEnd  = receiptOrderItemsA + receiptOrderItemsBL + receiptOrderItemsD
            case "L Y N":
                receiptOrderItemsEnd  = receiptOrderItemsA + receiptOrderItemsBL + receiptOrderItemsC
            case "L Y Y":
                receiptOrderItemsEnd  = receiptOrderItemsA + receiptOrderItemsBL + receiptOrderItemsC + receiptOrderItemsD + receiptOrderItemsE
            case _:
                receiptOrder  =""
        receiptOrder += receiptOrderItemsEnd
        receiptOrder
        
    return receiptOrder + receiptOrderItemsF



#############################################################################################################################################################
#
#               # FREDDIES TEST 
#   # This is where the order is created for the rest of the program to use
#
#############################################################################################################################################################




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





def runFreddiesTest(number, testType):
    base_price = 0.00
    order_number = 1
    pizza_list = []
    order_list = ""
    continue_order = True
    order_again = ""
    endProgram = False
    receiptOrderItems = ""
    receiptOrderItemsDeliveryFee = " "


    #     createPizza
    #     delliverOrde
    print(breakField)
    print(testTopBrackt)
    print(f"\t\t\t\tBEGIN TEST NUMBER: {number + 1}")
    print(testBottomBracket)
    print(breakField)
    while endProgram == False:
        j = 0
        print(orderTopBracket)
        print(F"\t\t\t\tTEST NUMBER: {number + 1} BEGIN ORDER NUMBER:{order_number}")
        print(orderBottomBracket)

        while continue_order == True:
            print(breakField)
                #would you like to double the last order exactly as it was written? 
            # if Y - validate, set order_amount to 2, double price, createReceiptOrder,
            print(f" {"NEWPIZZA "*11}")
            print(beginField)
            print(f"\t\t\t\t-----PIZZA NUMBER: [ {(len(pizza_list)+1)} ]-----")
            print(endField)
            print(f" {"NEWPIZZA "*11}")
            print("\n")
            pizza_price, pizza_string, continue_order, order_again = createPizzaTest(testArray[1], testType)
            print(topField)
            print("CREATE ORDER COMPLETE")
            print(endField)
            print(f"\nPIZZA PRICE: {pizza_price} PIZZA STRING: {pizza_string} CONTINUE ORDER:{continue_order} ORDER AGAIN :{order_again}\n")
            print(fullField)
            print("\n")
            pizza_list.append(pizza_string)
            base_price +=pizza_price
        order_list = "endOfPizza".join(pizza_list)
        soda_count, breadstick_count, extra_value = addExtrasTest(testArray[1], testType)
        base_price+= extra_value
        delivery_option, receiptOrderItemsDeliveryFee = deliverOrderTest(testArray[1], testType)
        receiptOrderItems = createReceiptItems(order_list, soda_count, breadstick_count)
        print(topField)
        print("CREATING RECEIPT ITEMS USING PIZZA LIST")
        print(endField)
        print(f"\n{pizza_list}\n")
        print(fullField)
        print("\n")

        # Calculate paid values
        subtotal = base_price
        tax = round(base_price * 0.07, 2)
        tip = calculateGratuityTest(subtotal)
        total = round(base_price + tax + tip, 2)
        breakLine = "-"*100

        results = f"""
{breakLine}
        ____ORDER ITEMS____ 
        \n
{receiptOrderItems + receiptOrderItemsDeliveryFee}
        
{breakLine}
        ORDER NUMBER:           {order_number}
{breakLine}
        ORDER DELIVERY:         {True if delivery_option == "Y" else False}
{breakLine}
        ORDER BEFORE TAXES:     {subtotal: .2f}
{breakLine}
        ORDER TAXES:            {tax: .2f}
{breakLine}
        ORDER TIP:              {tip: .2f}
{breakLine}
        ORDER TOTAL:            {total: .2f}
{breakLine}"""
        
        print(orderTopBracket)
        print(f"\t\t\t\tTEST NUMBER: {number + 1} ORDER NUMBER: {order_number} RESULTS")
        print(results+"\n")
        print(orderBottomBracket)
        print(breakField)

        
        print(orderTopBracket)
        print(f"\t\t\t\tTEST NUMBER: {number + 1} END ORDER NUMBER: {order_number}")
        print(orderBottomBracket)
        print(breakField)
            
        if order_again == "Y":

            order_number+=1
            base_price = 0
            pizza_list = []
            order_list = ""
            receiptOrderItems = ""
            continue_order = True
            continue
        else:
            endProgram = True
            print(testBottomBracket)
            print("*"*100)
            print(f"\t\t\t\tEND TEST NUMBER: {number+1}")
            print("*"*100)
            print(testTopBrackt)

            exit
            


def createPizzaTest(testArray, testType):
    pizza_string = ""
    pizza_price = 0.00

    print(topField)
    print("TEST PIZZA SIZE")
    print(endField)
    pizza_size = generateTestInputs(["S", "M", "L"], testType)
    print(fullField)
    print("\n")

    print(topField)
    print("TEST ADDING PEPPERONI")
    print(endField)
    topping_pepperoni = generateTestInputs(testArray, testType)
    print(fullField)
    print("\n")

    print(topField)
    print("TEST ADDING CHEESE")
    print(endField)
    topping_extra_cheese = generateTestInputs(testArray, testType)
    print(fullField)
    print("\n")
       
    print(topField)
    print("TEST CONTINUE ORDER")
    print(endField)
    continue_order_valid = generateTestInputs(testArray, testType)
    print(fullField)
    print("\n")

    print(topField)
    print("TEST ADD NEW ORDER")
    print(endField)
    order_again = generateTestInputs(testArray, testType)
    print(fullField)
    print("\n")



    # Base Price of Pizza
    if pizza_size == "S":
        pizza_price += 15.00
    elif pizza_size == "M":
        pizza_price += 20.00
    elif pizza_size == "L":
        pizza_price += 25.00
    pizza_string += pizza_size + " "

    if topping_pepperoni == "Y" and pizza_price >= 20:
        pizza_price += 3.00
    elif topping_pepperoni == "Y":
        pizza_price += 2.00
    pizza_string += topping_pepperoni + " "



    # Add Extra Cheese to Pizza
    if topping_extra_cheese == "Y":
        pizza_price += 1.00
    pizza_string += topping_extra_cheese + ""

    
    if pizza_size == "L" and topping_pepperoni == "Y" and topping_extra_cheese == "Y":
        pizza_price = 25.00


    if continue_order_valid == "Y":
        continue_order = True
        return pizza_price, pizza_string, continue_order, order_again

    elif continue_order_valid == "N":
         continue_order = False
         return pizza_price, pizza_string, continue_order, order_again




def deliverOrderTest(testArray, testType):
    receiptOrderItemsDeliveryFee = " "
    print(topField)
    print("TEST ADD ORDER DELIVERY")
    print(endField)
    deliver_order = generateTestInputs(testArray, testType)
    print(fullField)
    print("\n")
        
    # Example usage:
    if deliver_order == "Y":
        receiptOrderItemsDeliveryFee += f"\n\t+ $5.00 delivery fee \n"
        
    elif deliver_order == "N": 
        receiptOrderItemsDeliveryFee += f"\n\tNO DELIVERY FEE"
    return deliver_order, receiptOrderItemsDeliveryFee

def addExtrasTest(testArray, testType):
    soda_count = 0
    stick_count = 0
    soda_value = 0.00
    stick_value = 0.00
    extra_value = 0.00

    print(topField)
    print("TEST ADDING SODA")
    print(endField)
    extra_soda = generateTestInputs(testArray, testType)
    if extra_soda == "Y":
        print(breakLine)
        soda_count = random.randint(0,10) 
        soda_value = (2.00*float(soda_count))
        print(f"SODAS ORDERED:      {soda_count}    VALUE: {soda_value}")
        extra_value += soda_value
    print(fullField)
    print("\n")
    
    
    print(topField)
    print("TEST ADDING FREDSTICKS")
    print(endField)
    extra_breadsticks = generateTestInputs(testArray, testType)
    if extra_breadsticks == "Y":
        print(breakLine)
        stick_count = random.randint(0,10) 
        stick_value +=( 5.00 * float(stick_count))
        print(f"FREDSTICKS ORDERED: {stick_count}    VALUE: {stick_value}")
        extra_value += stick_value
    print(fullField)
    print("\n")



    return soda_count, stick_count, extra_value


def calculateGratuityTest(subtotal):    
    tipAmount = (random.randint(1,10)/10)
    subtotal *= tipAmount
    print(topField)
    print("TEST DELIVER ORDER")
    print(endField)
    print(f"\nORDER TIP PERCENTAGE: {tipAmount*100}%")
    print(f"\n{breakLine}\n")
    print(f"ORDER TIP AMOUNT: {subtotal: .2f}\n")
    print(fullField)
    print("\n")
    return subtotal
    
#############################################################################################################################################################
#
#               # FREDDIES WEEK 4 TEST 
#   # This is where the order is created for the rest of the program to use
#
#############################################################################################################################################################
breakline = "-"*100



def generateRightOrders(number):
    #price of all of the pizzas total
    total_price = 0.00
    orders = 0
    pizza_string = ""
    print("#"*100)
    print(f"\t\t\t\tBEGIN TEST NUMBER:{number + 1}")
    print(">"*100)
    # Loop that creates the multiple orders
    while True:
        base_price = 0.00
        orders +=1
        print (f"This is pizza # {orders}.")
        print(">"*100)
        
    # Ask customer to choose the size of their pizza 
        print(breakline)
        print("Test Pizza Size")
        pizza_size = generateRightChance(testArray[0])
        while pizza_size.upper() not in ("S", "M", "L"):
            print("Invalid input. Please enter S, M, or L. \n")
            pizza_size = generateRightChance(testArray[0])
        pizza_string += pizza_size
        print("\n")
        if pizza_size.upper() == "S":
            base_price += 15.00
        elif pizza_size.upper() == "M":
            base_price += 20.00
        elif pizza_size.upper() == "L":
            base_price += 25.00
        
    # Ask customer if they want pepperoni #
        print(breakline)
        print("Test Adding Pepperoni")
        topping_pepperoni = generateRightChance(testArray[1])
        while topping_pepperoni.upper() not in ("Y", "N"):
            print("Invalid input. Please enter Y or N")
            topping_pepperoni = generateRightChance(testArray[1])
        pizza_string += topping_pepperoni

        print("\n")
        if topping_pepperoni == "Y":
            if pizza_size.upper() == "S":
                base_price += 2.00
            if pizza_size.upper() == "M":
                base_price += 3.00
            if pizza_size.upper() == "L":
                base_price +=3.00
            elif topping_pepperoni.upper() == "N":
                base_price += 0.00
    
    # Ask customer if they want extra cheese #
        print(breakline)
        print("Test Adding Cheese")
        topping_extra_cheese = generateRightChance(testArray[1])
        while topping_extra_cheese.upper() not in ("Y", "N"):   
            print("Invalid input. Please enter Y or N")
            topping_extra_cheese = generateRightChance(testArray[1])
        pizza_string += topping_extra_cheese

        print("\n")
        if topping_extra_cheese.upper() == "Y":
            base_price += 1.00
        elif topping_extra_cheese.upper() == "N":
            base_price += 0.00
        
    # If the customers orders a Large Pizza with pepperoni and extra cheese they get a $5 discount.
        if pizza_size.upper() == "L" and topping_pepperoni == "Y" and topping_extra_cheese == "Y":
            print ("Congratulations! You've earned a $5 discount on your order.")
            base_price -= 5.00
        
    # Add base price to total order
        total_price += base_price
        
        print (f"Your total is ${total_price:.2f} at this time.")
        
    # Ask if they want to order another pizza BEFORE showing total
        print(breakline)
        print("Test Adding more pizzas")
        another = generateRightChance(testArray[1])
        while another not in ("Y", "N"):
            another = generateRightChance(testArray[1])
        pizza_string += another
        print(f"\nPIZZA STRING IS :{pizza_string}\n")
        print("\n")
    # Exit the pizza-adding loop    
        if another == "N":
            break  

    # Final Bill
    if orders > 1:
        print(f"You have {orders} pizzas in your order.")
    if orders == 1:
        print(f"You have {orders} pizza in your order.")
    print(f"Thank you for choosing Python Pizza Deliveries, your final bill is ${total_price:.2f}")
    print("<"*100)
    print(f"\t\t\t\tEND TEST NUMBER:{number+1}")
    print(("<"*100)+"\n\n\n\n")



breakLine = "-"*100

def generateOrders(number):
    #price of all of the pizzas total
    total_price = 0.00
    orders = 0
    print("#"*100)
    print(f"\t\t\t\tBEGIN TEST NUMBER:{number + 1}")
    print(">"*100)
    # Loop that creates the multiple orders
    while True:
        base_price = 0.00
        orders +=1
        print (f"This is pizza # {orders}.")
        print(">"*100)
        
    # Ask customer to choose the size of their pizza 
        print(breakline)
        print("Test Pizza Size")
        pizza_size = generateChance(testArray[0])
        while pizza_size.upper() not in ("S", "M", "L"):
            print("Invalid input. Please enter S, M, or L. \n")
            pizza_size = generateChance(testArray[0])
        
        if pizza_size.upper() == "S":
            base_price += 15.00
        elif pizza_size.upper() == "M":
            base_price += 20.00
        elif pizza_size.upper() == "L":
            base_price += 25.00
        
    # Ask customer if they want pepperoni #
        print(breakline)
        print("Test Adding Pepperoni")
        topping_pepperoni = generateChance(testArray[1])
        while topping_pepperoni.upper() not in ("Y", "N"):
            print("Invalid input. Please enter Y or N")
            topping_pepperoni = generateChance(testArray[1])
            
        if topping_pepperoni == "Y":
            if pizza_size.upper() == "S":
                base_price += 2.00
            if pizza_size.upper() == "M":
                base_price += 3.00
            if pizza_size.upper() == "L":
                base_price +=3.00
            elif topping_pepperoni.upper() == "N":
                base_price += 0.00
    
    # Ask customer if they want extra cheese #
        print(breakline)
        print("Test Adding Cheese")
        topping_extra_cheese = generateChance(testArray[1])
        while topping_extra_cheese.upper() not in ("Y", "N"):   
            print("Invalid input. Please enter Y or N")
            topping_extra_cheese = generateChance(testArray[1])
            
        if topping_extra_cheese.upper() == "Y":
            base_price += 1.00
        elif topping_extra_cheese.upper() == "N":
            base_price += 0.00
        
    # If the customers orders a Large Pizza with pepperoni and extra cheese they get a $5 discount.
        if pizza_size.upper() == "L" and topping_pepperoni == "Y" and topping_extra_cheese == "Y":
            print ("Congratulations! You've earned a $5 discount on your order.")
            base_price -= 5.00
        
    # Add base price to total order
        total_price += base_price
        
        print (f"Your total is ${total_price:.2f} at this time.")
        
    # Ask if they want to order another pizza BEFORE showing total
        print(breakline)
        print("Test Adding more pizzas")
        another = generateChance(testArray[1])
        while another not in ("Y", "N"):
            another = generateChance(testArray[1])
            
    # Exit the pizza-adding loop    
        if another == "N":
            break  

    # Final Bill
    if orders > 1:
        print(f"You have {orders} pizzas in your order.")
    if orders == 1:
        print(f"You have {orders} pizza in your order.")
    print(f"Thank you for choosing Python Pizza Deliveries, your final bill is ${total_price:.2f}")
    print("<"*100)
    print(f"\t\t\t\tEND TEST NUMBER:{number+1}")
    print(("<"*100)+"\n\n\n\n")


def runWeek4WrongTest():
    input = inputYesOrNo("Would you like to run tests with PROPER inputs?")
    if input == "Y":
        testsToRun = inputInt()
        print(topField)
        print("@"*100)
        print("\t\t\t\tBEGIN TESTS")
        print("@"*100)
        print(bottomField)
        number = 0
        while number < testsToRun:
            try:
                value = generateOrders(number)
            except (KeyboardInterrupt, EOFError, AttributeError, UnboundLocalError, TypeError) as e:
                print("-- ERROR --"*10)
                print(f"\n\t\t\tTHIS INPUT BROKE THE SYSTEM:\n\t\t\t\t\t\"{value}\"\n")
                print("<"*100)
                print(f"\t\t\t\tEND TEST NUMBER:{number+1}")
                print(("<"*100)+"\n\n\n\n")
            number+=1

    
    



def RunWeek4RightTest():
    input = inputYesOrNo("Would you like to run tests with PROPER inputs?")
    if input == "Y":
        testsToRun = inputInt()
        print(topField)
        print("@"*100)
        print("\t\t\t\tBEGIN TESTS")
        print("@"*100)
        print(bottomField)
        number = 0
        while number < testsToRun:
            value = ""
        try:
            value = generateRightOrders(number)
        except (KeyboardInterrupt, EOFError, AttributeError, UnboundLocalError, TypeError) as e:
            print("-- ERROR --"*10)
            print(f"\n\t\t\tTHIS INPUT BROKE THE SYSTEM:\n\t\t\t\t\t\"{e}\"\n")
            print("-- ERROR --"*10)    
            print("\n\n\n")
        number+=1
    

    

    

#############################################################################################################################################################
#
#               # FREDDIES WEEK 5 TEST 
#   # This is where the order is created for the rest of the program to use
#
#############################################################################################################################################################


def week5Test():
    print(breakLine)
    input = inputYesOrNo("Would you like to run tests with PROPER inputs?")
    print(breakLine)
    if input == "Y":
        testsToRun = inputInt("How many tests would you like to run?")
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
            except (KeyboardInterrupt, EOFError, AttributeError, UnboundLocalError, TypeError) as e:
                print(orderTopBracket)
                print(f"\t\t\t\tTEST NUMBER: {number + 1} \t\tEND LAST ORDER")
                print(orderBottomBracket)
                print("--ERROR--"*11)
                print(f"\n\t\t\tTHIS INPUT BROKE THE SYSTEM:\t\t\t\t\t\"{value}\"\n")
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

    print(breakLine)
    input = inputYesOrNo("Would you like to run tests with IMPROPER inputs?")
    print(breakLine)
    if input == "Y":
        testsToRun = inputInt("How many tests would you like to run?")
        number = 0
        while number < testsToRun:
            value = 0
            try:
                value = runFreddiesTest(number, "wrong")
            except (KeyboardInterrupt, EOFError, AttributeError, UnboundLocalError, TypeError) as e:
                print(orderTopBracket)
                print(f"\t\t\t\tTEST NUMBER: {number + 1} \t\tEND LAST ORDER")
                print(orderBottomBracket)
                print("-- ERROR --"*10)
                print(f"\n\t\t\tTHIS INPUT BROKE THE SYSTEM:\n\t\t\t\t\t\"{value}\"\n")
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


    
######################################################################################################################################################################################################

              # Freddies Pizzeria Console Application Main
  # This is the main entry point for the Freddies Pizzeria Console Ordering application.

######################################################################################################################################################################################################

    


def FreddiesPizzaApplication():
    print(breakLine)
    runTest = inputYesOrNo("Would you like to run tests for Freddies Week 5 Code?")
    print(breakLine)
    if runTest == "Y":
        week5Test()
    # initialize base values and comparison lists
    break_line = ("-"*80)
    new_order = ("#"*120)

    base_price = 0.00
    _id = random.randint(1, 999)
    order_number = 1
    order_id = order_number + _id

    order_name = ""
    order_list = ""
    continue_order = True
    order_again = ""
    endProgram = False
    receiptOrderItems = ""
    receiptOrderItemsDeliveryFee = " "

    # incorporate pizza_extra into pizza list
    pizza_list = []





    print(pizza_intro)
    # base_price, pizza_string, continue_order = createPizza()
    while not endProgram:
        try: 
            while continue_order:
            
                    if (order_name == ""):
                        print(break_line)
                        order_name = input("\nPlease enter a name for the order?\n")
                    #would you like to double the last order exactly as it was written? 
                    # if Y - validate, set order_amount to 2, double price, createReceiptOrder,
                    pizza_price, pizza_string, continue_order, pizza_extra = createPizza()
                    pizza_list.append(pizza_string)
                    base_price +=pizza_price
            order_list = "endOfPizza".join(pizza_list)
            splits = inputSplits()
            soda_count, breadstick_count, extras_value = addExtras()
            delivery_option, receiptOrderItemsDeliveryFee = deliverOrder()
            receiptOrderItems = createReceiptItems(order_list, soda_count, breadstick_count)
            createReceipt(order_name, order_number + order_id, receiptOrderItems + receiptOrderItemsDeliveryFee, base_price + extras_value, splits)

            if delivery_option == "Y":
                print(f"THANK YOU FOR ORDERING WITH FREDDIES {order_name}!!! \nWe are working AS FAST AS HUMANLY POSSIBLE to get your pizza to you. \nIf it ain't there in 30 minutes, we are sorry :(")
            else:
                print(f"THANK YOU FOR ORDERING WITH FREDDIES {order_name}!!! \nWe are baking AS FAST AS HUMANLY POSSIBLE so your order is ready when you arrive. \nIf it ain't ready in 15 minutes, we are sorry :(")

        except (KeyboardInterrupt) as e:
            print("\nQuitting current order.")
                        
        

        order_again = inputYesOrNo(f"\nIf you would like to add a seperate order please enter \"Y\" otherwise enter \"N\" to end the program\n")
        
        if order_again == "Y":
            base_price = 0
            breadstick_count = 0
            soda_count= 0
            pizza_list = []
            order_name = ""
            order_list = ""
            receiptOrderItems = ""
            receiptOrderItemsDeliveryFee = ""
            continue_order = True
            order_number+=1
            order_id +=1
            print(new_order)
            print(pizza_intro)
            continue
        else:
            endProgram = True
            print(pizza_outro)
            exit


FreddiesPizzaApplication()



