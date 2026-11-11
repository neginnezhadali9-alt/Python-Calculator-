#calculator

try:

    num1 = float(input("enter first number:"))
    num2 = float(input("enter second number:"))
    print("nchoose operation:")

    print("1. addition")
    print("2. sutraction")
    print("3. multiplication")
    print("4. division")

    choice = input("enterchoice (1/2/3/4):")

    if choice == '1':
        print("result:", num1 + num2)

    elif choice == '2':
        print("result:", num1 - num2)

    elif choice == '3':
        print("result:", num1 * num2)
        
    elif choice == '4':
        if num2 != 0:
            print("result:", num1 / num2)
        else:
            print("error! division by zero")
    else:
        print("invalid choice!")
except ValueError:
    print("please enter valid numbers.")
