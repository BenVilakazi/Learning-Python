# creating Functions in Python & Reusing code

def function1(): # This is the function that will repeat will called
    print("Hello")
    print("World")
    print("I am a Function!")
    
function1() # This will call back the function and execute the code within the function 

### Passing an argument through a function 

def add(a,b):
    print(a+b)
    
add(7,8)


### Functions returning a value 

def adds ( a,b):
    c = a + b
    return c

result = adds(12,14)

print(result)