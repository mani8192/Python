# reduce () --

# form functools  import reduce
# num_list = [2,4,5,6,7,8,9]

from functools import reduce


# addition -
num_list = [2,3,4,5,6]
num_sum = reduce(lambda  x , y: x + y , num_list)
print(num_sum)

# multi--

num_multi = reduce(lambda x , y : x * y , num_list)
print(num_multi)

big_num =  reduce(lambda x , y : x if x > y else y , num_list)
print(big_num)
