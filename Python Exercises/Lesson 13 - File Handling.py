file = open("demo.txt",'w')
#perform an operation
file.close()

### Reading data from file

file = open("demo.txt",'r')
content = file.read()
print(content)
file.close()

#### You can specify how much data you require from a file

file = open("demo.txt",'r')
content = file.read(10) #This will take only 10 bytes of data from the file
print(content)
file.close()

### you can read only line with the readline function

file = open("demo.txt",'r')
content = file.readline()
print(content)
file.close()

### Adding data to the file

file = open("demo.txt", 'w')
file.write("The following text will be added to our file")
file.close()

