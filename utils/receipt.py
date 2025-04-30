from .utils import calculateGratuity


    #############################################################################################################################################################
#
#               # Freddies Pizzeria Console Application Receipt Generator
#   # These are the utility functions that handle generating the tip, creating the order for the receipt, and creating the receipt itself
#
#############################################################################################################################################################


# import necessary technologies for date time and random integer generation
from datetime import datetime, date
import random

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
        billing = f"\tVISA: XXXX-XXXX-XXXX-{random.randint(1000, 9999)}\n"*split_amount
        split_bill = f"TOTAL SPLIT x{split_amount}:    ${split_price:.2f}"
    else:
        billing += f"\tVISA: XXXX-XXXX-XXXX-{random.randint(1000, 9999)}"

        

    
    
    
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

