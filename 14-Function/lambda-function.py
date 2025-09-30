# lamda function 

# lambda arguments: expression

addition = lambda x,y : x + y
print(addition(3,5))


# square --

squ = lambda x : x ** 2
print(squ(10))


# even-odd-number --

# even == true
# odd = false 
even_odd = lambda x : x % 2 == 0
print(even_odd(2))


# print_num --
sum = lambda x , m:  x + m
n = sum(2,3)
print(n)

    

# solving
# Using lambda + filter, extract only even numbers from a given list.
num_list = [1,4,3,5,6,4,3,7,8,9,4,666,76,87]

even_num = tuple(filter(lambda x : x % 2 == 0 , num_list))
print(even_num)


# Print numbers from 1 to 50 that are multiples of 5.

num_list = (range(1,51))
multi_num_2 = list(filter(lambda x : x % 5 == 0 , num_list))
print(multi_num_2)


# Square of a number---
square = lambda x : x * x
s = square(4)
print(s)