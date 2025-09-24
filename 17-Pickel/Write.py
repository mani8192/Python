
list = [1,2,3,4,5,6,7]

import pickle


file = open("Data.txt" , "wb") 
pickle.dump(list,file)
file.close()

#  open--
file = open("Data.txt" , "rb")
a = pickle.load(file)
print(a)