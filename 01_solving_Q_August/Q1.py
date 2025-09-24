# Reverse a string without using slicing.--

string = "Manish tiwari"

reversed_str = ""
for char in string:
    reversed_str = char + reversed_str
print(reversed_str)