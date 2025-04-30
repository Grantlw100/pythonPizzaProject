######################################################################################################################################################################################################

              # Freddies Pizzeria Console Application Main
  # This is the main entry point for the Freddies Pizzeria Console Ordering application.

######################################################################################################################################################################################################



# import receipt generator
from main.order import createPizza, deliverOrder, addExtras
from main.receipt import createReceiptItems, createReceipt
from utils.Utils import pizza_intro, pizza_outro, inputYesOrNo, inputSplits
from utils.TestFunctions import breakLine
from test.Week5Test import week5Test
import random



def FreddiesPizzaApplication():
    print(breakLine)
    runTest = inputYesOrNo("Would you like to run tests for Freddies Week 5 Code?")
    print(breakLine)
    if runTest == "Y":
        week5Test()
    # initialize base values and comparison lists
    break_line = ("-"*100)
    new_order = ("#"*100)

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
    print("Enter ctrl + c to end current order then enter \"N\" to exit the program")
    while not endProgram:
        try: 
            while continue_order:
            
                    if (order_name == ""):
                        print(break_line)
                        order_name = input("\nPlease enter a name for the order?\n")
                    #would you like to double the last order exactly as it was written? 
                    # if Y - validate, set order_amount to 2, double price, createReceiptOrder,
                    pizza_price, pizza_string, continue_order = createPizza()
                    pizza_list.append(pizza_string)
                    base_price +=pizza_price
            order_list = "endOfPizza".join(pizza_list)
            soda_count, breadstick_count, extras_value = addExtras()
            delivery_option, receiptOrderItemsDeliveryFee = deliverOrder()
            splits = inputSplits()
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





