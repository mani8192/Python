# Nested dictionry in python --

Student = {
    
    "stu1" :{
        "name" : "mansih tiwari",
        "age" :21,
        "Cource" : "Python",
        "fee" : 10000
    },
    
    
    "stu2" : {
        "name" : "anaya",
        "age" : 21,
        "Cource" : "web Devlopment",
        "fee" : 12000,
    },
    
     "stu3" : {
        "name" : "priya",
        "age" : 21,
        "Cource" : "cyber security",
        "fee" : 14000,
    },
    
}


print(Student["stu1"])   # get one dict --
d = len(Student)   #define lenght--
print(d)


# update a value --

# m = Student["stu3"].update({"fee" : 15000})
# print(m)
Student["stu2"]["fee"] = 200000

for a ,b in Student.items():
    print(a, "-",b)
    




