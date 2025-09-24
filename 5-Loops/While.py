# while Loop in python --

num = 1
while num <= 10:
    print(num)
    num = num + 1
    
    
# @1---Countdown
# Print numbers from 10 down to 1.


num = 10 
while num >= 1:
    print(num)
    num = num - 1
    
    


# @2-Palindrome Check

# Check if a number is the same when reversed (e.g., 121 → Palindrome).
# give me  answer this qustion 
usernum = int(input("Enter a number: "))
originalnum = usernum  # store original number
reversednum = 0

while usernum > 0:  
    digit = usernum % 10
    reversednum = reversednum * 10 + digit
    usernum //= 10

if originalnum == reversednum:
    print("Number is Palindrome")
else:
    print("Not Palindrome")
