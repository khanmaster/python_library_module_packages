# Python Library, Module and Packages

### Let's have a look at some built in functions in python
### most languages have built in methods and we will see how can we take advantage of them in python
``` python
import random
# we have a random method in python library which we can use by importing it here

print(random.random())
# let's what is does
each time it generates a random float number between 0-1
```
- 2nd iteration - comment out the above code
- We'ill simplify it even further by using from import statement together to remove the need to call the basse random object
```python
from random import random

print(random())
This will produce the same result but keeps our code clean and readable
```
- Let's see how can we use multiple packages from python library

- we'll add a package called math

- comment out the above code

``` python
from random import random
import math

print(" This number is generated randomly using the RANDOM method " + str(random()))

# Let's creata variable and assign float value
num_floar = 23.66

# Let's see what we can do with our math functions
print("floor method will round the figure to 23 from 23.66, to the lower end")
print(math.floor(num_floar))

print("ceil method will round the figure to 24 from 23.66, to the higher end of the float value")
print(math.ceil(num_floar))
``` 
```markdown

exercise:

get user input of a float number
check if the number is greater than .50 then round the figure to lower end
check if the number is greater than .51 then round the figure to higher end
example - num_float = 23.66 - round it to 24, num_float = 23.50 - round it to lower end
tips - get help online - python library
```