# Chapter 4: More Control Flow Tools

This chapter covers control flow statements and tools in Python.

## if statements

```
x  = int(input("Enter a number : "))
>>> if x < 0 :
...  print("Number is negative")
... elif x == 0:
...  print("Number is zero")
... else: 
...  print("Number is positive")
...  
Number is positive
```

## for statements
- 'for' statement can iterate over 'items' of any sequence 'list' or 'string' etc.

```
>>> for i in ['a','b','c']:
...  print(i)
...  
a
b
c
>>> for i in 'iloveai':
...  print(i)
...  
i
l
o
v
e
a
i
```

## The `range()` Function

```
# returns type of 'range'
>>> for i in range(9):
...  print(i)
...  
0
1
2
3
4
5
6
7
8
```
```
# Create list and iterate
>>> x = list(range(9))
>>> type(x)
<class 'list'>
>>> for i in x:
...  print(i)
...
0
1
2
3
4
5
6
7
8
```

### Enumerate function returns 'enumerate' object. 'iterator' returned by 'enumerate()' returns 'tuple' which contains 'index', 'item'. For example 'tuple's for below 'algorithms' list are "(0, 'xgboost')", "(1, 'transformers')"
```
>>> algorithms = ['xgboost', 'transformers']
>>> for i, algorithm in enumerate(algorithms):
...  print(f"{i} {algorithm}")
...  
0 xgboost
1 transformers
```

## 'break' and 'continue' statements

### Break
- breaks out of the 'innermost'(Check out second example, it comes out of only inner loop for 'j') enclosing 'for' or 'while' loop
```
>>> for i in range(9):
...  print(i)
...  break
...  
0
```
```
>>> for i in range(5):
...   print(f"i : {i}")
...   for j in range(5):
...     print(f"j : {j}")
...     break
...     
i : 0
j : 0
i : 1
j : 0
i : 2
j : 0
i : 3
j : 0
i : 4
j : 0
```

### Continue
- continues the loop.

```
# Note 'else' statement is not required and without 'else' the program will continue. But added else just to show use of 'continue'.
>>> while True:
...   x = int(input("Enter number: loop continues until you enter 9 : "))
...   if x == 9:
...     break
...   else:
...     continue
...     
Enter number: loop continues until you enter 9 : 1
Enter number: loop continues until you enter 9 : 2
Enter number: loop continues until you enter 9 : 3
Enter number: loop continues until you enter 9 : 4
Enter number: loop continues until you enter 9 : 5
Enter number: loop continues until you enter 9 : 9
```

## 'else' clause on loops
- In 'for' loop, the 'else' cause is executeed after the loop finishes its 'final' iteration, that is, if no break.
```
>>> for i in range(3):
...   print(i)
... else:
...   print("Else block")
...   
0
1
2
Else block
```
- In 'while' loop, its executed after the loop's condition becomes false.

```
>>> i = 0
>>> while i < 2:
...   print(i)
...   i += 1
... else:
...   print("End While Block")
...   
0
1
End While Block
```

## 'pass' statements
- 'pass' statement does nothing. It can be used when a statement is required syntactically but the program requires no action.
```sh
>>> for i in range(2):
...   pass
... 
```

## 'match' statement
- 'match' statement takes 'expression' and compares its value to one or more patterns.

```
>>> def print_llm_model(model_name):
...   match model_name:
...     case "chatgpt":
...       print("I am chatgpt")
...       return
...     case "claude":
...       print("I am claude")
...       return
...     case "gemini":
...       print("I am gemini")
...       return
...     case _:
...       print(f"I built my own model : {model_name}")
...       
>>> print_llm_model("chatgpt")
I am chatgpt
>>> print_llm_model("claude")
I am claude
>>> print_llm_model("gemini")
I am gemini
>>> print_llm_model("vijay_llm")
I built my own model : vijay_llm
```

## Defining functions

- keyword 'def' is start of function 'definition'.
- function can have list of 'formal' parameters.
- 'execution' of a function introduces a new 'symbol' table used for local symbol table. Python finds variables in following order
- 'actual' parameters are parameters which are used when 'function' is called.
- all functions by default 'return' 'None' if 'return' is not defined.
- arguments are passed by 'call by value'(We are passing 'reference' to the object, not copies of the object)

```
>>> llm_list = ["chatgpt", "claude", "gemini"]
>>> def add_new_llm(llm_list):
...   print(id(llm_list))
...   llm_list.append("deepseek")
...   print(llm_list)
...   
>>> id(llm_list)
4353649920
>>> llm_list
['chatgpt', 'claude', 'gemini']
>>> add_new_llm(llm_list)
4353649920
['chatgpt', 'claude', 'gemini', 'deepseek']
>>> llm_list
['chatgpt', 'claude', 'gemini', 'deepseek']
```

**TODO** :- Write an detail analysis on below

    - local symbol table
    - then local symbol table in enclosing block
    - then 'global' symbol table
    - then 'built-in' names

```
>>> def tokenizer():
...   print("I am tokenizer function. I break 'prompt' into 'tokens'")
...   
>>> tokenizer()
I am tokenizer function. I break 'prompt' into 'tokens'
```
### Default Arguement values
- We can define parameters with 'default' values, so that if user doesn't provide value, 'default' value is used.
- Default values are evaluated at the point of function 'definition'.
- Default value is evaluated only once.

```
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
```

```
>>> def call_model(prompt="Hello World"):
...   print(f"Calling model with prompt : {prompt}")
...    
>>> call_model("I am learning AI")
Calling model with prompt : I am learning AI
>>> call_model()
Calling model with prompt : Hello World
```

### Keyword arguments
- we pass 'keyword' as an argugment. For example 'temperature' variable below.

```
>>> def tune_inference_parameters(temparature = 1, top_k = 2, top_p = 0.7):
...   print(f"Fine tuning inference parameters with values : {temparature}, {top_k}, {top_p}")
...   
>>> tune_inference_parameters()
Fine tuning inference parameters with values : 1, 2, 0.7
>>> tune_inference_parameters(0,0,0)
Fine tuning inference parameters with values : 0, 0, 0
>>> tune_inference_parameters(top_k=5,top_p=0.5)
Fine tuning inference parameters with values : 1, 5, 0.5
>>> tune_inference_parameters(temparature=0.5)
Fine tuning inference parameters with values : 0.5, 2, 0.7
```

- '\*\<variable>' in formal parameters is a 'tuple' of 'positional' arguments beyond formal parameter list. Should appear first after 'positional' parameters.
- '\*\*\<variable>' in formal parameters is a 'dictionary' of all 'keyword' parameters and values. Should appear last or after '*\<variable>'

```
>>> def train_model(model_name, *hypertune_parameters, **inference_parameters):
...   print(f"model_name: {model_name}")
...   print(f"hypertune_parameters : {hypertune_parameters}")
...   print(f"inference_parameters : {inference_parameters}")
...   
>>> train_model("chatgpt",1,2,3, temperature=1, top_k=2, top_p=0.5)
model_name: chatgpt
hypertune_parameters : (1, 2, 3)
inference_parameters : {'temperature': 1, 'top_k': 2, 'top_p': 0.5}
```

### Unpacking argument list
- we can use '*' to unpack the arguments out of a 'list' or 'tuple'.
```
>>> def list_models(model_1, model_2):
...   print(f"LLM Models : {model_1} {model_2}")
...   
>>> llms_list = ["chatgpt", "claude"]
>>> list_models(*llms_list)
LLM Models : chatgpt claude
```

### Lambda expressions
- We can create small anonymous functions using 'lambda'.
- Lambda functions are used wherever a function objects are required.

```
>>> def create_model(number_of_parameters):
...   return lambda model_name: f"Created LLM model : {model_name} with : {number_of_parameters}"
...   
>>> model_creator = create_model(10000000)
>>> model_creator("chatgpt")
'Created LLM model chatgpt with : 10000000'
>>> model_creator("claude")
'Created LLM model claude with : 10000000'
>>> model_creator("gemini")
'Created LLM model gemini with : 10000000'
```

### Document String
- Document strings start and end with """.

```
>>> def document_strings_examples():
...   """
...      This is document string example. Document strings starts and ends with 'triple' 'doublequotes'
...   """
...   pass

>>> document_strings_examples.__doc__
"\nThis is document string example. Document strings starts and ends with 'triple' 'doublequotes'\n"
```

### Function annotationss

```
>>> def list_models(filter_by_company : str) -> list:
...   print(f"List of models create by company : {filter_by_company}")
...   print(f"Annotations : {list_models.__annotations__}")
...   return ["Opus", "Sonnet"]
...   
>>> list_models("Anthropic")
List of models create by company : Anthropic
Annotations : {'filter_by_company': <class 'str'>, 'return': <class 'list'>}
['Opus', 'Sonnet']
```

## Python Code Style
- PEP 8 is the style Guide for Python Code: https://peps.python.org/pep-0008/


# Iterators, Iterable
# global, nonlocal