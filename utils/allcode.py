#######################################################################################################################################################################################################
#
#               # Freddies Pizzeria Console Application Main
#   # This is the main entry point for the Freddies Pizzeria Console Ordering application.
#
#######################################################################################################################################################################################################


# import receipt generator
import random
from datetime import datetime, date
import random

# initialize base values and comparison lists
size_list = ["S","M","L"]
option_list = ["Y","N"]

base_price = 0.00
order_id = random.randint(1, 999)
order_number = 1
order_name = ""
pizza_list = []
continue_order = True
final_order = ""
endProgram = False

split_total = "N"
split_amount = 1



# print Freddies' Welcome Message (See end for more nnotes)
print("\nWelcome to Freddies' Console Pizza Ordering Service where \n\n\"If it ain't fresh it ain't Freddies'\"\n\n")

print("Order a Large pizza Freddies' way for a $5 discount (with extra cheese and pepperoni)\n\n")

# base_price, pizza_string, continue_order = createOrder()
while endProgram == False:
    while continue_order == True:
        if (order_name == ""):
            order_name = input("\nPlease enter a name for the order?\n")
        #would you like to double the last order exactly as it was written? 
        # if Y - validate, set order_amount to 2, double price, createReceiptOrder,
        
        yesOrNo = "\nPlease enter \"Y\" for yes and \"N\" for no.\n"

        size_list = ["S","M","L"]
        option_list = ["Y","N"]
        pizza_string = ""
        pizza_price = 0.00
        continue_order_valid = ""

        # else create the receipt order_items

        # after completing the order, if receiptOrderItems.find(newReceiptOrderItems) > -1  change order_amount on that order to 2

        # Error Handling
        pizza_size = input("\nWhat size pizza suits your appetite? \nPlease enter a size for your Freddies' Pizza.\nOptions include:\nS for Small, M for Medium, and L for Large.\n").strip().upper()
        while pizza_size not in size_list:
            pizza_size = input(f"You entered {pizza_size} which is an invalid value. Please try again. \nPlease enter a size for your Freddies' Pizza.\nOptions include:\nS for Small, M for Medium, and L for Large.\n").strip().upper()

        topping_pepperoni = input("\nWould you like pepperoni? "+ yesOrNo).strip().upper()
        while topping_pepperoni not in option_list:
            topping_pepperoni = input(f"You entered {topping_pepperoni} which is an invalid input. Please try again." + yesOrNo).strip().upper()

        topping_extra_cheese  = input ("\nWould you like extra cheese?" + yesOrNo).strip().upper()
        while topping_extra_cheese not in option_list:
            topping_extra_cheese = input(f"You entered {topping_pepperoni} which is an invalid input. Please try again." + yesOrNo).strip().upper()



        # Base Price of Pizza
        if pizza_size == "S":
            pizza_price += 15.00
            pizza_string += pizza_size + " "
        elif pizza_size == "M":
            pizza_price += 20.00
            pizza_string += pizza_size + " "
        elif pizza_size == "L":
            pizza_price += 25.00
            pizza_string += pizza_size + " "
            

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


        if pizza_size == "L" and topping_pepperoni == "Y" and topping_extra_cheese == "Y":
            pizza_price = 25.00

        pizza_list.append(pizza_string)
        base_price += pizza_price

        continue_order_valid = input(f"\nWould you like to add onto this order?"+yesOrNo).strip().upper()
        while continue_order_valid not in option_list:
            continue_order_valid = input(f"You entered {continue_order_valid} which is an invalid input. Please try again. \nPlease enter Y to add Pepperonis to your pizza or N if you do not.\n").strip().upper()

        if continue_order_valid == "Y":
            continue_order = True;
        else:
            continue_order = False

    pizza_list_string = "endOfPizza".join(pizza_list)
    
    receiptOrder = ""    
    receiptOrderItemsBS = f" $15.00 \n"
    receiptOrderItemsBM = f" $20.00 \n"
    receiptOrderItemsBL = f" $25.00 \n"
    receiptOrderItemsC = f"\t + $2.00 - Ad Pepp \n\t + $1.00 - sz chrg \n"
    receiptOrderItemsCS = f"\t + $2.00 - Ad Pepp\n"
    receiptOrderItemsD = f"\t + $1.00 - Ex Chss\n"
    receiptOrderItemsE = f"\t - $5.00 - Discount \n"
    pizza_list_items = pizza_list_string.split("endOfPizza")
    print(pizza_list_items)
    # create copy of pizza list do not have to tamper with original pizza list
    pizza_list_copy = pizza_list_items.copy()

    for pizza in set(pizza_list_items):  # set() ensures we only loop over unique pizzas
        if pizza == "":
            continue

        count = pizza_list_copy.count(pizza)  # count occurrences

        pizza_size = pizza[0]
        receiptOrderItemsA = f"{count} X {pizza_size} Pizza "

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
            case "S Y Y":
                receiptOrderItemsEnd  = receiptOrderItemsA + receiptOrderItemsBM + receiptOrderItemsC + receiptOrderItemsD
            case "L N N":
                receiptOrderItemsEnd  = receiptOrderItemsA + receiptOrderItemsBL
            case "L N Y":
                receiptOrderItemsEnd  = receiptOrderItemsA + receiptOrderItemsBL + receiptOrderItemsD
            case "S Y N":
                receiptOrderItemsEnd  = receiptOrderItemsA + receiptOrderItemsBL + receiptOrderItemsC
            case "L Y Y":
                receiptOrderItemsEnd  = receiptOrderItemsA + receiptOrderItemsBL + receiptOrderItemsC + receiptOrderItemsD + receiptOrderItemsE
            case _:
                receiptOrder  =""
        receiptOrder+=receiptOrderItemsEnd
    receiptOrder
    tip_input = input("\nEnter the tip as a dollor amount: \n\n1 or 1.00 or 1.0 \n\nOr as a decimal percentage: \n\n.15 = 15%, .2 = 20%, 0.25 = 25%.\n")

    # Calculate paid values
    subtotal = base_price
    tax = round(base_price * 0.07, 2)
    if tip_input == "":
        tip_input = .15 * subtotal;
    else:
        tip_input = float(tip_input);
        
    # calculate and add gratuity rate
    if tip_input >= 1:
        tip_input
    elif tip_input <= .15:
        subtotal * .15
    else:
        tip_input = tip_input * subtotal
        round(tip_input, 2)
    total = round(base_price + tax + tip_input, 2)
    
    
    split_bill = ""
    billing = ""
    if(split_total == "Y"):
        split_price = total / float(split_amount)
        i = 0
        while(i < split_amount):
            billing += f"VISA: XXXX-XXXX-XXXX-{random.randint(1000, 9999)}"
            ++i
        split_bill = f"\t{total} split {split_amount} = {split_price:.2f} per"
    else:
        billing += f"VISA: XXXX-XXXX-XXXX-{random.randint(1000, 9999)}"

        

    
    
    
    # Time and date
    today = date.today()
    current_time = datetime.now().time()

    # Generate random IDs
    
    batch = random.randint(10000000, 99999999)
    appr = random.randint(10000000, 99999999)
    if receiptOrder.find("Congrats"):
        Congratulaions = f"\nYou got an extra $5 in savings on your Big Freds' Big Discount Pie!\n"
        
    # Print Dynamic Receipt
    receipt = f"""

    If it ain't fresh it ain't...
    Freddies'
           (_)             
     _ __  __ __________ _ 
    | '_ \\| ||_  /_  / _` |
    | |_) | |/ / / / (_| |
    | .__/|_/___/___\\__,_|
    | |                   
    |_|     

    Freddies Pizza, 
    1234 Bipple Bopple Way Ct, 
    Glip Glop City, FL, 98765-4321

    SALE 
    {today}       {current_time.isoformat(timespec='seconds')} 
    NAME:            {order_name} 
    ORDER:           {order_id} 
    BATCH:           {batch} 
    APPR:            {appr} 
    {billing}

    Order:
    {receiptOrder}

    SUBTOTAL:          ${base_price:.2f}
    TAX:               ${tax:.2f}
    TIP:               ${tip_input:.2f}
    TOTAL:             ${total:.2f}
    {split_bill}
    """
    exitMessage = f"Thank You for your Freddies' order {order_name}! \n Here is your receipt."

    print(receipt + "\n\n" + exitMessage + Congratulaions)
    order_number += 1

    if order_number > 1: 
        final_order = input(f"\nIf you would like to add a seperate order please enter \"Y\" otherwise enter \"N\" to end the program\n").strip().upper()
        while final_order not in option_list:
                final_order = input(f"You entered {final_order} which is an invalid input. Please try again. \nPlease enter Y to add Pepperonis to your pizza or N if you do not.\n").strip().upper()
        if final_order == "Y":
            base_price = 0
            pizza_list = []
            i = 1
            order_name = ""
            continue_order = True
            continue
        else:
            #exit program with message
            print("THANK YOU FOR ORDERING WITH FREDDIES!!! \nWe are WORKING AS FAST AS HUMANLY POSSIBLE to get your pizza to you. \nIf it ain't there in 30 minutes, we are sorry :(")
            endProgram = True
            exit
        


#     elif final_order == True: 
#         endOrder(total_price, pizza_list)
# if final_order == True: #create new order using pizza_list
#     endOrder(total_price, continue_pizza_list, order_name)
    
            
#######################################################################################################################################################################################################
# NOTES

# Note 1
# The full name is Freddies the apostrephe is grammativally correct ALTER if youd like

# Note 2
# add onto this by
        # initialize the empty string 
        # format the string where it the udpate is needed
    # if the order item is its own entity like a soda or a side like breadsticks use one space 
        # _breadsticks \t $0.00
        # try to keep all prices in the same format
    # if the order item is a item modifier like pepperoni or extra cheese append like this 
        # \t $0.00 add pepperoni
        # tab escape sequence - $amount for the surcharge, what the surcharge is for 
    # each line should end with \n to leave a new line before the next statementEXCEPT FOR THE LAST 
