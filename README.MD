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


## Installation
To install this project, begin by creating a new directory in a proper location on your computer. Change from your current directory into the new directory. Then, simply follow these instructions created by Github.

```bash 
git init
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Grantlw100/pythonPizzaProject.git
git pull origin main
```
## Usage
To use this project, you will need to have Python 3.x installed on your computer. You can download Python from the official website: [Python.org](https://www.python.org/downloads/).
    This project creates a simple pizza ordering console application which dynamically builds and subsequently prints to the user upon completion. 

Running any file in this project requires pythons module notation: `python -m fileName`. Be sure ***NOT*** to include the .py from the python file's name as this is unnecessary when utilizing the module notation.
To run the project, open a terminal or command prompt, navigate to the directory where the project is located, and run the following command:
```bash
python -m freddies
```

This will start the application and prompt the user for inputs. 

The initial prompt will be to query whether or not the user would like to perform tests. The query requests permission to run tests and the user will respond with `"Y"`and the number of tests to run or `"N"` to bypass tests.

Follow the prompts to place your order and subsequent orders.
The program will ask for a series of "Y" or "N" questions to build orders. Each subsequent order will be added into a final order where the user will be prompted to enter a tip as either a dollar amount or a percentage. The program will compile all pizzas for that order and print a receipt to the console followed by a series of delivery or pickup simulation messages. 


The end result should look like this: 
![First image of Freddies console Application showing the pizza intro](./freddiesApp1.png)
![Second image of Freddies console Application showing the pizza intro](./freddiesApp2.png)
![Third image of Freddies console Application showing the pizza intro](./freddiesApp3.png)
![Fourth image of Freddies console Application showing the pizza intro](./freddiesApp4.png)
![Fifth image of Freddies console Application showing the pizza intro](./freddiesApp.png)

If you need to move the code into a simple python editor, use the `allcode.py` file and paste the code into your editor of choice. 


## Credits
Franci Chappie
Grant Williams
Taylor Keyshla

## License
This project is licensed under the Apache 2.0 license.
https://opensource.org/licenses/Apache-2.0

## Contributing
To contribute to this project, follow the [Installation](#installation) instructions, clone this repo and make changes to the repo. Submit your changes via a pull request where new features will be reviewed before being adding.
Ensure to include your name and all contributions in the `README.md` file.

## Tests
To test this application, run `python freddies.py` and follow the first initial prompts to run the tests. Tests are generated using randomly selected values from the list of options. The tests will run and print the results to the console.
There are two tests. One test is ran with nothing but proper inputs for each question. The second test is ran with random inputs for each question. The tests will print the results to the console. The program will then print the final order and receipt to the console and notify the user when the test session has ended. 

## Questions
If you have any questions, please feel free to reach out to me at Grant.L.Williams@outlook.com. You can also check out my GitHub profile at [GrantLw100, , ](GrantLw100, , ).
