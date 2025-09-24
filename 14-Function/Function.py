# function in python --

# Example without function:--
print("manish")
print("mansih")
print("manish")

 
# Create a simple function --

def hello ():    #Function define --
    print("Hello manish")
    
hello()    #function calling --




# 4. Parameters and Arguments--

def sum (num1 , num2):   #Parameter: 
    return f"A sum of num :-{num1 + num2}"

s = sum(2,4)
print(s)
l = sum(10,20)   #Argument-
print(l)




# return staemment --

def sum (num):
    return num * num 

number = sum(5)
print(number)



#  local variable and global variable --

# local variable  --

def sum (x,y):
    return x+y

s = sum(4,2)
print(s)



# global variable --
a = 4
def sum2 (b):
    return a +b

sum_2 = sum2(22)
print(sum_2)