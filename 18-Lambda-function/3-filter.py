# filter() --

students = [
    {"student_name": "John", "father_name": "Michael", "age": 21, "country": "USA"},
    {"student_name": "Aarav", "father_name": "Rakesh", "age": 19, "country": "India"},
    {"student_name": "Sophia", "father_name": "William", "age": 22, "country": "Canada"},
    {"student_name": "Yuki", "father_name": "Hiroshi", "age": 18, "country": "Japan"},
    {"student_name": "Carlos", "father_name": "Miguel", "age": 25, "country": "Mexico"},
    {"student_name": "Fatima", "father_name": "Ahmed", "age": 20, "country": "UAE"},
    {"student_name": "Emma", "father_name": "Robert", "age": 17, "country": "UK"},
    {"student_name": "Liu Wei", "father_name": "Liu Feng", "age": 23, "country": "China"},
    {"student_name": "Oliver", "father_name": "James", "age": 24, "country": "Australia"},
    {"student_name": "Hana", "father_name": "Omar", "age": 19, "country": "Egypt"}
]


# Find students older than 20.
older = list(filter(lambda student : student['age'] > 20 , students))
print(older)

# Find students from India.
indian_stu = list(filter(lambda ind_stu : ind_stu["country"] == 'India' , students))
print(indian_stu)

# Find students whose age is less than 19.
stu = list(filter(lambda less_age : less_age['age'] < 19 , students))
print(stu)

# Find students from countries starting with “U”.
u_contry = list(filter(lambda u_country : u_country['country'][0] in 'U' , students))
print(u_contry)

# Find all students with age between 18 and 22.
age = list(filter(lambda age : (age['age'] == 18 | age['age'] < 22), students))
print(age)