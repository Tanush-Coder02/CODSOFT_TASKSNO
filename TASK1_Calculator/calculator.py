def calculator():
    print("Simple Calculator")
    num1 = float(input("ENTER FIRST NUMBER"))
    num2 = float(input("ENTER SECOND NUMBER"))

    print("SELECT OPERATION")
    print("1. ADD (+)")
    print("2. SUBTRACT(-)")
    print("3. MULTIPLY (*)")
    print("4. DIVIDE (%)")

    CHOICE = input("ENTER YOUR CHOICE (1/2/3/4) ")
    if CHOICE == '1':
        result = num1 + num2
    elif CHOICE == "2" :
        result = num1 - num2
    elif CHOICE == '3' :
        result = num1*num2
    elif CHOICE == '4':
        if num2 == 0 :
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2

    else:
        print("INVALID CHOICE")
        return
    print(f"Result: {result}")

if __name__ == "__main__":
    calculator()