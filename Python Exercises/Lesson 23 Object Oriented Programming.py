### Object Oriented Programming in Python

class Students:
    
    def __init__(self, name, contact, age, adress,dateOfBirth): ## Defines class properties
      self.name = name
      self.contact = contact
      self.age = age 
      self.adress = adress
      self.dateOfBirth = dateOfBirth 
      
    def getdata(self): ## Requests user input in order to collect the required data
        print("Accepting Data")
        self.name = input("Enter name")
        self.contact = input("Enter contact")
        self.age = input("Enter age")
        self.adress = input("Enter adress")
        self.dateOfBirth = input("Enter date of birth")
        
    def putdata(self): ## This will output the collected data, this the function of this class collecting and outputting data
        print("The name is: "+self.name, "This is the contact: "+self.contact, "This is the age: "+self.age, "This is the adress: "+self.adress)
        
## The following code create an object in the above class

Luvuyo = Students("blank",0,0,"blank")
Luvuyo.getdata()
Luvuyo.putdata()

### Object Inheritence in Python

class PythonStudents(Students): #This line lets this class inherit the properties & methodology of the above class
    def __init__(self,status):
        self.status = status 
        
        
    def Python(self):
        print("I Am a Python Student")
        
Ben = PythonStudents("Single")
Ben.getdata()
Ben.putdata()
Ben.Python()

### Hiding Data in Python

class Myclass:
    __hiddenvariable = 0 # putting double underscore bofre the variable will make it hidden and inaccessible outside this class
    
    def add(self,increment):
        self.__hiddenvariable += increment 
        print(self.__hiddenvariable)
        
    object1 = Myclass()
    object1.add(5)
    ## print(object1.__hiddenvariable)  This line would result in an error because it would be able to acess the hidden code
    