#  Practise Qustion ----

"""
@1----Vote Eligibility
Ask the user for their age.
If the age is 18 or above, print "You can vote". Otherwise, print "You cannot vote".
"""

user = int(input("Enter a age :-"))

if user > 18:
    print("you can vote :-")
  
else:
    print("you can't do vote:-")
    
    
    
"""
@2----Even or Odd

Take a number as input.
Check if it’s even or odd.
"""


user_number = int(input("Enter a number :-"))
if user_number % 2==0:
    print("Even Number")
    
else:
    print("Odd number")
