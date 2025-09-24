# Dictinory in python --


# 1️⃣ What is a Dictionary in Python?
# A dictionary is used to store data in key-value pairs.--
student_data = {
    "name" : "masish",
    "age" : 20,
    "cource" : "Python",
    "sudent_id" : [234534556]
}

print(student_data)


# 2️⃣ Creating a Dictionary


# dict1 ---
dict1 = {"name" :"manish tiwari" ,"age" : 20 , "contect" : 8279810}
print(dict1.values())
print(dict1.keys())

# using a dict word----
dict2 = dict(name = "anaya" , age=22 , cource="data-scince")
print(dict2)

# empty dict --

dict3 = {}
print(dict3)


# get a specfic value --
data_of_student = {
    "name": "manish",
    "age":21,
    "cource":"BCA",
    "stu_id" : [65554]
}

l = data_of_student["age"]
print(l)



#  using a for loop print a dictianory with key and value ----

my_dict = {
    "name": "Manish",
    "age": 20,
    "course": "Python",
    "city": "Delhi",
    "country": "India",
    "email": "manish@example.com",
    "phone": "9876543210",
    "grade": "A",
    "hobby": "Coding",
    "language": "English"
}


for a , b in my_dict.items():
    print(a , ":" ,b)

