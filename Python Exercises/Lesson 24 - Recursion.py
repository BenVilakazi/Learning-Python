### Recursion in Python 

def factorail(x):
    if (x == 1):
        return 1
    else:
        return x*(factorail(x-1))
    
result = factorail(8)
print(result)