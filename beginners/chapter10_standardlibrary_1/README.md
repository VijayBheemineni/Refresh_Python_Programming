# Chapter 10: Brief Tour of the Standard Library

This chapter introduces commonly used modules from Python's standard library, including os, sys, glob, re, math, and more.

# Operating System Interface
- `os` module provides functions to interact with OS.

```
>>> import os
>>> os.system('clear')
```
- `shutil` provides functions for file and management tasks
```
>>> import shutil
>>> shutil.disk_usage('.')
```

# File Wildcards
- `glob` module provides a function for making file lists from directory wildcard searches.
```
>>> import glob
>>> glob.glob('*py')
[]
```

# Command Line Arguments
- Command line arguments we provide are stored in `sys` modules `argv` attribute as a list.

```
# File model_analysis.py
import sys
print(sys.argv)

# Calling the module
python model_analysis.py chapgpt claude gemini llama

# Output
['model_analysis.py', 'chapgpt','claude','gemini','llama']
```
- `argparse` module provides more sophisticated mechanism to process commnad line arguments.
**TODO* There are more other modules to process command line arguments. For example `click`, `argparse` etc

# Error Output Redirection and Program Termination
- `sys` module has attributes `stdin`, `stdout` and `stderr`.
```
>>> sys.stdout.write('Deploying the model')
Deploying the model19
>>> 
```
- To exit the program `sys.exit()`

# String Pattern Matching
- `re` module provides regular expression tools for advanced string processing.

# Mathematics
- `math` module
- `random` module provides tools for random selections
- `statistics` provides basic statistical properties

# Internet Access
- `urllib.request` to retrieve data from the url.
**TODO* Check `requests` module too.
```
from urllib.request import urlopen
with urlopen("https://huggingface.co/") as response:
     for line in response:
        line_decode = line.decode()
        print(line_decode)
```

# Dates and Times
- `datetime` modules provides classes for manipulating dates and times.
```
>>> from datetime import date
>>> date.today()
datetime.date(2026, 2, 7)
```

# Data Compression
- Common data archiving modules `zlib`, `gzip`, `bz2`, `zipfile`, `tarfile`.
```
>>> gzip modules.py
```
# Performance Management
- `timeit` modules provides the tool to check processing time of the commands.

# Quality Control
- `doctest` module provides a tool for scanning a module and checking `docstrings`.
```
>>> import doctest
>>> def list_models():
...     pass
...     
>>> doctest.testmod()
TestResults(failed=0, attempted=0)
```
- `unittest` module for unit testing.
**TODO** Write separate chapter for `testing`

