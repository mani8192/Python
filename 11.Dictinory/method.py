# Dectionary method in python----

my_dict = {
    "name": "John Doe",
    "age": 25,
    "country": "India",
    "language": "Python",
    "hobby": "Photography",
    "device": "Laptop",
    "brand": "Apple",
    "subject": "Mathematics",
    "city": "Mumbai"
}


# get a key and value 
l = my_dict.get("name")    #get only one value at a time()--
print(l)   

for i in my_dict:   # print a both key and value--
    print(i ,":", my_dict[i])
    
    
    
for i in my_dict.keys():  # get a all keys from dict --
    print(i)
    
    
for v in my_dict.values():   # get a all values from dict --
    print(v)   
    

for key , value in my_dict.items():
    print(key ,":",value)
    
    
# del keyword in dictionry----

my_dict = {
    "name": "Manish",
    "age": 21,
    "country": "India",
    "language": "Python",
    "hobby": "Coding",
    "city": "Delhi",
    "profession": "Web Developer",
    "favorite_food": "Paneer Butter Masala",
    "sports": "Cricket",
    "goal": "Become a successful software engineer"
}

del my_dict["sports"]  #delete a key and value --
print(my_dict)




# POP delete 
print(my_dict.pop("city"))
print(my_dict)



# Uppdate a value --
d = my_dict.update({"profession":"AI Devloper"})
print(d)



m = dict(name = "mansih" , age = 21 , cource_duration = "6Month")  #way of cretae dictinory--
print(m)



# key and value insert in dict--
my_dict['cloud']='Aws'
print(my_dict)


my_dict.clear()   # clear a complete dict--
print(my_dict)




