# file heandling --

# read mode --
f = open('demo.txt' , 'r')
data = f.read()
print(data)
f.close()


# write mode  ---
f2 = open('line2.txt' , 'w')
write_data = f2.write('hello - python / hii --')
print(write_data)
f2.close()


# read one line --
f3 = open('demo.txt' , 'r')
line = f3.readline()
print(line)


# if i change a data in same folder --

newf = open('demo.txt' , 'w')
newf.write('hello - now i learn js')
newf.close()


# append new data in same folder --
appnew = open('demo.txt' ,'a')
appnew.write('\nand learn python--')
appnew.close()
