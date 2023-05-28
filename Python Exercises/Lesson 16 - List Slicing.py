### List Slicing

names = ["Mary", "Mark", "Luke", "John","James", "Paul"]

print(names[2:5]) # This will slice the list and only print from index 2 till 5
print(names[:3]) # This will print all the values before the 3rd index
print(names[3:]) # This will print all the values after the 3rd index
print(names[::2]) # This will only print every 2nd value

### List Comprehension

list = [x**2 for x in range(5)] ## This is a rule that will define what is present in the list
print(list)

lists = [x**2 for x in range(10)  if x**2 % = 0] # This rule will only allow even numbers into the list
print(lists)