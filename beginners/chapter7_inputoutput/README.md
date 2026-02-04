# Chapter 7: Input and Output

This chapter covers reading from and writing to files, formatting output, and working with different file formats.

# Fancier Output Formatting
- 'formatted string literals'. We need to begin string with 'f' or 'F' before the opening quotation mark.
- `str()` prints in human readable form.
- `repr()` prints that can be read by 'interpreter'

## Formatted string literals
```
>>> llm_name = 'claude'
>>> f'LLM name is {llm_name}'
'LLM name is claude'
>>> f'LLM name is : {llm_name}'
'LLM name is : claude'
```
- ':' defines format specification.
    - passing an 'integer' after ':' defines minimum number of characters wide.
```
>>> f'LLM name is : {llm_name}'
'LLM name is : claude'
>>> f'LLM name is : {llm_name:10} :'
'LLM name is : claude     :'
>>> version = 10
>>> f'LLM version is : {version:10d} :'
'LLM version is :         10 :'
```
- "=" can be used to print variable and its value.
```
>>> f'LLM name is : {llm_name=}'
"LLM name is : llm_name='claude'"
```

## String format method

```
>>> print('llm name : {}'.format(llm_name))
llm name : claude

>>> print('llm name : {} and its version : {}'.format(llm_name, version))
llm name : claude and its version : 10

>>> print('llm name : {1} and its version : {0}'.format(version, llm_name))
llm name : claude and its version : 10

>>> print('llm name : {llm_name} and its version : {version}'.format(llm_name="chatgpt", version=0))
llm name : chatgpt and its version : 0

```

# Reading and Writing Files
- `open()` returns a 'file object'. `open(filename, mode, encoding=None)`. We need to call `f.close()` to close the file object.
```
f = open('create_model.py','w')
```
- It is good practice to use the `with` keyword when dealing with file objects. Closes the 'file' object automatically.

```
    with open('create_model.py', 'r') as f:
        read_code = f.read()

    # Check 'file' object closed
    f.closed
```

## File objects methods
- `read(size)` :- 'size' is optional. Reads a line. If end of file reached returns ''. 
- `readline()` :- reads single line from the file. If end of file reached returns ''.
- for readling lines from file we can loop over 'file' object.
```
    for line in f:
        print(line)
```
- Read all the lines of a file in a list, we can use `list(f)` or `f.readlines()`
- `f.write(string)` writes content of string to file, returning number of characters written.

## Saving structured data with json
- `json.dumps` converts Python Object to json string

```
>>> llms = {
... "anthropic": "claude",
... "openai": "chatgpt"
... }
>>> import json
>>> llms
{'anthropic': 'claude', 'openai': 'chatgpt'}
>>> type(llms)
<class 'dict'>
>>> llms_json = json.dumps(llms)
>>> llms_json
'{"anthropic": "claude", "openai": "chatgpt"}'
>>> type(llms_json)
<class 'str'>
```
- `json.loads` :- loads json string and convert to Python object.

```
>>> new_llms = json.loads(llms_json)
>>> type(new_llms)
<class 'dict'>
>>> new_llms
{'anthropic': 'claude', 'openai': 'chatgpt'}
```
- `json.dump(x,f)` :- dumps the JSON string to file. To decode we use `json.load(f)`.