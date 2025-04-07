def modulas(x,y):
    return x% y

def exponatiate(x,y):
    return x ** y

def divide(x,y):
    return x / y

def power(x,y):
    return x//y

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y


print("Simpl Calculator signs below")
print("1.Modulas")
print("2.exponatiate")
print("3. Addition")
print("4. Subtraction")
print("5. Multiplication")
print("6. Division")
print("7. power")


while True:
    choice = input("Enter your choice (1, 2, 3, 4, 5, 6, 7): ")
    if choice  !=("1", "2", "3", "4", "5", "6", "7"):
        num1 = int(input("Enter  number: "))
        num2 = int(input("Enter  number: "))

        if choice == '1':
            print(num1, "%", num2, "=", modulas(num1, num2))

        elif choice == '2':
            print(num1, "**", num2, "=", exponatiate(num1, num2))

        elif choice == '3':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '4':
            print(num1, "-", num2, "=", subtract(num1, num2))

        
        elif choice == '5':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '6':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '7':
            print(num1, "//", num2, "=", power(num1, num2))    
        
        next_calculation = input("Do you want to do another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    else:
        print("Invalid input. Please enter a number(1 TO 7).")