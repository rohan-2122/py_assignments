def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y==0:
        return "Error : Division by Zero"
    else:
        return x / y


def Calculator():
    print("Welcome to Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divison")
    print("5. Exit Program")

    while True:
        choice = input("Enter the operation no. between 1 to 5:")

        if choice in ('1','2','3','4','5'):
            if choice != '5':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} x {num2} = {multiply(num1, num2)}")
                if choice == '4':
                        print(f"{num1} / {num2} = {divide(num1, num2)}")

            elif choice == '5':
                print("Exiting Calculator. Goodbye!!")
                break

        else:
            print("Invalid Input: Enter a no. between 1 to 5")
            

Calculator()