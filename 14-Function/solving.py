# Function Practice Questions--

# @1---Write a function that takes a number and returns its square.
def square (num):
    return num *num

num2 = square(10)  #100
print(num2)

# @2---Write a function that takes two numbers and returns their sum.

def sum (x,y):
    return x + y

sum2 = sum(2,8)
print(sum2)

# @3---Write a function that takes a list of numbers and returns the maximum value.

list = [1,3,4,5,6,7,8,99]
def maxi ():
    return maxi

r = max(list)
print(r)

# @4---Write a function that takes a string and returns it in uppercase.

name = "manish"
def stu ():
    return stu

n = name.upper()
print(n)

# @5---Write a function that takes a list of numbers and returns only the even numbers.

num_list = [5,7,8,9,0,8,7,6,8,6,5,44,87,89,90,83]

def even_check ():
    even = []
    for num in num_list:
        if num % 2 == 0:
            even.append(num)
    return even
        
r = even_check()
print(r)