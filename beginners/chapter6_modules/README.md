# Chapter 6: Modules

This chapter covers how to organize Python code into modules and packages.

## Modules
- 'module' is a python file which consists of Python 'definitions' and 'statements'.
- 'definitions' from a module can be 'imported' into other modules.
- Module name is available as the value of the global variable '__name__'. For example in our case the file is 'import_modules.py'. So '__name__' has value as 'import_modules'

```
>>> import import_modules
>>> import_modules.__name__
'import_modules'
```
- Once we create file(module) we can import the module and use the definitions in the module. In our case 'import_modules' file has defintion/function 'list_llms'. We can call 'list_llms' function.

```
>>> import import_modules
>>> dir(import_modules)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'list_llms']
>>> import_modules.list_llms()
Model Name : chatgpt
Model Name : claude
Model Name : gemini
Model Name : llama
>>> import_modules.__name__
'import_modules'
```
- Module 'statements', 'function definitions' are executed only one time during first time import.

- Each module has its own 'private' namespace.
- Module can import another modules using 'import' statement.
- We can also below method to import 'module' defintions. When execute as below 'import_modules' name doesn't exist in python program namespace where below 'from' statement executed.

```
>>> from import_modules import list_llms
>>> list_llms()
Model Name : chatgpt
Model Name : claude
Model Name : gemini
Model Name : llama
```
- We can also import all 'names' using below method. This imports all names except those which start with '_'

```
>>> from import_modules import *
>>> list_llms()
Model Name : chatgpt
Model Name : claude
Model Name : gemini
Model Name : llama
```

- Using 'as' we can give different name to imported module or name.

```
>>> import import_modules as vijay_modules
>>> vijay_modules.list_llms()
Model Name : chatgpt
Model Name : claude
Model Name : gemini
Model Name : llama
```

**NOTE** :- For efficiency reasons, each module is 'imported' only once. If we change our module we can reload the module using `import importlib;importlib.reload(modulename)` or `importlib.reload()`

### Executing Python Modules as scripts

- When we call 'module' as script. '__name__' variable value is set to "__main__".

```
 python import_modules.py 
Model Name : chatgpt
Model Name : claude
Model Name : gemini
Model Name : llama
```

- Below code means the code will be executed only when 'module' is run as script as above. In Python interpretor or if we import the module in another python module below code will not be called.

```
if __name__ == "__main__":
    list_llms()
```

### Module Search Path
- When a module is imported, Python first searches for 'built-in' modules with that name. 

```
>>> import sys
>>> sys.builtin_module_names
('_abc', '_ast', '_codecs', '_collections', '_contextvars', '_datetime', '_functools', '_imp', '_io', '_locale', '_opcode', '_operator', '_signal', '_sre', '_stat', '_string', '_suggestions', '_symtable', '_sysconfig', '_thread', '_tokenize', '_tracemalloc', '_types', '_typing', '_warnings', '_weakref', 'atexit', 'builtins', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'posix', 'pwd', 'sys', 'time')
```
- Then it searches for a file in a list of directories given by variable `sys.path`. `sys.path` is initialized from these locations
    - The directory containing the input script or current directory.
    - `PYTHONPATH` system variable
    - The installation-dependent default (by convention including a site-packages directory, handled by the site module).


## Standard Modules
- Python comes with a library of standard modules.
- Some modules are built into the interpreter. For example `sys`.

```
>>> import sys
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_baserepl', '_clear_internal_caches', '_clear_type_cache', '_clear_type_descriptors', '_current_exceptions', '_current_frames', '_debugmallocstats', '_dump_tracelets', '_framework', '_get_cpu_count_config', '_getframe', '_getframemodulename', '_git', '_home', '_is_gil_enabled', '_is_immortal', '_is_interned', '_jit', '_setprofileallthreads', '_settraceallthreads', '_stdlib_dir', '_xoptions', 'abiflags', 'activate_stack_trampoline', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'deactivate_stack_trampoline', 'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exception', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getunicodeinternedsize', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'is_remote_debug_enabled', 'is_stack_trampoline_active', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'monitoring', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'ps1', 'ps2', 'pycache_prefix', 'remote_exec', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions']
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.path
```

## The dir() function
- built-in function `dir()` is used to find out which names a module defines.

```
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_baserepl', '_clear_internal_caches', '_clear_type_cache', '_clear_type_descriptors', '_current_exceptions', '_current_frames', '_debugmallocstats', '_dump_tracelets', '_framework', '_get_cpu_count_config', '_getframe', '_getframemodulename', '_git', '_home', '_is_gil_enabled', '_is_immortal', '_is_interned', '_jit', '_setprofileallthreads', '_settraceallthreads', '_stdlib_dir', '_xoptions', 'abiflags', 'activate_stack_trampoline', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'deactivate_stack_trampoline', 'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exception', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getunicodeinternedsize', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'is_remote_debug_enabled', 'is_stack_trampoline_active', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'monitoring', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'ps1', 'ps2', 'pycache_prefix', 'remote_exec', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions']
```
- `dir()` doesn't list builtin functions and variables.

```
>>> import builtins
>>> dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'PythonFinalizationError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '_IncompleteInputError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```

## Packages
- Packages are a way of structing Python's module namespace by using "dotted module names"