# @2-Check if a number is prime.--

user_num = int(input("Enter a number here:-"))

if user_num <= 1:
    print("it's not a prime number")
    
if user_num >1:
        for i in range(2,user_num):
          if user_num % i == 0:
                print("Not a prime number:-")
        
else:
    print("prime number:-")
    
    