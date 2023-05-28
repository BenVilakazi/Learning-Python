### Data Structures (Dictionaries)

people = {"John":32, "Mary":27}
print(people["John"])

### Dictionary functions

numbers = {
    1:"one",
    2:"two",
    3:"three",
}

print(1 in numbers) ### checks if particular key is found in the mentioned dictionary (boolean  )

print(numbers.get(2)) # the get function maps a key to its value and prints the value

print(numbers.get(5, "key not found")) ### the specified message will be printed out if result not found instead of "None"