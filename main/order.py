
from utils.Utils import inputPizzaSize, inputPizzaYesOrNo, inputYesOrNo, inputInt, start_delayed_message
input_array =  [ "add Pepperoni to", "add Extra Cheese to", "add a soda to", "add FredSticks to", "add more Freddies Pizzas to", "split", "add delivery or pick-up to"]



#############################################################################################################################################################
#
#               # Freddies Pizzeria Console Application Order Generator
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


    if pizza_size == "L" and topping_pepperoni == "Y" and topping_extra_cheese == "Y":
        pizza_price = 25.00


    
    if continue_order_valid == "Y":
        continue_order = True
    else:
         continue_order = False
    return pizza_price, pizza_string, continue_order







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
    
    
    deliver_order = inputYesOrNo("If you would like to add delivery to your order please enter \"Y\" for yes and \"N\" for no delivery.")
        
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


