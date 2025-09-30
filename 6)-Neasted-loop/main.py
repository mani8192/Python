# nested loop --

for i in range(1,11):
    for j in range(1 ,10):
        print(f"i={i} - j={j}")
        
        
        
# pattern --

for i in range(1 , 5):
    for j in range(1 ,5):
        print("*" , end = "")
    print()
    
# pattern 2 --

'''
*
* *
* * *
* * * *
* * * * *
'''

n = 5
for i in range(1, n + 1):
    for j in range(1 , i +1):
        print("*" , end = " ")
    print()
    

print('-' * 20)  #for line
# -------------

m = 5
for i in range(m - 1 , 0 , -1):
    for j in range(i):
        print('*' , end = " ")
    print()


 