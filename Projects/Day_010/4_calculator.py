from art import logo

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}


def calculator():
    print(logo)
    n1 = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue =True
    while should_continue:
        operation_symbol = input("Pick an operation from line above: ")
        n2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](n1,n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()
