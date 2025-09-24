import my1

print(my1.sum(1,2))
print(my1.multi(10,4))



# using a from -- 
from my1 import multi
print(multi(10,2))


# using * for call all function --
from my1 import *
print(multi(9,8 ))