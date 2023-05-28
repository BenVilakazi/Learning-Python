#### Types of errors

SyntaxError ### a grammatical error in coding language

LogicalError = "inaccurate output" ### code performs incorrectly 

exceptions = "will cause program to terminate, hault process"

### Handling exceptions

try:
    a = 20
    b = 10
    print(a/b)
except ZeroDivisionError:
    print("There is a divide by zero error")
    
### Finally Block (this block of code will execute no matter what)

finally:
    print("Nothing can stop me, I will run no matter what")

