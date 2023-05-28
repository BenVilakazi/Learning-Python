### Boolean logic in Python

username = input("Enter username")
password = input("Enter password")

if username == "Admin" and password == "admin123": 
    print("Valid user")
else:
    print("Unknown user")
    
username = input("Enter username")
password = input("Enter password")

if username == "Admin" or password == "admin123": 
    print("Valid user")
else:
    print("Unknown user")