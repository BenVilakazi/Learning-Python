

def function():
    counter = 0 
    while counter < 5:
        yield counter # creates the generator 
        counter += 1 
        
for x in function():
    print(x)
    

def evenNumbers(x):   # this generator will create a list of even numbers
    
    for i in range(x):
        if i % 2 == 0:
            yield i
            
            
print(list(evenNumbers(21)))

            
