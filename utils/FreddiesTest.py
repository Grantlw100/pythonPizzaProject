from .receipt import createReceiptItems
import random
from .testUtils import generateTestInputs
from .utils import testArray

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
    pizza_extra = [0,0]
    order_list = ""
    soda_count = 0
    breadstick_count = 0
    continue_order = True
    order_again = ""
    endProgram = False
    receiptOrderItems = ""
    receiptOrderItemsDeliveryFee = " "


    #     createOrder
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
            pizza_price, pizza_string, continue_order, pizza_extra, order_again = createOrderTest(testArray[1], testType)
            print(topField)
            print("CREATE ORDER COMPLETE")
            print(endField)
            print(f"\nPIZZA PRICE: {pizza_price} PIZZA STRING: {pizza_string} CONTINUE ORDER:{continue_order} PIZZA EXTRA :{pizza_extra} ORDER AGAIN :{order_again}\n")
            print(fullField)
            print("\n")
            pizza_list.append(pizza_string)
            soda_count += pizza_extra[0]
            breadstick_count += pizza_extra[1]
            base_price +=pizza_price
        order_list = "endOfPizza".join(pizza_list)
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
            breadstick_count = 0
            soda_count= 0
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
            


def createOrderTest(testArray, testType):
    pizza_string = ""
    pizza_extra = [0,0]
    pizza_price = 0.00
    pizza_extra = [0,0]

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
    print("TEST ADDING FREDSTICKS")
    print(endField)
    extra_breadsticks = generateTestInputs(testArray, testType)
    print(fullField)
    print("\n")
    
    
    print(topField)
    print("TEST ADDING SODA")
    print(endField)
    extra_soda = generateTestInputs(testArray, testType)
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
        return pizza_price, pizza_string, continue_order, pizza_extra, order_again

    elif continue_order_valid == "N":
         continue_order = False
         return pizza_price, pizza_string, continue_order, pizza_extra, order_again




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


def calculateGratuityTest(subtotal):
    
    tipAmount = (random.randint(1,10)/10)
    subtotal *= tipAmount
    print(topField)
    print("TEST DELIVER ORDER")
    print(endField)
    print(f"\nORDER TIP PERCENTAGE: {tipAmount*10}%")
    print(f"\n{breakLine}\n")
    print(f"ORDER TIP AMOUNT: {subtotal: .2f}\n")
    print(fullField)
    print("\n")
    return subtotal
    

