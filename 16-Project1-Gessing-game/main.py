# Number gussing game in python --

import random   # use a random module


# computer Ganrate a number -
computer = int(random.randrange(0,20))

# user input number -
user_time = int(input("Enter a your Number :-"))

# condition  --
if user_time > computer:
    print("User won :" , user_time)
    print("computer number:-" ,computer)
    
elif user_time < computer:
    print("computer won:" , user_time)
    print("computer number:" , computer)
    

elif user_time == computer:
    print("maatch Drw:" , user_time)
    print("computer number :" , computer)
    
else:
    print("invalid number :-")


