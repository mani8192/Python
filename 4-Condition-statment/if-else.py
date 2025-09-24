# Condition Statment in python ---

"""
if 
elif
else
"""

age = 18

if age > 18:
    print("you are adult")
    
elif age == 18:
    print("you just become a adult ")
    
else :
    print("you are minor")
    
    
  
"""
@4-----Pass or Fail

Ask the user for their exam marks.
If marks are 33 or more, print "Pass". Otherwise, "Fail".

"""  


student = int(input("Enter a Marks :-"))

if student >= 60:
    print("first Div")
    
elif student >= 45:
    print("second div")
    
elif student >= 33:
    print("third div")
    
else:
    print("student fail ")