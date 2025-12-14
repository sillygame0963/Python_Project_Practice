# CACULATOR PROJECT

# ADD
def add (x,y):
    return x + y

# SUBTRACT
def subtract (x,y):
    return x - y

# MULTIPLY
def multiply (x,y):
    return x * y

# DIVIDE
def divide (x,y):
    if y == 0:
        return "Error!"
    else:
        return x / y

def calculator ():
    print("Select operator: ")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")

    while True:
        # Take user input
        choice  = input("Enter choices (1/2/3/4)")

        if choice in ['1','2','3','4']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            if choice == '2':
                print(f"{num1} + {num2} = {subtract(num1, num2)}")
            if choice == '3':
                print(f"{num1} + {num2} = {multiply(num1, num2)}")
            if choice == '4':
                print(f"{num1} + {num2} = {divide(num1, num2)}")

        # Option to exit
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    print("Exit Calculator. Goodbye!")

# Call the function
calculator()