######################################################################################################################################################################################################

              # Freddies Pizzeria Console Application Main
  # This is the main entry point for the Freddies Pizzeria Console Ordering application.

######################################################################################################################################################################################################



# import receipt generator
from .utils.order import createOrder, splitOrder, deliverOrder
from .utils.receipt import createReceiptItems, createReceipt
from .utils.utils import pizza_intro, pizza_outro, inputYesOrNo
import random


# initialize base values and comparison lists
size_list = ["S","M","L"]
option_list = ["Y","N"]
break_line = ("-"*80)
new_order = ("#"*120)

base_price = 0.00
_id = random.randint(1, 999)
order_number = 1
order_id = order_number + _id
order_name = ""
pizza_list = []
soda_count = 0
breadstick_count = 0
continue_order = True
order_again = ""
endProgram = False
receiptOrderItems = ""









print(pizza_intro)
# base_price, pizza_string, continue_order = createOrder()
while endProgram == False:
    while continue_order == True:
        if (order_name == ""):
            print(break_line)
            order_name = input("\nPlease enter a name for the order?\n")
        #would you like to double the last order exactly as it was written? 
        # if Y - validate, set order_amount to 2, double price, createReceiptOrder,
        pizza_price, pizza_string, continue_order, pizza_extra = createOrder()
        pizza_list.append(pizza_string)
        soda_count += pizza_extra[0]
        breadstick_count += pizza_extra[1]
        base_price +=pizza_price
    order_list = "endOfPizza".join(pizza_list)
    splits = splitOrder()
    delivery_option, receiptOrderItemsDeliveryFee = deliverOrder()
    receiptOrderItems = createReceiptItems(order_list, soda_count, breadstick_count)
    createReceipt(order_name, order_number + order_id, receiptOrderItems + receiptOrderItemsDeliveryFee, base_price, splits)

    if delivery_option == "Y":
        print(f"THANK YOU FOR ORDERING WITH FREDDIES {order_name}!!! \nWe are working AS FAST AS HUMANLY POSSIBLE to get your pizza to you. \nIf it ain't there in 30 minutes, we are sorry :(")
    else:
        print(f"THANK YOU FOR ORDERING WITH FREDDIES {order_name}!!! \nWe are baking AS FAST AS HUMANLY POSSIBLE so your order is ready when you arrive. \nIf it ain't ready in 15 minutes, we are sorry :(")

    order_again = inputYesOrNo(f"\nIf you would like to add a seperate order please enter \"Y\" otherwise enter \"N\" to end the program\n")
    
    if order_again == "Y":
        base_price = 0
        breadstick_count = 0
        soda_count= 0
        pizza_list = []
        order_name = ""
        order_list = ""
        receiptOrderItems = ""
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
        






