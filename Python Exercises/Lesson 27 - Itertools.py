## Itertools in Python

from itertools import count

for x in count(20):
    print(x)

    if x >= 20:
        break

### Accumulate function

from itertools import accumulate, takewhile 

numbers = list(accumulate(range(30)))
print(numbers)

### Take while function

print(list(takewhile(lambda x: x <= 120,numbers)))