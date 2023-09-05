from art import logo


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }
rerun = True
use_result = "n"

print(logo)
while rerun:

    # Get the first number.
    # In case of a rerun, do we use the result from last time?
    if use_result == "n":
        n1 = float(input("What is the first number? "))
    else:
        print(f"First number: {n1}")

    # Choose the kind of operation
    action = ""
    while action not in operations:
        action=input("Pick an operation (+ - * /) ")
    operation = operations[action] # operation points to relevant function

    # Get the second number.
    n2=float(input("What is the next number? "))

    # Print result.
    result = operation(n1, n2)
    print(f"{n1} {action} {n2} = {result}")

    # Use result for next calculation "y/n" or quit "q"?
    use_result=""
    while not use_result == "y" and not use_result == "n" and not use_result == "q":
        use_result=input(f"Type Y to continue working with {result}, type N to start a new calculation or Q to quit. ").lower()
    match use_result:
        case "y":
            n1 = result
            rerun = True
        case "n":
            rerun = True
        case "q":
            rerun = False
            print("OK, bye!")
