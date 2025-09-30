# class and object in python --

# Creating a class ---
class Student ():
    def __init__(self,name1,age1):   #Constructor 
        self.name = name1
        self.age = age1
        
        
    def Welcome (self):
        print("Hello Student")
    
    
    def display_data(self):
        print(f"name :- {self.name}  | age :-{self.age} ")
  
  
    
# Creting a object --
s1 = Student("manish" ,21)
s2 = Student("anaya" , 20)
s3 = Student("harsh" , 22)
s4 = Student("pankaj" ,19)

s1.display_data()
s2.display_data()
s3.display_data()
s4.display_data()

s1.Welcome()






# create a student class that take & marks of student or argument in constructor then create to print the avrage --

class student ():
    def __init__(self , name , marks):
        self.name = name 
        self.marks = marks
        
    def avg_marks(self):
        num = 0
        for val in self.marks:
            num +=val
            
        avg = num / len(self.marks)
        print(f"A student is {self.name} avrage of score {avg}")
        
        
s1 = student("mansih" , [90,99,89])
s1.avg_marks()


        
        
        
        
        
        