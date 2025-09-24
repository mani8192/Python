# For loop in python --

# print a number-
for i in range(1,10):
    print(i)
    
    
    
employees = [
    {
        "name": "Rajesh Kumar",
        "age": 28,
        "work": "Software Engineer",
        "mobile_number": "9876543210",
        "id": "EMP001"
    },
    {
        "name": "Priya Sharma",
        "age": 25,
        "work": "Web Developer",
        "mobile_number": "9876543211",
        "id": "EMP002"
    },
    {
        "name": "Ankit Verma",
        "age": 30,
        "work": "Data Analyst",
        "mobile_number": "9876543212",
        "id": "EMP003"
    },
    {
        "name": "Neha Singh",
        "age": 27,
        "work": "UI/UX Designer",
        "mobile_number": "9876543213",
        "id": "EMP004"
    },
    {
        "name": "Manish Tiwari",
        "age": 24,
        "work": "Python Developer",
        "mobile_number": "9876543214",
        "id": "EMP005"
    },
    {
        "name": "Pooja Patel",
        "age": 26,
        "work": "HR Manager",
        "mobile_number": "9876543215",
        "id": "EMP006"
    },
    {
        "name": "Amit Yadav",
        "age": 29,
        "work": "Network Engineer",
        "mobile_number": "9876543216",
        "id": "EMP007"
    },
    {
        "name": "Sneha Gupta",
        "age": 23,
        "work": "Front-End Developer",
        "mobile_number": "9876543217",
        "id": "EMP008"
    },
    {
        "name": "Rahul Mehta",
        "age": 31,
        "work": "Project Manager",
        "mobile_number": "9876543218",
        "id": "EMP009"
    },
    {
        "name": "Kavita Joshi",
        "age": 22,
        "work": "Intern",
        "mobile_number": "9876543219",
        "id": "EMP010"
    }
]


print(type(employees))

for i in employees:
    print(i)
    
    
    
# reverse string --
for i in range (10 , 0 , -1):
    print(i)
    
    
# print a 2 table--
for i in range (1, 11):
    print(i , "* 2" , "=" , i*2 )
    
    