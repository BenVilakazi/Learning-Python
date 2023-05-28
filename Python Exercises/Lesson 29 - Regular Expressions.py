### Regular Expressions in Python

import re 

pattern = r"eggs"

if re.match(pattern,"eggseggseggs"):
    print("match found")
else:
    print("No matches found")
    
### Search & Find All function

if re.search(pattern,"baconeggseggsbacon"):
    print("Match found")
else:
    print("No match")
    
    
if re.findall(pattern,"baconeggseggsbacon"):
    print("Match found")
else:
    print("No match")
    
print(re.findall(pattern,"baconeggseggsbaconeggas"))

### Find & Replace function

string = "Hi, My name is John"
pat = r"John"
newstr = re.sub(pat, "Slimshady",string)
print(newstr)