while True:
    print("\nMenu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "5":
        print("Exit")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Wrong choice")
        continue

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == "1":
        print("Result:", a + b)

    elif choice == "2":
        print("Result:", a - b)

    elif choice == "3":
        print("Result:", a * b)

    elif choice == "4":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", a / b)