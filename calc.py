import math


print("       PYTHON CALCULATOR")
print("==============================")

while True:

    print("\n------------------------------")
    print("1. Addition        (+)")
    print("2. Subtraction     (-)")
    print("3. Multiplication  (*)")
    print("4. Division        (/)")
    print("5. Remainder       (%)")
    print("6. Power           (**)")
    print("7. Square Root")
    print("8. Percentage")
    print("9. Quit")
    print("------------------------------")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 + num2
            print(f"\n{num1} + {num2} = {result}")
        except ValueError:
            print("Invalid number!")

    elif choice == "2":
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 - num2
            print(f"\n{num1} - {num2} = {result}")
        except ValueError:
            print("Invalid number!")

    elif choice == "3":
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 * num2
            print(f"\n{num1} × {num2} = {result}")
        except ValueError:
            print("Invalid number!")

    elif choice == "4":
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if num2 == 0:
                print("ERROR: Cannot divide by zero!")
                continue

            result = num1 / num2
            print(f"\n{num1} ÷ {num2} = {result}")
        except ValueError:
            print("Invalid number!")

    elif choice == "5":
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if num2 == 0:
                print("ERROR: Cannot divide by zero!")
                continue

            result = num1 % num2
            print(f"\n{num1} % {num2} = {result}")
        except ValueError:
            print("Invalid number!")

    elif choice == "6":
        try:
            num1 = float(input("Enter base: "))
            num2 = float(input("Enter exponent: "))
            result = num1 ** num2
            print(f"\n{num1} ^ {num2} = {result}")
        except ValueError:
            print("Invalid number!")

    elif choice == "7":
        try:
            num = float(input("Enter number: "))

            if num < 0:
                print("ERROR: Cannot square-root a negative number!")
                continue

            result = math.sqrt(num)
            print(f"\n√{num} = {result}")
        except ValueError:
            print("Invalid number!")

    elif choice == "8":
        try:
            percent = float(input("Enter percentage: "))
            number = float(input("Enter number: "))
            result = (percent / 100) * number
            print(f"\n{percent}% of {number} = {result}")
        except ValueError:
            print("Invalid number!")

    elif choice == "9":
        print("\nThanks for using the calculator!")
        break

    else:
        print("\nInvalid choice! Please choose 1-9.")
