#stacke and queue in python --

list = []   # empty list-

while True:
    user_choise = int(input('''
        1 Push Element
        2 Pop Element
        3 Peak Element
        4 Display stack
        5 Exit 
        '''))

# append --

    if user_choise == 1:
        user_detail = input("Enter hare :-")
        list.append(user_detail)   #Append a value in list
        print(list)


# Pop -remove a last element --
    if user_choise == 2:
        if len(list) == 0:
            print("Empty list :-")
        else:
            l = list.pop()  # remove a last element from list--
            print(l, ":-", "value delet from list")
            print(list)

# Peak--
    if user_choise == 3:
        if len(list) == 0:
            print("Emptylist :-")
        else:
            print("a peak value of list", list[-1])
            print(list)


# Display --
    if user_choise == 4:
        print("your list now:-", list)


# Exit --
    if user_choise == 5:
        break

# -----
    else:
        print("invalid number ")