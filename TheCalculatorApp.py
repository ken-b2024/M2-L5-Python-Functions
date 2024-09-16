import math
#Task 1
def add(num1, num2):
    Total = num1 + num2
    print(Total)
def subtract(num1, num2):
    Total = num1 - num2
    print(Total)
def divide(num1, num2):
    Total = num1 / num2
    print(Total)
def multiply(num1, num2):
    Total = num1 * num2
    print(Total)

#Task 2 
user_action = input("What function do you want to perform? (add/subtract/divide/multiply): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if user_action == 'add':
    add(num1, num2)
if user_action == 'subtract':
    subtract(num1, num2)
#Task 3
if user_action == 'divide':
    if num1 and num2 != 0:
        divide(num1, num2)
    else:
        print("Oops! Cannot divide by zero!")   
if user_action == 'multiply':
    multiply(num1, num2)