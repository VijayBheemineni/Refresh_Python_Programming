# Chapter 9: Classes

This chapter covers object-oriented programming in Python, including class definitions, inheritance, and special methods.

# Classes
- provides a way to bundle data and functionality together.
- Each class can have attributes attached to it for maintaining its state. Class instances can also have methods for modifying its state.
- `attribute` is any name following dot. For example `llms.get_models()` `get_model` is an attribute of object `llms`. In another example `myllms.get_llms` `get_llms` 'myllms' is an object and 'get_llms' is an attribute.
    - attribute may be 'read-only' and 'writable'.

# Python Scope and Namespaces
- A `namespace` is a mapping from names to objects.
- Examples of `namespaces` are 'built-in' names, global names, local names.
- Different namespaces are created at different time.
    - 'built-in' names created when the python interpreter starts up and is never deleted.
    - 'global' namespace is created when the module definition is read in.
    - 'local' namespace is created when function is called and delted when function returns or raises an exception that is not handled by function.
- Search for variable in 'namespaces' happens as following
    - the innermost scope, which is served first, contains the local names.
    
        ```
        >>> llm_model_name = 'chatgpt'
        >>> def get_model_name():
        ...     # 'llm_model_name' is defined in the function. Now Python will used this name instead of 'global' variable.
        ...     llm_model_name = 'claude'
        ...     print(f"LLM Model Name : {llm_model_name}")
        ...     
        >>> get_model_name()
        LLM Model Name : claude
        ```
    
    - scopes of any enclosing functions.
    - next 'global' names.
    
        ```
        >>> # Global name
        >>> llm_model_name = 'chatgpt'
        >>> globals()
        {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, 'os': <module 'os' (frozen)>, 'builtins': <module 'builtins' (built-in)>, 'llm_model_name': 'chatgpt'}
        >>> def get_model_name():
        ...     # 'llm_model_name' variable doesn't exist within function 'local' namespace, so goes and check 'global' namespace.
        ...     print(f"LLM Model Name : {llm_model_name}")
        ...     
        >>> globals()
        {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, 'os': <module 'os' (frozen)>, 'builtins': <module 'builtins' (built-in)>, 'llm_model_name': 'chatgpt', 'get_model_name': <function get_model_name at 0x105b8da60>}
        >>> get_model_name()
        LLM Model Name : chatgpt
        ```
    
    - finally 'built-in' names
    
        ```
        >>> import builtins
        >>> dir(builtins)
        ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'PythonFinalizationError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '_IncompleteInputError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
        ```
- if we need define variable as `global` we need to use key word `global`.
- We can use `globals()` to find all variables in 'global' namespace. We can use `locals()` to find all variables in 'local' space.

## LEGB Rule: Name Resolution Order
    - L(Local)
    - E(Enclosing)
    - G(Global)
    - B(Built In)

    Note :- if variable in not found in any of the scopes, 'NameError' is thrown.

# Global Keyword

```
>>> def increment():
...     global counter # We are telling 'Python' to use 'Global' variable
...     counter += 1
...     print(f"Counter : {counter}")
...  
>>> increment()
Counter : 1
>>> increment()
Counter : 2
>>> increment()
Counter : 3
>>> 
```
```
# Without Global Keyword
>>> counter=0
>>> def increment():
...     counter = 0
...     counter += 1
...     print(f"Counter : {counter}")
...     
>>> increment()
Counter : 1
>>> increment()
Counter : 1
```

# Non Local
- `nonlocal` indicates the particular variable live in an enclosing scope and should be rebound here

```
...     def do_nonlocal():
...         nonlocal model_status
...         model_status = "nonlocal training"
...     
...     def do_global():
...         global model_status
...         model_status = "global training"
...     
...     model_status = "test model"
...     do_local()
...     print("After local assignment:", model_status)
...     do_nonlocal()
...     print("After nonlocal assignment:", model_status)
...     do_global()
...     print("After global assignment:", model_status)
... 
... train_model()
... print("In global scope:", model_status)
... 
After local assignment: test model
After nonlocal assignment: nonlocal training
After global assignment: nonlocal training
In global scope: global training
```

# First Look At Classes
## Class Defintion
- When a class definition is entered, a new namespace is created and used as a local scope, thus all assignments to local variables go into new namespace.
- When a class definition is left normally, a class object is created. 

```
class CustomModel:
    pass
```
## Class Objects
- Class object support 2 kinds of operations: attribute references(obj.name) and instantiation.
- Class instantiation `model = CustomModel()`

```
>>> class CustomModel:
...     """Vijay's custom llm model"""
...     model_name = "vijay_llm"
...     def get_model_name(self):
...         return self.model_name
...         
>>> dir(CustomModel)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'get_model_name', 'model_name']
>>> CustomModel.model_name
'vijay_llm'
>>> CustomModel.get_model_name
<function CustomModel.get_model_name at 0x105e65d20>
>>> model = CustomModel()
>>> model.get_model_name()
'vijay_llm'
>>> CustomModel.__doc__
"Vijay's custom llm model"
```
- Using `__init__()` method we can create instances with specific initial state.

```
>>> class CustomModel:
...     """ Vijay's custom model"""
...     def __init__(self, model_name):
...         self.model_name = model_name
...     def get_model_name(self):
...         return self.model_name
...         
>>> fm_model = CustomModel("vijay_fm_model")
>>> fm_model.get_model_name()
'vijay_fm_model'
>>> health_model = CustomModel("vijay_health_model")
>>> health_model.get_model_name()
'vijay_health_model'
```

## Instance Objects
- The only operation understood by instance objects are attribute references. There are two kinds of valid attribute names: `data attributes` and `methods`.

```
>>> fm_model = CustomModel("vijay_fm_model")
>>> fm_model.model_name
'vijay_fm_model'
>>> fm_model.get_model_name()
'vijay_fm_model'
```

## Method Objects
```
>>> fm_model.get_model_name()
'vijay_fm_model'
```

## What is Self?
- In class method below we have seen parameter called 'self'. What is 'self'? 'self' is the actual Python object created. In the below code we can see we call the `method` of object like `model.get_model_name` but in the backend actual way it is called is `CustomModel.get_model_name(model)`. In this case we can see we are passing 'object' model to the method which is assigned to the variable 'self'.
- The name of the parameter 'self' can be anything but it is Python convention. So we name this variable as `self` always.

```
>>> model = CustomModel("my_model")
>>> model.get_model_name()
'my_model'
>>> CustomModel.get_model_name(model)
'my_model'
```

## Class and Instance variables
- instance variables are unique to each instance.
- class variables are shared by all instances of the class.
```
>>> class CustomModel:
...     # Class variable. Its same for all instances of this class.
...     version = "1.0"
...     def __init__(self, model_name):
...         # 'model_name' is instance variable. It can different for each instance.
...         self.model_name = model_name
...     def get_model_name(self):
...         return self.model_name
...         
>>> model1 = CustomModel("model1")
>>> model1.version
'1.0'
>>> model1.model_name
'model1'
>>> model1.get_model_name()
'model1'
>>> model2 = CustomModel("model2")
>>> model2.version
'1.0'
>>> model2.model_name
'model2'
>>> model2.get_model_name()
'model2'
```

## Random remarks
- If the same attribute name occurs in both an instance and in a class, then attribute lookup priritizes the `instance`.
```
>>> class CustomModel:
...     version = "1.0"
...     def __init__(self, version):
...         self.version = version
...         
>>> model = CustomModel("9.0")
>>> model.version
'9.0'
```

# Inheritance
- We can inherit our class from another class. In below example `LLMModel` is inheriting from `FMModel` baseclass.
```
    class LLMModel(FMModel):
        pass
```
- `isinstance(obj, <ClassType>)`: checks if object is of specific type, if yes returns True, else False
```
>>> model = CustomModel(9)
>>> class CustomModel:
...     version = "1.0"
...     def __init__(self, version):
...         self.version = version
...         
>>> model = CustomModel(9)
>>> isinstance(model, CustomModel)
True
>>> isinstance(model, int)
False
```
- `issubclass` checks if object is subclass of a class.

```
>>> class FMModel:
...     pass
...     
>>> class LLMModel(FMModel):
...     pass
...     
>>> llmmodel = LLMModel()
>>> issubclass(LLMModel, FMModel)
True
```

## Multiple Inheritence

```
    class CustomModel(FMModel, LLMModel):
        pass
```

# Private Variables
- This is just convention. There is no `private` variables concept in python. 
- Private variables start with '_'. These variables are treated as Non-Public part of the API.

```
>>> class CustomModel:
...     # This is a private variable by naming convention. Shouldn't be accessed directly and its used for internal purpose.
...     # But this is just convention, if we want to access we can access this variable.
...     _custom_hyper_parameters = {}
...     pass
...     
...     
>>> CustomModel._custom_hyper_parameters
{}
```

# DataClasses
- These are similar to `C` `Struct`. We can create custom data types.

```
>>> from dataclasses import dataclass
>>> @dataclass
... class CustomModel:
...     model_name: str
...     model_version: float
...     model_description: str
...     
>>> fm_model = CustomModel("vijay_model",0.0, "This is my first llm model")
>>> fm_model.model_name
'vijay_model'
>>> fm_model.model_version
0.0
>>> fm_model.model_description
'This is my first llm model'
```

# Iterators

- In `for` loop we can iterate over few objects, for example `str`, `list`. This is possible because `for` function calls `iter()` method on the object.  

```
>>> llms = ['chatgpt', 'claude']
>>> for model in llms:
...     print(model)
...     
chatgpt
claude
```
 - The function `iter()` return `iterator` object that defines `__next__()` method which access elements in object one at a time. When there are no elements `__next__()` raises `StopIteration` which will terminate `for` loop.

```
>>> llms
['chatgpt', 'claude']
>>> llms_iterator = iter(llms)
>>> llms_iterator
<list_iterator object at 0x104bb8250>
>>> next(llms_iterator)
'chatgpt'
>>> next(llms_iterator)
'claude'
>>> next(llms_iterator)
Traceback (most recent call last):
  File "<python-input-93>", line 1, in <module>
    next(llms_iterator)
    ~~~~^^^^^^^^^^^^^^^
StopIteration
>>>
```
- Example of our own 'Custom' class defining 'iterator' methods.

```
# Example
>>> class ListMyLLMs:
...     def __init__(self):
...         self.llm_models = ['chatgpt','claude','gemini','llama']
...         self.index = 0
...     
...     def __iter__(self):
...         return self
... 
...     def __next__(self):
...         if self.index < len(self.llm_models):
...             model = self.llm_models[self.index]
...             self.index += 1
...             return model 
...         else:
...             raise StopIteration
...             
>>> for model in ListMyLLMs():
...     print(model)
...     
chatgpt
claude
gemini
llama
```

# Generators
- `Generators` are a simple and powerful tool to create `iterators`(Object which implement '__iter__' method).
- They are regular function but use `yield` statement. Each time `next()` is called on it, the `generator` resumes where it left off.
- This is simpler than creating `iterator` object.

```
>>> class MyLLMModels:
...     def __init__(self):
...         self.llm_models = ['claude', 'chatgpt', 'gemini', 'llama']
...     def __iter__(self):
...         for model in self.llm_models:
...             yield model
...             
>>> for model in MyLLMModels():
...     print(model)
...     
claude
chatgpt
gemini
llama
```

# Generator Expressions
- Generator Expressions are similar to list comprehensions but with parentheses instead of square brackets.
- Generator expression is are memory friendly. List expressions stores all items in memory, where are `generator` expression only stores one item at a time in memory.

```
>>> numbers_list = [x for x in range(10000000)]
# Generator
>>> numbers_gen = (x for x in range(10000000))
>>> print(f"List memory:      {sys.getsizeof(numbers_list):,} bytes")
List memory:      89,095,160 bytes
>>> print(f"Generator memory: {sys.getsizeof(numbers_gen):,} bytes")
Generator memory: 200 bytes
```

