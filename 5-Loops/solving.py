# @1--------Sum of Numbers
# Find the sum of numbers from 1 to 100 using a for loop.

sum = 0
for i in range (1, 20):
    print(i)
    sum += i
    print(sum)
    
    
    
# @2--------- Multiplication Table
# Take a number from the user and print its multiplication table (1 to 10).


num = int(input("Enter a number -"))
for i in range(1,11):
    print(num , "x" , i , "=" , num * i)
    


# @3---------Sum of Even Numbers
# Find the sum of all even numbers between 1 and 100.

sum = 0
for i in range(1,300):
    if i % 2 == 0:
        sum += i
        print("the sum of total even number " , sum)
        
        

# @4-------------Reverse Multiplication Table
# Take a number from the user and print its multiplication table from 10 down to 1.

user_num = int(input("Enter a number :-"))
for i in range (11,0,-1):
    print(user_num*i)
    
    
