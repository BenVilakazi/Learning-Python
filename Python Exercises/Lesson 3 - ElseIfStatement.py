#Else if Statement in Python

a = int(input("Enter Value for A"))
b = int(input("Enter Value for B"))
c = int(input("Enter Value for C"))
d = int(input("Enter Value for D"))
e = int(input("Enter Value for E"))
f = int(input("Enter Value for F"))

APS = (a+b+c+d+e+f)

if APS >= 21:
    print("You've qualified for a Bachelor Degree")
    
elif APS == 19:
    print("You've qualified for Diploma studies")
    
else:
    print("You've qualified for Higher Certificate")