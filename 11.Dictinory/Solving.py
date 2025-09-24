# Basic Level----  in dictionary 


# @1-----Create a dictionary of 5 fruits with their prices and print each fruit with its price.

fruits = {
    "Apple": 120,
    "Banana": 40,
    "Mango": 150,
    "Orange": 80,
    "Grapes": 90,
    "Pineapple": 70,
    "Papaya": 60,
    "Watermelon": 50,
    "Strawberry": 200,
    "Kiwi": 100
}

print(fruits)
fruits ["Mango"] = 200   #udate mango price--
fruits["cherry"] = 150 #add new element--
fruits.pop("Banana")  # delete a spesfic element--
for a in fruits.keys():
    print(a)
for b in fruits.values():
    print(b)
print(fruits)


# @2-----Write a program to get the value of a specific key from a dictionary.
for x , y in fruits.items():
    print(x,":",y)



# @3----Add a new key-value pair to an existing dictionary.

fruits["angur"] = 90
print(fruits)

# @4----Remove a key from a dictionary using pop().

fruits.pop("Mango")
print(fruits)

# @5----Check if a key exists in a dictionary.

if "Orange" in fruits:
    print("this fruits availble in store")
else:
    print("not availble")
    
    
# @6----- Create a dictionary of 5 students with their marks and print the student with the highest marks.

student = {
    "manish" :89,
    "anaya" :90,
    "pankaj" :98,
    "kelly": 88,
    "harsh": 78,
    
    }

top_student = max(student , key=student.get)
print("A student is -" , top_student , "top with" , student[top_student])





# @7----- Merge two dictionaries into one.

# stu1 = {
#     "name" : "mansih",
#     "age" : 21,
# }

# stu2 = {
#     "name" : "anaya",
#     "age" : 20,
# }

# merge_dict = stu1 | stu2
# print(merge_dict)


#  @8 ----Create a nested dictionary for 3 students (name, age, marks) and print each student's details.



stdents = {
    
"stu5" : {
    "name": "mansih",
    "age": 21,
},

"stu2" :{
    "name": "anaya",
    "age": 20,
},

"stu3" :{
    "name" : "pankaj",
    "age":22,
    
},

}

l = (stdents["stu5"])
print(l)


stdents["stu5"] ["name"] = "mansih tiwari"
print(stdents)
