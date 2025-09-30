# map ()


# 1 --Even odd
num_list = [1,2,3,4]

even_odd = list(map(lambda x : x % 2 == 0 , num_list))
print(even_odd)


# 2 -- square 
num_list1 = [2,4,6,8,10]
square = list(map(lambda x : x ** 2 , num_list1))
print(square)


# Add 5 to each number in a list--
x_list = [1,2,3,4,5]

new_list = list(map(lambda x : x + 5 , x_list))
print(new_list)  # 6,7,8,9,10



# print 10  number using loop
number = list(map(lambda x : x , range(1,11)))
print(number)


# get each student name --
students = [
    {
        "student_name": "John",
        "father_name": "Michael",
        "age": 21
    },
    {
        "student_name": "Sophia",
        "father_name": "Robert",
        "age": 20
    },
    {
        "student_name": "Liam",
        "father_name": "David",
        "age": 22
    }
]

stu_data = list(map(lambda student : (student['student_name'],student['age']) , students))
print(stu_data)



# Q2 --
students = [
    {"student_name": "Amit", "father_name": "Rakesh", "age": 21, "country": "India"},
    {"student_name": "Anita", "father_name": "Mahesh", "age": 18, "country": "India"},
    {"student_name": "John", "father_name": "Michael", "age": 22, "country": "USA"},
    {"student_name": "Sophia", "father_name": "David", "age": 19, "country": "UK"},
    {"student_name": "Ravi", "father_name": "Mukesh", "age": 23, "country": "India"},
    {"student_name": "Ali", "father_name": "Omar", "age": 20, "country": "UAE"},
    {"student_name": "Emma", "father_name": "Robert", "age": 17, "country": "UK"},
    {"student_name": "Liam", "father_name": "David", "age": 22, "country": "USA"},
    {"student_name": "Fatima", "father_name": "Ahmed", "age": 20, "country": "UAE"},
    {"student_name": "Carlos", "father_name": "Miguel", "age": 24, "country": "Mexico"}
]

# Get only student names from the list.
student_name = list(map(lambda names : names['student_name'],students))
print(student_name)

# Get only ages of all students.
student_age = list(map(lambda age : age['age'] , students))
print(student_age)

# Create a list of strings: "Name - Age" for each student.
a_name = list(map(lambda a_names : a_names['student_name'][0] =='A',students))
print(a_name)

# Convert all student names to uppercase.
upper_name = list(map(lambda name : name['student_name'].upper() , students))
print(upper_name)