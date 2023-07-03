#!/usr/bin/env python3

interaction_str = dict(
    available_operators="\nPlease \033[31mselect\033[0m an operation:\n"
    "1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n",
    welcome="Welcome to the Calculator Program\033[31m!\033[0m\n\n",
    num_1="Please enter the first number: ",
    num_2="Please enter the second number: ",
    op="Enter your choice (1-4): ",
    result="\nThe result is: ",
    operator_error="Unknown operator: ",
    hint_num="Enter an integer or floating point number",
    error_divide_by_0="Can't divide by zero",
)


def add(number_1: float, number_2: float) -> float:
    return number_1 + number_2


def subtract(number_1: float, number_2: float) -> float:
    return number_1 - number_2


def multiply(number_1: float, number_2: float) -> float:
    return number_1 * number_2


def divide(number_1: float, number_2: float) -> float:
    return number_1 / number_2


def _calc(number_1: float, number_2: float, operator: int) -> float:
    """Simple arithmetic operations on two numbers."""
    if operator == 1:
        return add(number_1, number_2)
    elif operator == 2:
        return subtract(number_1, number_2)
    elif operator == 3:
        return multiply(number_1, number_2)

    return divide(number_1, number_2)


def calculator() -> None:
    """
    Prompt the user to enter two numbers.
    Prompt the user to select an operation from the following options:
    addition, subtraction, multiplication, division.
    Based on the selected operation, the corresponding calculation is performed.
    Display the result to the user.
    """
    print(interaction_str["welcome"])

    while True:
        try:
            number_1 = float(input(interaction_str["num_1"]).replace(",", "."))
            break
        except ValueError:
            print(interaction_str["hint_num"])
            continue

    while True:
        try:
            number_2 = float(input(interaction_str["num_2"]).replace(",", "."))
            break
        except ValueError:
            print(interaction_str["hint_num"])
            continue

    while True:
        print(interaction_str["available_operators"])

        try:
            operator = int(input(interaction_str["op"]))
        except ValueError:
            print(interaction_str["operator_error"])
            continue
        else:
            if operator not in range(1, 5):
                print(interaction_str["operator_error"], operator)
                continue
            break

    try:
        result = _calc(number_1, number_2, operator)
    except ZeroDivisionError:
        print(interaction_str["error_divide_by_0"])
        exit(2)

    print(interaction_str["result"], result)


if __name__ == "__main__":
    calculator()
