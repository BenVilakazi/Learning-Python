#Lists & List Functions & Operations in Python

friends = ["Mike", "James","Rob","Luke"]
friends[1] = "Paul" #appends new value of 2nd index position

newfriends = ["Mark", "John", "Peter", "Andrew"]

abc = [] # empty lists
print(friends)
print(friends[2]) #checks 3rd index position

### Operations 

print(friends+newfriends) #adds two lists together
print(friends*3) #multiply lists
print("Apple" in friends) #check whether the mentioned value is found within the list

### Functions

friends.append("Steve") #adds new item to list
print(friends)

print(len(friends)) #calculates length of list

friends.insert(3,"Amanda") #inserts a value in chosen position
print(friends)

print(friends.index("Rob")) #checks index position of listed item









