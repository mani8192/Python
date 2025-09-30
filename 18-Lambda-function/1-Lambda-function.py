# lamda function --

# lambda argument : expresion 
sum = lambda x , y : x + y
s = sum(2 , 8)
print(s)


# check odd or even -
odd_even = lambda x : 'even' if x % 2 == 0 else 'odd'
print(odd_even(4))


# first charecter is "a"
check = lambda x : x[0] == 'a'
print(check('anna')) 


# for solving --

# Write a lambda function to multiply two numbers.
multi = lambda x , y : x * y
print(multi(2,8))

# Write a lambda function to find the cube of a number.
cube = lambda x : x ** 3
print(cube(3))

# Write a lambda function that checks if a number is positive or negative.
num_check = lambda x : 'positive' if x > 0 else('negative' if x < 0 else 'Zero')
print(num_check(2))

# Write a lambda function to return the length of a string.
len_str = lambda x : len(x)
print(len_str('manish'))


# ==================


def return_sum(num_list, func):
    result = 0
    for i in num_list:
        if func(i):
            result = result + 1 
    return result  

num_list = [22, 3, 4, 55, 66, 77, 87, 87, 54, 34, 54, 66, 76]

num1 = lambda x: x % 2 == 0   
num2 = lambda y: y % 2 != 0   
num3 = lambda z: z % 3 == 0    

print("Even numbers count:", return_sum(num_list, num1))
print("Odd numbers count:", return_sum(num_list, num2))
print("Divisible by 3 count:", return_sum(num_list, num3))

