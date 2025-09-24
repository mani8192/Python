def student ():        # function define--
    print("welcome to function class")
    

student()     #function call --

# ==-=======

def sumdata (a , b=5):
    print(a+b)
    
sumdata(20)
    
    # =========
    

list = [2,3,4,5,6]

def check (num_check):
    m = max(num_check)
    return m


l = check(list)
print(l)
    
    
    #  -----
    
def even_odd ():
    num1 = int(input("Enter a first :-"))
    if num1 % 2==0:
        print("even number :-")
        
    else:
        print("Odd number :-")
    return num1

m = even_odd()
print(m)

