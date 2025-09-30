# convert string to a list progrsm--

# input from user --

user = input("Enter a vslue")

l = user.split()
print(l)


# take a multiple input from user and convert to string --


list = []
for i in range(1,5):
    user = input("Enter a value" + str(i))
    list.append(user)
    print(list)
    