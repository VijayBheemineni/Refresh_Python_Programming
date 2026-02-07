# Chapter 11: Brief Tour of the Standard Library - Part II

This chapter continues exploring Python's standard library with more advanced modules including logging, threading, multiprocessing, and other specialized tools.

# Output Formatting
- `pprint` prints out output in better format.
```
>>> from pprint import pprint
>>> pprint({'company_name': 'Anthropic', 'model_name': 'Claude'})
{'company_name': 'Anthropic', 'model_name': 'Claude'}
```
# MultiThreading
- Threading allows to do multiple things at once instead of one thing at a time. Threading in Python is great for tasks that involve a lot of waiting around.
- `threading` module provides the necessary tools

```
import threading
import time

def train_model(model_name):
    time.sleep(2)
    print(f"Training Model : {model_name}")

chatgpt_thread = threading.Thread(target=train_model, args=("ChatGPT",))
claude_thread = threading.Thread(target=train_model, args=("Claude",))
gemini_thread = threading.Thread(target=train_model, args=("Gemini",))

# Start the threads
chatgpt_thread.start()
claude_thread.start()
gemini_thread.start()

# Wait for every one to finish
chatgpt_thread.join()
claude_thread.join()
gemini_thread.join()

print("All models training completed")
```

# Logging
- `logging` module is used for 'logging'
```
>>> import logging
>>> LOGGER = logging.getLogger(__name__)
>>> logging.basicConfig(level=logging.INFO)
```

# Tools for working with Lists
- `array` are similar to lists but only stores one 'type' of items(homogeneous) so they are memory efficient.
```
>>> import array
>>> array.array('i',[1,2,3,4,5])
array('i', [1, 2, 3, 4, 5])
```
- `collections` module provides important objects like `deque`(Double ended queue) that acts like `list` with faster appends and `pops` from left too but slower lookups in the middle.

```
>>> from collections import deque
>>> d = deque(["chatgpt","claude","gemini","llama"])
>>> d.append("vijayllm")
>>> d
deque(['chatgpt', 'claude', 'gemini', 'llama', 'vijayllm'])
>>> print(d.popleft())
chatgpt
>>> d
deque(['claude', 'gemini', 'llama', 'vijayllm'])
```
- `heapq` module provides functions for implementing 'heaps' based on reqular lists. It keeps list organized so that we can always pickup the 'smallest' or 'largest' items. Generaly used for scheduling, prioritizing tasks or finding top 'K' items.

```
>>> import heapq
>>> tasks = []
>>> heapq.heappush(tasks,(3, 'ChatGPT'))
>>> heapq.heappush(tasks,(1, 'Claude'))
>>> heapq.heappush(tasks,(2, 'Gemini'))
>>> heapq.heappush(tasks,(4, 'Llama'))
>>> heapq
>>> print(heapq.heappop(tasks))
(1, 'Claude')
>>> print(heapq.heappop(tasks))
(2, 'Gemini')
>>> print(heapq.heappop(tasks))
(3, 'ChatGPT')
>>> print(heapq.heappop(tasks))
(4, 'Llama')
```