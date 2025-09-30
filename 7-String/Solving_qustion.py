# 3. Strings---

# @1----Take a string and print it in reverse.

name = "we learn python"
print(name[::-1])

# @2-----Count the number of vowels in a string.

user_text = input("Enter a vowel :-").lower()
word = "aeiou"
count = 0

for ch in user_text:
    if ch in word:
        count = count +1 
        print("this is vowel")
        
# @3----Replace all spaces in a string with -.

name = "manish tiwari"
print(name.replace(" " , "_"))
