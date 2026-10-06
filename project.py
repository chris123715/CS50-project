def main():
    try:
        while True:
            first, operation, second = calculator()
            result1 = calculations(first,operation,second)
            answer(result1)

            calculation2 = input("Do you want to continue your calculation? (yes or no):")
            if calculation2 == "no":
                break
    except TypeError:
        print(end="")

def answer(result1):
    print("Answer: ", result1)

def calculator():
    try:
        first = float(input("What's the first number? "))
        operation = input("Which operation? ")
        second = float(input("What's the second number? "))
        return first, operation, second
    except ValueError:
        print("Not Valid!")


def calculations(first, operation, second):
    if operation == "+":
        result1 = first + second
    elif operation == "-":
        result1 = first - second
    elif operation == "*":
        result1 = first * second
    elif operation == "/":
        if second == 0:
            return "Cannot divide by zero!"
        result1 = first / second
    return result1

if __name__ == "__main__":
    main()