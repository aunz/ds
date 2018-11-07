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
numbers[0] # -> NULL
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
 b = 2
```
