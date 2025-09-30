# string in python ---

# Important: Strings are Immutable
# 1. What is a String----

# A string is a sequence of characters (letters, numbers, symbols) inside quotes.

name1 = "mansish tiwari" 
name2 = 'mani'
name3 = """manish"""
print(name1,name2,name3)

# 2. String Indexing--

name = "mansih tiwari"
print(name[0])  #from starting 

print(name[-1])  #from ending -1

cource = "python"
print(cource[4])


intro = "we are learn about python"
print(intro[8])
print(intro[-4])




#  String Slicing----

name = "manish tiwari"
print(name[2:5])
print(name[0:])
print(name[:7])



# 4. String Functions (Methods)---

student_name = "manish tiwari"
print(len(student_name))   # lenght
print(student_name.upper()) #upperCase
print(student_name.lower())  #LowerCase
print(student_name.strip())  #remove extra space
print(student_name.replace("tiwari" , "python"))  #replace a data


# 5. String Search--

color = "green"
print(color.find("ree"))
print(color.count("n"))


# 6. String Concatenation & Repetition--
x = "manish"
y = "tiwari"

print (x + " " +y)
print(x*3)



#  7.Loop Through a String--

name = "mansih tiwari"
for i in name:
    print(i)


# 8. f-string--

name = "manish tiwari"
age = 21
cource = "pyhton"

print(f"my name is {name} age {age}  i learn {cource}")
