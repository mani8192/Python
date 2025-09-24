# ---  Tuple in python --
 
 # with parenthess --
tuple = (1,2,3,"manish" , True)
print(tuple , type(tuple))     


# without prenthess--
t = 1,2,3,4,"tiwari"
print(t)



# 3. Accessing Tuple Elements--
# Indexing:--

ind_tup = (1,2,3,4,5,"manish","anaya")
print(ind_tup[5])  #positive indexing -
print(ind_tup[-1])  # negative indexing -




# 4. Slicing Tuples--
tuple_data = (1,2,3,4,5,6,"manish" , "anaya","apple" , "banana" , "you")
print(tuple_data[0:9])
print(tuple_data[:4])
print(tuple_data[:-1])


# tuple length --
tule_len = ("blue" , "green" , "apple" , 12,43,54,76 ,"toreto")
print(len(tule_len),tule_len)


# iterating a tuple --
class_student = ("manish" , "kelly" , "cristion" , "massi")
l = len(class_student)
print(class_student,l)

for i in range(l):
    print(class_student[i])
# for i in class_student:
#     print(i)



#  checking element is exists--

best_players = ( "Cristiano Ronaldo","Lionel Messi", "Kylian Mbappé", "Erling Haaland", "Neymar Jr")
if "Cristiano Ronaldo" in best_players:
    print("yes here-")
else:
    ("not here-")
    
    
#  concatnting in tuple --
t1 = (1,2,3,4,5)
t2 = (6,7,8,9,0)
t3 = t1 + t2
print(t3)


#  tuple method ----

# min,
# max,
# Index,
# count

check_num = (10,4,5,6,7,4,5,7,5,8)
print(min(check_num))  #min
print(max(check_num))  #max
print(check_num.count(5))   #count value
print(check_num[2])  # index value
