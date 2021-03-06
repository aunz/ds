# Differences between R and Python

## General

| | R | Python |
|---|---|---|
| History | 1993 | 1991 |
| Objective | Statistics | General purpose |
| Learning curve | Hard at first | Smooth |
| IDE | RStudio | Many: PyCharm, Spyder, Ipthon Notebook |


## Syntax



### Index
 
R is based 1
```R
numbers = c(1, 2, 3, 4, 5)
numbers[0] # -> numeric(0)
numbers[1] # -> 1
numbers[2] # -> 2
numbers[5] # -> 5
numbers[6] # -> NULL
```
Python is based 0
```Python
numbers = [1, 2, 3, 4, 5]
numbers[0] # -> 1
numbers[1] # -> 2
numbers[2] # -> 3
numbers[5] # -> IndexError: list index out of range
```

### White space

R is NOT white space sensitive
```R
a = 1
  b = 2 # OK
```

Python is white space sensitive
```Python
a = 1
 b = 2 # IndentationError: unexpected indent
```

### Reference

R copies by value
```R
a = c(1, 2, 3)
b = a
b[1] = 2
a # c(1, 2, 3)
```

Python copies by reference for array, object
```Python
a = [1, 2, 3]
b = a # copy a
b[0] = 2 # change b[0]
a # [2, 2, 2], a is changed

a = { 'k': 1 }
b = a
b['k'] = 2
b['l'] = 3
a # { 'k': 2, 'l': 3 }

# but not primitives like num or string
a = 1
b = a # copy a
b = 2 # change b
a # 1, a is still 1
```

### Data type
R
```R
typeof(1) # double
typeof(1L) # integer
typeof(1i) # complex
typeof(NA) # logical
typeof(NULL) # NULL
typeof(TRUE) # logical
typeof('a') # character
typeof(c(1, 2, 3)) # double
typeof(list(1, 'a', NA)) # list
typeof(function() {}) # closure
typeof(data.frame(a = 1:3)) # list

class(1) # numeric
class(1L) # integer
class(1i) # complex
class(NA) # logical
class(True) # logical
class('a') # character
class(c(1, 2, 3)) # numeric
class(list(1, 'a', NA)) # list
class(function() {}) # function
class(data.frame(a = 1:3)) # data.frame
```
Python
```Python
type(1) # int
type(1j) # complex
type(1.0) # float
type(None) # NoneType
type(True) # bool
type(False) # bool
type('a') # str
type((1)) # tuple
type([1]) # list
type({ 'a': 1 }) # dict
type({1, 2, 3}) # set
type(lambda: 1) # function
```
R and Python both have primitive types such as integer, double in R (float in Python), character i R (str in Python).

NULL in R, None in Python

In R, a sequence of cells such as `c(1, 2, 3)` or `list(1, 2, 3)` is a vector. While `c(1, 2, 3)` can only contain the same data type, `list(1, 2, 3)` can contain mixed types. Arrays in R contain 2 or more dimensions and are created by `array()` or `matrix()`. In Python, arrays are created by `[]` and each element can be of any type.

Python also has tuple, set, dict. Dict can be emulated in R with `list()` such as `l = list(number = 1, char = 'a')`, elements can be accessed by `$` or `[[]]` such as `l$number` or `l[['number']]`. In Python, values in a dictionary such as `d = { 'number': 1, 'char': 'a' }` can be accessed by `[]`: `d['number']`


### Cool features in R

#### Many built-in objects and functions for stats
```R
# a quick sequence of number
n = 1:3 # 1, 2, 3. In Python, it has to be written as: list(range(1, 4))

data.frame # construct data frame

# the apply families!
lapply, sapply, tapply, mapply, apply, aggregate, by, Map

# a special function to call a function with a list of arguments
do.call

# explicit environment
e = new.env()

# formular syntax
lm(x ~ y, data)
```

#### [non-standard evaluation](http://adv-r.had.co.nz/Computing-on-the-language.html#nse)
```R
library(data.table)
dt = data.table(a = 1:10)

dt[a > 5] # no quotes needed, succinct. If using Python Pandas, it is: dt[dt['a'] > 4]

with()
transform()
subbset()
```


### Cool features in Python

#### Slice syntax
```Python
n = list(range(4)) # [0, 1, 2, 3]
n[2:] # [2, 3]
n[:2] # [0, 1]
```

#### arguments with * and **
```Python
a = [1, 2, 3]
print(*a) # same as print(a[0], a[1], a[2])
```

#### List and dict comprehension
```Python
n = list(range(4)) # [0, 1, 2, 3]
[i ** 2 for i in n] # [0, 1, 4, 9]
{ i: i ** 2 for i in n } # { 0: 0, 1: 1, 2: 4, 3: 9 }
```
