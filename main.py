from art import logo


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y


rerun = True
use_result = "n"

print(logo)
while rerun:
    if use_result == "n":
        n1 = float(input("What is the first number? "))
    else:
        print(f"First number: {n1}")
    action = ""
    while not action == "+" and not action == "-" and not action == "*" and not action == "/":
        action=input("Pick an operation (+ - * /) ")
    n2=float(input("What is the next number? "))
    match action:
        case "+":
            result=add(n1, n2)
        case "-":
            result = subtract(n1, n2)
        case "*":
            result = multiply(n1, n2)
        case "/":
            result = divide(n1, n2)
        case _:
            result = "Undefined result"
    print(f"{n1} {action} {n2} = {result}")
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
