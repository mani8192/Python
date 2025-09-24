# Set in ptyhon --

# Create a set--

# @1--
my_set = {1,2,3,4,5,6}
print(my_set)

# @2--
my_set = set([1,2,3,4,5,6,7])
print(my_set)




#  itreat a set-data using loop---
lop_data = {"manish" , "tiwari" ,"python" , "anaya"}
for i in lop_data:
    print(i)



#  function in set --

"""
set()
add()
pop()
remove()
deccard()
update()
clear()
"""

set_data = {1,23,45,65,8,7,6,77}
set_data.add(88)   #Add a value
print(set_data)

set_data.pop()  #romve a rendom value from set-
print(set_data)

set_data.remove(45)  # passing value delete from set-
print(set_data)

set_data2 = (90, 99,97,89)  # new set --

set_data.update(set_data2)  #update a set withou any changes-
print(set_data)

set_data.clear()  # clear all data in set--
print(set_data)    




#  solving qustion in set ---


# Q1 – Create a set of 5 numbers and add two more numbers to it.
Q1_set = {1,2,3,4,5}
add_set = {6,7,8}
Q1_set.update(add_set)
print(Q1_set)


# Q2 – Remove one item from a set using remove().
Q1_set.remove(3)
print(Q1_set)