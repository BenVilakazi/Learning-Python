### String formatting in Python

# numbers = [4, 5, 7]
# newstring ="numbers:[0][1][2]".format(numbers[0][1][2]) ## This will convert our list values into a string 
# print(newstring)

### String Functions

print(",".join(["Apple", "Mango", "Orange"])) # This function will separate each list item with a ,

### Replace function

print("Hello there".replace("there","World")) # with this function ypu have to specify which string you'd like to replace and with and the replacement string

oldstring = "Yo, what it do? my dunkin-donuts"

print(oldstring.replace("what it do?", "what does it do?"))

stri = " a random set of words"
print(stri.startswith("is")) ## This function checks if a string starts with the specified word
print(stri.endswith("words")) # TEhis function check what a particullar string ends with