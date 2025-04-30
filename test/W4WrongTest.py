from FinalProject.utils.testUtils import generateChance, testArray
from ..utils.FreddiesTest import topField, bottomField
from ..utils.utils import inputYesOrNo, inputInt
breakline = "-"*100

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

    