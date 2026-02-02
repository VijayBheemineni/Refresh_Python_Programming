# Chapter 5: Data Structures

This chapter covers Python's built-in data structures including lists, tuples, sets, and dictionaries.

# More on Lists
- 'insert', 'remove' or 'sort' methods modify the list and return None. 

## Using Lists as Stacks
```
>>> llms = ["chapgpt", "claude", "gemini"]
>>> llms.append("Llama")
>>> llms.append("Grok")
>>> llms
['chapgpt', 'claude', 'gemini', 'Llama', 'Grok']
>>> llms.pop()
'Grok'
>>> llms
['chapgpt', 'claude', 'gemini', 'Llama']
```

## Using Lists as Queues
```
# dqeue :- double ended queue
>>> from collections import deque
>>> llms = deque(["chapgpt", "claude", "gemini"])
>>> llms.append("Llama")
>>> llms.append("Grok")
>>> llms
deque(['chapgpt', 'claude', 'gemini', 'Llama', 'Grok'])
>>> llms.popleft()
'chapgpt'
>>> llms
deque(['claude', 'gemini', 'Llama', 'Grok'])
```

## List comprehensions

```
>>> llms_new_version = [model + "_v1" for model in ["chatgpt","claude","gemini"]]
>>> llms_new_version
['chatgpt_v1', 'claude_v1', 'gemini_v1']
```
```
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
```

```
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
>>> [[row[n]for row in matrix] for n in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

# The 'del' statement
- 'del' statement can be used to remove slices from a list or clear entire list.
```
>>> matrix
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
>>> del matrix[0]
>>> matrix
[[5, 6, 7, 8], [9, 10, 11, 12]]
```
- It doesn't return anything(None). 'pop()' method returns the 'item'.
- Can aslo be used to delete variables.

```
>>> del matrix
>>> matrix
Traceback (most recent call last):
  File "<python-input-27>", line 1, in <module>
    matrix
NameError: name 'matrix' is not defined
```

# Tuples and Sequences
- Consists of values seperated by commands
```
>>> t = 1,'a','b'
>>> t
(1, 'a', 'b')
```

- Tuples are immutable.
```
>>> t[0] = 9
Traceback (most recent call last):
  File "<python-input-30>", line 1, in <module>
    t[0] = 9
    ~^^^
TypeError: 'tuple' object does not support item assignment
```
- Creating tuples with 0 or 1 items.

```
>>> empty = ()
>>> one = 1,
>>> empty
()
>>> one
(1,)
```
- Packing and unpacking
```
# Packing
>>> t = 1, 2, 3
# Unpacking
>>> a, b, c = t
>>> a
1
>>> b
2
>>> c
3
```

# Sets
- is an 'unordered' collection with no 'duplicate' elements.
```
>>> llms = {'chatgpt', 'gemini', 'claude', 'llama', 'chatgpt'}
>>> llms
{'chatgpt', 'claude', 'llama', 'gemini'}
```
- We can perform mathematical operations too.

```
>>> llms
>>> llms_chatgpt = {'chatgpt'}
>>> llms - llms_chatgpt
{'claude', 'llama', 'gemini'}

>>> llms & llms_chatgpt
{'chatgpt'}
>>> llms ^ llms_chatgpt
{'claude', 'llama', 'gemini'}
>>> llms | llms_chatgpt
{'claude', 'gemini', 'chatgpt', 'llama'}
```

# Dictionaries
- Dictionaries are indexed by 'keys'.
- Keys are 'immutable' types. 'strings' and 'numbers' can be keys. 'Tuples' can also be used as keys if they contain only 'strings', 'numbers' or 'tuples'
- To get value of 'key' we can either use 'd[key]' or 'd.get('key'). Former throws 'KeyError' if key doesn't exist. Later returns 'None' if 'key' doesn't exist. So 'get' is better option.
- list(d) returns list of keys in 'insertion' order. If we need 'sorted' we need to use 'sorted(d)'.
- If we need to check 'key' exists, we use `'key' in dict`.

```
>> llms = {
... "OpenAI" : "ChatGpt",
... "Anthropic" : "Claude",
... "Google" : "Gemini",
... "Meta" : "Llama"
... }
>>> llms['anthropic']
Traceback (most recent call last):
  File "<python-input-54>", line 1, in <module>
    llms['anthropic']
    ~~~~^^^^^^^^^^^^^
KeyError: 'anthropic'
>>> llms['Anthropic']
'Claude'
>>> llms.get('anthropic')
>>> 'OpenAI' in llms
True
```

- Dictionary can also be built using 'dict()' constructor.
```
>>> llms = dict([('OpenAI','ChatGpt'),('Anthropic','Claude')])
>>> llms
{'OpenAI': 'ChatGpt', 'Anthropic': 'Claude'}
```

- List comprehensions
```
>>> {x : x**2 for x in {1,2,3,4}}
{1: 1, 2: 4, 3: 9, 4: 16}
```

- Looping 

```
>>> for company, model in llms.items():
...     print(f"{company} : {model}")
...     
OpenAI : ChatGpt
Anthropic : Claude
```

# Looping Techniques
- Dictionaries
```
>>> for company, model in llms.items():
...     print(f"{company} : {model}")
...     
OpenAI : ChatGpt
Anthropic : Claude
```
- Enumerate
```
>>> for index, value in enumerate([1,2,3]):
...     print(f"{index} : {value}")
...     
0 : 1
1 : 2
2 : 3
```
- Zip allows to loop over 2 sequences at the same time.
```
>>> companies = ['OpenAI','Anthropic','Google','Meta']
>>> llms = ['ChatGPT','Claude','Gemini','Llama']
>>> for company, model in zip(companies, llms):
...     print(f"{company} : {model}")
...     
OpenAI : ChatGPT
Anthropic : Claude
Google : Gemini
Meta : Llama
```

- To loop in 'reverse'.

```
>>> llms
['ChatGPT', 'Claude', 'Gemini', 'Llama']
>>> for i in reversed(llms):
...     print(i)
...     
Llama
Gemini
Claude
ChatGPT
```

- To loop over 'sorted'.
```
>>> for i in sorted(llms):
...     print(i)
...     
ChatGPT
Claude
Gemini
Llama
```