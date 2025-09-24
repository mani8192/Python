# list in python ----

l = ["manish" , "aryan" , "pankaj" , "tiwari" , 57]
print(l,type(l))


marks = [56,75,45,77,87,90,88]
print(marks)  #print a marks -
print(type(marks))  # type -
print(marks[0])  # index number find--


#  List Indexing--
color = ["red","green" , "blue","white","black","purple"]
print(color[1])
print(color[-1])




# 3. List Slicing
data = ["manish" , "pankaj" , "himanshu" , "tiwari" , "thor" , "marvel" , "banana"]

print(data[0:5])
print(data[:3])
print(data[0:])



# 4. List Methods---

list = [2,3,4,5,6,7,8,9,0]
list.append(11)  #add the end -
print(list)

list.remove(6) # remove element -
print(list)

list.pop(1)  #remove item at index
print(list)

list.sort()  # sort in asceending order(1,2,3,4)
print(list)



# 5. Searching & Counting--

employee = ["manish" , "manish", "sanju","Himanshu" , "nidhi","anaya"]
print(employee.count("manish")) # count element -
print(employee.index("anaya"))  # find index number -


# nested list --

num = [1,2,3,[4,5,6]]
print(num[3] [2])



# ----- 
list = [1,2,3,4,5,6,7,8]
print(max(list))
print(list[1: : 2])



# list--loop--
# @1 --
lm = [1,2,3,4,5,6,7,8]
for i in lm:
    print(i)


# @2 --
program = ["python" , "C++" , "java" , "R" ,"java script" , "C#"]
for i in program:
    print(i)
    
    
    
#@--3  
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple", "Watermelon", "Papaya", "Strawberry", "Kiwi"]

print(fruits)
t = len(fruits)
for i in range(t):
    print(fruits[i])
    
    
list = [1,2,3,4,5,6,7,8]
print(max(list))