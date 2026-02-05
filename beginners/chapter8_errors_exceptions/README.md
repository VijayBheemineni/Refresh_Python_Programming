# Chapter 8: Errors and Exceptions

This chapter covers handling errors and exceptions in Python, including try-except blocks, raising exceptions, and creating custom exceptions.

# Exceptions
- Errors detected during 'execution' are called as 'exceptions'
- We handle the exception if we think we can recover from issue, else we log the exception and 'raise' it again to display the issue.

# Handling Exceptions
- In below code we are asking user to enter 'number'. If user enters 'strings' an error is thrown. We can decide how to handle the error either ignore it and handle it and exit the program cleanly.
- When we think a code might throw error then we wrap that block of code in `try`, `except` block.
```
>>> x = int(input("Please enter a number: "))
Please enter a number: abc
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    x = int(input("Please enter a number: "))
ValueError: invalid literal for int() with base 10: 'abc'

# Exception Handling
>>> try:
...     x = int(input("Enter a number : "))
... except ValueError:
...     print(f"ERROR: User entered value which is not number")
... 
Enter a number : abc
ERROR: User entered value which is not number
```
- Catching multiple exceptions.

```
    except (RuntimeError, ValueError):
        pass
```
- `except` clause may specify a variable after the exception name.

```
>>> try:
...     raise Exception("Raised exception")
... except Exception as e:
...     print(type(e))
...     print(e.args)
...     print(e)
...     
<class 'Exception'>
('Raised exception',)
Raised exception
```

- `BaseException` is the common base class of all exceptions. One of its subclasses is `Exception`, which is base class for all 'non-fatal' exceptions. Exceptions which are not part of `Exception` are not typically handled because the indicate that the program should terminate. For example `SystemExit`. `Exception` can be used as 'wildcard' to catch any exception.

```
>>> try:
...     print("Using Exception as Wildcard Exception Handler")
... except MemoryError as e:
...     print("Memory errors are handled here")
... except ModuleNotFoundError as e:
...     print("Module not found error are handled here")
... except Exception as e:
...     print("All other exceptions are handled here")
... 
```

- `try`, `except` statement has an optional `else` clause. This is executed when no exceptions are thrown.

```
>>> try:
...     print("No exceptions are being raised here")
... except Exception as e:
...     print("If any exception is raised, we will handle here")
... else:
...     print("No exceptions have been raised in this program")
...     
No exceptions are being raised here
No exceptions have been raised in this program
```

# Raise Exceptions
- `raise` statement allows us to raise an exception.
```
>>> raise RuntimeError("Runtime Error as occured.")
Traceback (most recent call last):
  File "<python-input-8>", line 1, in <module>
    raise RuntimeError("Runtime Error as occured.")
RuntimeError: Runtime Error as occured.
```

# Exceptions Chaining
- Exceptions can be chained. Below first 'MemoryError' happened and then 'RuntimeError'. To indicate that an exception is a direct consequence of another, the `raise` statement allows an optional `from` clause. `raise RuntimeError from exc`

```
>>> try:
...     raise MemoryError("Memory Error occurred")
... except MemoryError as e:
...     raise RuntimeError("System doesn't have memory, so throwing runtime error") from e
...     
Traceback (most recent call last):
  File "<python-input-12>", line 2, in <module>
    raise MemoryError("Memory Error occurred")
MemoryError: Memory Error occurred

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<python-input-12>", line 4, in <module>
    raise RuntimeError("System doesn't have memory, so throwing runtime error") from e
RuntimeError: System doesn't have memory, so throwing runtime error
```

# User Defined Exceptions
- We can define our own exceptions by creation a new exception class.

```
>>> class A(Exception):
...     pass
...     
>>> try:
...     raise A("Throwing our own exception")
... except Exception as e :
...     print("Catching our own exception")
...     print(e)
...     
Catching our own exception
Throwing our own exception
```

# Defining Clean Up Actions
- `try` statement has another optional clause `finally` which gets exceuted as the last task before `try` statements completes. This block is called whether exception is raised or not.

```
>>> try:
...     raise MemoryError("Memory Error Raised")
... except Exception as e:
...     print("Memory Error handled")
...     print(e)
... finally:
...     print("Finally block executed")
...     
Memory Error handled
Memory Error Raised
Finally block executed
>>> 

# No Exception
>>> try:
...     print("No Error")
... except Exception as e:
...     print("Memory Error handled")
...     print(e)
... finally:
...     print("Finally block executed")
...     
No Error
Finally block executed
```

# Predinfed Clean Up Actions
- If we write below code, the `file` object is not closed immediately after executing the for loop. The object stays in memory for some amount of time which is bad.
```
>>> for line in open("aimodel.py"):
...     print(line)
...     
```
- If we open the file with `with` clause, the file is closed automatically after the block.

```
>>> with open("aimodel.py") as f:
...  for line in f:
...   print(line)
...   
```

# Enriching Exceptions with Notes
```
>>> try:
...     raise MemoryError("No memory available")
... except Exception as e:
...     e.add_note("Loaded a big csv file due to memory might be utilized")
...     raise 
...     
Traceback (most recent call last):
  File "<python-input-26>", line 2, in <module>
    raise MemoryError("No memory available")
MemoryError: No memory available
Loaded a big csv file due to memory might be utilized
```