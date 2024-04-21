#Design a simple calculator with basic arithmetic operations.Prompt the user to input two numbers and an operation choice.Perform the calculation and display the result.
#Make Function of addition
def addition(x, y):
    return x + y

#Make Function of subtraction
def subtraction(x, y):
    return x - y

#Make Function of Multiplication
def multiply(x, y):
    return x * y

#Make Function of Division
def divide(x, y):
    return x / y

print(" ------- Select Operation that are given below ----------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

#Take input from the user
choice = input("Select the operation from (1/2/3/4) : ")

num_1 = float(input("Enter the number : "))
num_2 = float(input("Enter the number : "))

if choice == "1":
    print(num_1, "+", num_2, "=", addition(num_1, num_2))

elif choice == "2":
    print(num_1, "-", num_2, "=", subtraction(num_1, num_2))

elif choice == "3":
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))

elif choice == "4":
    print(num_1, "/", num_2, "=", divide(num_1, num_2))

else:
    print("Invalid Syntax!")