interaction_str = dict(
    available_operators="\nPlease \033[31mselect\033[0m an operation:\n"
    "1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n",
    welcome="Welcome to the Calculator Program\033[31m!\033[0m\n\n",
    num_1="Please enter the first number: ",
    num_2="Please enter the second number: ",
    op="Enter your choice (1-4): ",
    result="\nThe result of multiplication is: ",
    operator_error="Unknown operator: ",
)


def _calc(number_1: float, number_2: float, operator: int) -> float:
    """
    Simple arithmetic operations on two numbers
    """
    if operator == 1:
        return number_1 + number_2
    if operator == 2:
        return number_1 - number_2
    if operator == 3:
        return number_1 * number_2

    return number_1 / number_2


def calculator() -> None:
    """
    Prompt the user to enter two numbers.
    Prompt the user to select an operation from the following options:
        addition
        subtraction
        multiplication
        division
    Based on the selected operation, the corresponding calculation is performed.
    Display the result to the user.
    """
    print(interaction_str["welcome"])

    try:
        number_1 = float(input(interaction_str["num_1"]))
        number_2 = float(input(interaction_str["num_2"]))

        print(interaction_str["available_operators"])

        operator = int(input(interaction_str["op"]))

        if operator not in range(1, 5):
            print(interaction_str["operator_error"], operator)
            exit(2)

        result = _calc(number_1, number_2, operator)

    except (ZeroDivisionError, ValueError) as e:
        print(e)
        exit(2)

    print(interaction_str["result"], result)


if __name__ == "__main__":
    calculator()
