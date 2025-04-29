# Final Project
![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
## Description
The final project for Programming Logic 1000-12345. This class project is the culmination of all learned  material and skill from throughout the course and tested through a final class project.

## Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [Credits](#credits)
* [License](#license)
* [Contributing](#contributing)
* [Tests](#tests)
* [Questions](#questions)

## Iterations and updates

### Iteration I

#### ***Week I - Senior Developer - Keyshia ...***

#### ***Tasks:***
- Implement pizza size selection 
- Implement pepperoni topping option 
- Implement extra cheese option 
- Create pricing logic based on size and toppings 
- Implement order total calculation 
- Create basic user interface for order input 
- Perform unit testing 
- Conduct integration testing


#### ***Developer Notes*** 

blah blah blah blah 

#### ***Code for Iteration I***

```python
# Pizza Order Program
base_price = 0.00
# Ask customer to choose the size of their pizza #
pizza_size = input("What size of pizza do you want? Please write S, M or L:  ").upper()


if pizza_size.upper() == "S":
    base_price += 15.00
elif pizza_size.upper() == "M":
    base_price += 20.00
elif pizza_size.upper() == "L":
    base_price += 25.00

# Ask customer if they want pepperoni #
topping_pepperoni = input ("Would you like pepperoni? Y or N:  ").upper()

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
topping_extra_cheese = input ("Would you like extra cheese? Y or N:  ").upper()
 
if topping_extra_cheese.upper() == "Y":
    base_price += 1.00
elif topping_extra_cheese.upper() == "N":
    base_price += 0.00

print(f"Thank you for choosing Python Pizza Deliveries, your final bill is ${base_price:.2f}")


```

### Iteration II

#### ***Week II - Senior Developer - Grant ...***

#### ***Tasks:***
- Implement discount logic
- Create a receipt generator
- Implement gratuity calculator
- Create a input validation system and error handling system
- Test the application for bugs and errors
- Conduct integration testing


#### ***Developer Notes*** 
All the required tasks were completed in a 3 line block. 

1. Check if `pizza_size`, `topping_pepperoni`, and `topping_extra_cheese` are valid inputs.
2. Check if `pizza_size` is "L" and if `topping_pepperoni` and `topping_extra_cheese` are both "Y". If so, apply a $5 discount.
3. Print the final price and receipt.
4. The code is modular and can be easily extended to include more toppings or discounts in the future.

**User Interface Requirements**
- Clear communication when discount is applied
- Display congratulatory message for qualifying orders
- Show final price with discount applied
- No discount messaging for non-qualifying orders

**Technical Requirements**
- Input validation for all user inputs
- Accurate price calculation including discount
- Clear code documentation
- Maintain existing input structure

#### ***Code for Iteration II***

```python



option_list = ["Y","N"]
size_list = ["S","M","L"]
base_price = 0.00





receiptOrderItemsB = ""
receiptOrderItemsC = ""
receiptorderItemsC2 = ""
receiptOrderItemsD = ""
receiptOrderItemsE = ""
receiptOrderItemsF = ""

# Error Handling
pizza_size = input("\nEnter pizza size as s, m, l, S, M or L.\n").strip().upper()
while pizza_size not in size_list:
    pizza_size = input(f"You entered {pizza_size} which is an invalid value. Please try again. \nPlease enter a size for your Freddies' Pizza.\nOptions include:\nS for Small, M for Medium, and L for Large.\n").strip().upper()

topping_pepperoni = input("\nPepperoni? Y or N:  \n").strip().upper()
while topping_pepperoni not in option_list:
    topping_pepperoni = input(f"You entered {topping_pepperoni} which is an invalid input. Please try again. \nPlease enter Y to add Pepperonis to your pizza or N if you do not.\n")

topping_extra_cheese  = input ("\nExtra cheese? Y or N:  \n").strip().upper()
while topping_extra_cheese not in option_list:
    topping_extra_cheese = input(f"You entered {topping_pepperoni} which is an invalid input. Please try again. \nPlease enter Y to add Extra Cheese to your pizza or N to opt out.\n")

receiptOrderItemsA = f"1 {pizza_size} Pizza = "

# Base Price of Pizza
if pizza_size == "S":
    base_price += 15.00
    receiptOrderItemsB = f"$15.00 \n"
elif pizza_size == "M":
    base_price += 20.00
    receiptOrderItemsB = f"$20.00 \n"
elif pizza_size == "L":
    base_price += 25.00
    receiptOrderItemsB = f"$25.00 \n"
else:
    print("Invalid input. Please enter S, M, or L")
  

# Add Pepperoni to Pizza
if topping_pepperoni == "Y" and base_price >= 20:
    base_price += 3.00
    receiptOrderItemsC = f"""\t+ $2.00 - add Pe \n """
    receiptorderItemsC2 = """ \t+ $1.00 - sz srchrg \n"""
elif topping_pepperoni == "Y":
    base_price += 2.00
    receiptOrderItemsC = f"""\t+ $2.00 - add Pe \n"""
    
# Add Extra Cheese to Pizza
if topping_extra_cheese == "Y":
    base_price += 1.00
    receiptOrderItemsD = f"""\t+ $1.00 - add Ex Ch"""



if pizza_size == "L" and topping_pepperoni == "Y" and topping_extra_cheese == "Y":
    base_price -= 5.00
    receiptOrderItemsE = f"""\t- $5.00 - Big Freds Discount \n"""

if pizza_size == "L" and topping_pepperoni == "Y" and topping_extra_cheese == "Y":
    receiptOrderItemsF = "Congratulations on your Freddies' $5 discount."
    base_price -= 5.00
    
# Calculate paid values
print(base_price)
receiptOrderItems = receiptOrderItemsA + receiptOrderItemsB + receiptOrderItemsC + receiptorderItemsC2 + receiptOrderItemsD + receiptOrderItemsE + receiptOrderItemsF
print(receiptOrderItems)
```
### Iteration III

#### ***Week III - Senior Developer - Franci ...***

#### ***Tasks:***
- Implement pizza size selection 
- Implement pepperoni topping option 
- Implement extra cheese option 
- Create pricing logic based on size and toppings 
- Implement order total calculation 
- Create basic user interface for order input 
- Perform unit testing 
- Conduct integration testing


#### ***Developer Notes*** 

blah blah blah blah 

#### ***Code for Iteration III***

```python
#price of all of the pizzas total
total_price = 0.00

while True:
    base_price = 0.00
    
    # Ask customer to choose the size of their pizza #
    pizza_size = input("What size of pizza do you want? Please write S, M or L:  ").upper()
    while pizza_size.upper() not in ("S", "M", "L"):
        print("Invalid input. Please enter S, M, or L.")
        pizza_size = input("What size of pizza do you want? Please write S, M, or L:  ").upper() 
    
    if pizza_size.upper() == "S":
        base_price += 15.00
    elif pizza_size.upper() == "M":
        base_price += 20.00
    elif pizza_size.upper() == "L":
        base_price += 25.00
    
    # Ask customer if they want pepperoni #
    topping_pepperoni = input ("Would you like pepperoni? Y or N:  ").upper()
    while topping_pepperoni.upper() not in ("Y", "N"):
        print("Invalid input. Please enter Y or N")
        topping_pepperoni = input ("Would you like pepperoni? Y or N:  ").upper()
    
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
    topping_extra_cheese = input ("Would you like extra cheese? Y or N:  ").upper()
    while topping_extra_cheese.upper() not in ("Y", "N"):   
        print("Invalid input. Please enter Y or N")
        topping_extra_cheese = input ("Would you like extra cheese? Y or N:  ").upper()  
    
    if topping_extra_cheese.upper() == "Y":
        base_price += 1.00
    elif topping_extra_cheese.upper() == "N":
        base_price += 0.00
    
    if pizza_size.upper() == "L" and topping_pepperoni == "Y" and topping_extra_cheese == "Y":
        print ("Congratulations! You've earned a $5 discount on your order.")
        base_price -= 5.00
    
    # Ask if they want to order another pizza BEFORE showing subtotal
    another = input("\nWould you like to add another pizza to your order? (Y/N): ").upper()
    while another not in ("Y", "N"):
        another = input("Please enter Y to add another or N to finish your order: ").upper()
    
    
    # Add to total order
    total_price += base_price
    
    
    if another == "N":
        break  # Exit the pizza-adding loop

# Final output
print(f"\nThank you for choosing Python Pizza Deliveries, your final bill is ${base_price:.2f}")
```

## Installation
To install this project, pull the repo to your personal terminal and run `python freddies.py` in your console. 

## Usage
This project creates a simple pizza ordering console application which dynamically builds and subsequently prints to the user upon completion. 

The end result should look like this: 
![Example Console Output](./ExampleConsole.png)

If you need to move the code into a simple python editor, in place of the `from ---- import ----` you can cut the actual function and paste it over the import statements to simplify using multiple files. I just like mulitple files because it is easier to read. 

Directory structure is as follows:
- README.md - this file.
- Freddies.py - the main file that helpers will feed into.
- tip.py - the gratuity calculator file and its components. 
- recepit.py - the recepit generater file and its components.
- Example and reference Images:
    - Example.png
    - ExampleConsole.png

## Credits
Credit goes to K, F, and G.

## License
This project is licensed under the Apache 2.0 license.
https://opensource.org/licenses/Apache-2.0

## Contributing
To contribute to this project, pull down this repo, make changes to the repo, and submit your changes via a pull request where new features will be reviewed before adding.

## Tests
To test out this application, run `python test.py` to run a simplified version of the code. This will run a test case to ensure that the code is working as intended.

## Questions
If you have any questions, please feel free to reach out to me at Grant.L.Williams@outlook.com. You can also check out my GitHub profile at [GrantLw100, , ](GrantLw100, , ).
