# Calculator

## Overview

This is a simple graphical calculator application, built using Pythons's **tkinter** library, mimicking the IOS calculator and its features. The calculator supports basic arithmetic operations such as addition, subtraction, multiplication and division, along some additional features like percentage calculation and toggling between positive and negative numbers.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, division
- Percentage calculation
- Toggle between positive and negative numbers
- Clear and clear all functionality
- Graphical interface that mimics the Ios calculator

## Requirements

- Python 3.x
- **tkinter** library

## Installation

1. Ensure you have Python 3.x installed on your system. You can download it from the [official Python website](https://www.python.org/).

2. Clone this repository or download the **Calculator.py** file on your local machine.

## Usage

1. Navigate to the directory containing the **Calculator.py** file in your terminal or command prompt.

2. Run the calculator application using the following command:

    python Calculator.py

3. The calculator window will appear. Use the buttons to perform your desired calculations.

## Code Structure

- **main()**: Initializes and starts the calculator application.
- **Calculator** class: Defines the main calculator logic and GUI components.
    - **__init__()**: Initializes the calculator, creating the root window, entry widget and buttons.

### Functions

- **create_root()**: Creates the main application window.
- **create_entry(root)**: Creates the entry widget for calculator display.
- **create_buttons(calculator)**: Creates and configures all the buttons on the calculator.
- Button-specific functions that define the behavior of indivisual buttons:
    - **button_num(calculator, num)**
    - **button_comma(calculator)**
    - **button_clear(calculator)**
    - **button_clear_all(calculator)**
    - **button_equal(calculator)**
    - **button_operator(calculator, op)**
    - **button_percentage(calculator)**
    - **button negative(calculator)**
- **button_toggle(calculator, operator="")**: Changes the colours of the chosen operator's button.

## Customization

- You can modify the appearance of the calculator by changing the button styles, colors, and fonts within the **create_buttons** function.
- Additional functionality can be added by defining new button-specific functions and adding corresponding buttons in the **create_buttons** function.

## Testing

A **test_Calculator.py** file is included to test the core functionality of the **Calculator.py** application. This test suite ensures that all calculator operations perform correctly.

### Running Tests 

1. Ensure you have **pytest** installed. If notn install it using the following command:

    pip install pytest

2. Run the tests using the following command:

    pytest test_Calculator.py

3. The test results will be displayed in the terminal, indicating whether the functions in *Calculator.py* are working as expected.

