# Chapter 3: An Informal Introduction to Python

This chapter covers the basics of Python programming.

## Python Data Types

### Numbers

#### Number Data Types
- int
- float

#### Number Operators
- / :- Division. Returns 'float'.
```
>>> 9 / 2
4.5
```
- // :- Floor division. Discards the fractional part.

```
>>> 9 // 2
4
```
- % :- Returns 'remainder' of the division.
```
>>> 9 % 2
1
```
- ** :- Power operator
```
>>> 3 ** 2
9
```

## Strings(Text)
```
>>> 'I want to be best at AI'
'I want to be best at AI'
```

### Multiline Strings
- String literals can span multiple lines by using """...""" or '''...'''.
```
>>> """
... I want to learn
... AI
... ML
... DL
... GenAI
... """
```

### General
- Strings can be concatenated or repeated with operators '+' and '*' respectively.
```
>>> 'AI' + 'ML' + 'DL'
'AIMLDL'

>>> 'AI' * 3
'AIAIAI'
```
- Breaking of long strings.
```
>>> text = (' I love AI and '
... 'Python')
>>> text
' I love AI and Python
```
- Strings can be indexed.
+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```
>>> word = 'Python'
>>> word[0]
'P'
>>> word[-1]
'n'
>>> word[0:2]
'Py'
>>> word[2:5]
'tho'
>>> word[:2]
'Py'
>>> word[2:]
'thon'
>>> word[-2:]
'on'
>>> word[:2] + word[2:]
'Python'
```

```
# Using index which is too large will cause Error.
>>> word[45]
Traceback (most recent call last):
  File "<python-input-23>", line 1, in <module>
    word[45]
    ~~~~^^^^
IndexError: string index out of range
```
- Strings cannot be changed. They are 'immutable'. If we need a new string we need to create new one.
```
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<python-input-25>", line 1, in <module>
    word[0] = 'J'
    ~~~~^^^
TypeError: 'str' object does not support item assignment
```

```
# New String
>>> 'J' + word[1:]
'Jython'
```

- 'len()' built in function returns length of a string.

### Lists
- contains list of 'items'. 'items' can be of any datatype. 

```
>>> even = [2,4,6,8]
>>> even = [2,'a']
```
- 'list' datatypes can be indexed and sliced.

```
>>> even = [2,'a']
>>> even[0]
2
>>> even[0:2]
[2, 'a']
>>> even[2:]
[]
>>> even[-1:]
['a']
```
- 'list' are 'mutuable'.

```
>>> even[0:2]
[2, 'a']
>>> even[1] = 4
>>> even
[2, 4]
```
- we can concatenate lists.
```
>>> even
[2, 4]
>>> odd = [1,3,5]
>>> numbers = even + odd
```
- We can add 'items' to end of list using 'list.append()' function.

```
>>> numbers
[2, 4, 1, 3, 5]
>>> numbers.append(6)
```

## Python Assignment
- Simple assignment never copies data. Below we have created new variable 'numbers2' and assigned it with 'numbers'. Instead of creating 2 objects in memory, Python points both variables 'number' and 'number2' to same memory location. If we change one variable(number) value other variable(numbers2) also changes because both point to same memory location.

```
>>> numbers
[2, 4, 1, 3, 5, 6]
>>> id(numbers)
4388831808
>>> numbers2 = numbers
>>> id(numbers2)
4388831808
```

```
>>> numbers
[2, 4, 1, 3, 5, 6]
>>> numbers[5] = 9
>>> numbers2
[2, 4, 1, 3, 5, 9]
```

- 'All Slice'([:]) operator returns new shallow copy which is new list of requested elements. Basically its create new object in memory.

```
>>> new_numbers_list = numbers[:]
>>> id(numbers)
4388831808
>>> id(new_numbers_list)
4388830464
>>> numbers[5] = 99
>>> numbers
[2, 4, 1, 3, 5, 99]
>>> new_numbers_list
[2, 4, 1, 3, 5, 9]
```

- Assignment of slices is possible and assigned list it can be any size.
```
>>> numbers
[2, 4, 1, 3, 5, 99]
>>> numbers[1:4] = [11,22,33,44,55,66]
>>> numbers
[2, 11, 22, 33, 44, 55, 66, 5, 99]
```

- 'len()' returns length of string.
```
>>> len(numbers)
9
```
- Its possible to create nested lists too.

```
>>> numbers
[2, 11, 22, 33, 44, 55, 66, 5, 99]
>>> numbers2
[2, 11, 22, 33, 44, 55, 66, 5, 99]
>>> nested_numbers = [numbers, numbers2]
>>> nested_numbers
[[2, 11, 22, 33, 44, 55, 66, 5, 99], [2, 11, 22, 33, 44, 55, 66, 5, 99]]
```