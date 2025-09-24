# take a input from user --

user = input("enter a name :-")
print(user)



# Count the number of vowels in a given string.


user_input = input("enter a name :- ")

for i in user_input:
    print(i)
    
    
    
    
"""Question 2: Even or Odd Checker
 Write a Python program that:

 Asks the user to enter a number.
 Checks if the number is even or odd.
 Prints "Even" if the number is even, or "Odd" if the number is odd."""
 
 
userNumber = int(input("enter a number :-"))

if userNumber % 2 == 0:
    print("Even Number")
    
else:
    print("Odd Number")
 
 
 
"""
Question 3: Simple Calculator
Write a Python program that:

Asks the user to enter two numbers.
Asks the user to enter an operator (+, -, *, or /).
Performs the operation and prints the result.

"""


user_num1 = int(input("Enter a Number :-"))
user_num2 = int(input("Enter a number :-"))
user_opreater = input("Enter a opreater :-")

if user_opreater == "+":
    print(user_num1 + user_num2)
    
elif user_opreater == "-":
    print(user_num1 + user_num2)
    
elif user_opreater == "*":
    print(user_num1 + user_num2)
    
elif user_opreater == "/":
    print(user_num1 / user_num2)
    
    

