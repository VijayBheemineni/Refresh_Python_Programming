# NumPy

NumPy is the fundamental package for numerical computing in Python, providing support for arrays, matrices, and mathematical functions.

## Topics

- Array creation and manipulation
- Mathematical operations
- Broadcasting
- Linear algebra
- Random number generation

## Advantages
- Mathematical Calculations over entire array.
- Fast for mathematical operations.
- is great for Vector arithmetic.

## Install NumPy
```
pip install numpy
```
## NumPy Basics
- `numpy` can do operations on entire list. For example if we want to 'double' every number in list with regular list its not possible until we write code like `[x * 2 for x in numbers]`. With `numpy` we can directly say `np_numbers * 2`

```
>>> np_numbers = np.array(numbers)
>>> np_numbers * 2
np_numbers * 2
array([ 2,  4,  6,  8, 10])
```
- `numpy` :- contains only one type of elements.

- Filtering elements in 'numpy' array. In below example we want to filter out all elements greater than '2'.

```
>>> type(np_numbers)
<class 'numpy.ndarray'>
>>> np_numbers
array([1, 2, 3, 4, 5])
# Below condition checks if each element is greater than 2 or not. If 'yes' returns 'True' else 'False'
>>> np_numbers > 2
array([False, False,  True,  True,  True])
# We can do actual filter using the condition.
>>> np_numbers[np_numbers > 2]
array([3, 4, 5])
```

### 2D 'numpy' array.

```
>>> odd = [1,3,5,7]
>>> even = [2,4,6,8]
>>> np_2d_odd_even = np.array([odd, even])
>>> np_2d_odd_even
array([[1, 3, 5, 7],
       [2, 4, 6, 8]])
>>> np_2d_odd_even.shape
(2, 4)
# Select rows
>>> np_2d_odd_even[0]
array([1, 3, 5, 7])
>>> np_2d_odd_even[1]
array([2, 4, 6, 8])
# Select row and element in that row
>>> np_2d_odd_even[0][1]
np.int64(3)
>>> np_2d_odd_even[1][1]
np.int64(4)
# Or a better way than above. np[<row>, <column>]
>>> np_2d_odd_even[0,1]
np.int64(3)
>>> np_2d_odd_even[1,1]
np.int64(4)
# Select 0 and 1st element from both rows. np[:, 0:2]. First ':' represents all rows in 'numpy' array. 
>>> np_2d_odd_even[:,0:2]
array([[1, 3],
       [2, 4]])
# Get entire first row
>>> np_2d_odd_even[0,:]
array([1, 3, 5, 7])
```

### Numpy Basic Statistics
```
>>> numbers = [1,2,3,4,5,6,7,8,9,10]
>>> np_numbers = np.array(numbers)
>>> np.mean(np_numbers)
np.float64(5.5)
>>> np.median(np_numbers)
np.float64(5.5)
>>> np.std(np_numbers)
np.float64(2.8722813232690143)
```

### Creating arrays
- `np.zeros` to create arrays which are filled with zeros. We need to pass tuple(rows, columns) as input to the method.
```
>>> import numpy as np
>>> np.zeros((2,4))
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.]])
```
- `np.random.random` can also be used to create `numpy` array. All elements values will be between '0' and '1'.

```
>>> np.random.random((2,4))
array([[0.58838525, 0.26011467, 0.31386384, 0.11637054],
       [0.55265201, 0.67904754, 0.32374006, 0.46661056]])
```
- `np.arrange` creates numbers based on 'start' and 'stop' value. Here we pass numbers directly not as tuples.
```
>>> np.arange(91,100)
array([91, 92, 93, 94, 95, 96, 97, 98, 99])
```

### 3D Arrays

```
>>> two_dim_1 = np.array([
...                             [1,2],
...                             [3,4]
... ])
>>> two_dim_2 = np.array([
...                             [5,6],
...                             [7,8]
... ])
>>> two_dim_3 = np.array([
...                             [9,10],
...                             [11,12]
... ])
>>> three_dim_array = np.array([two_dim_1, two_dim_2, two_dim_3])
>>> three_dim_array
array([[[ 1,  2],
        [ 3,  4]],

       [[ 5,  6],
        [ 7,  8]],

       [[ 9, 10],
        [11, 12]]])
```
- `vector` arrays are 1d arrays. There is no difference between row and column. This concept is used in `embeddings` in AI/ML.

```
>>> vector_array
array([1, 2, 3, 4])
```
- `matrix` arrays are 2d arrays.
```
>>> matrix_array = np.array([
...     [1,2],
...     [3,4]
... ])
>>> matrix_array
array([[1, 2],
       [3, 4]])
```
- `tensor` arrays are 3d or mode dimensions arrays.


## Numpy Attributes
- `shape` :- provides shape of array.
```
>>> matrix_array.shape
(2, 2)
```
- `flatten()` :- flattens the array.

```
>>> matrix_array.flatten()
array([1, 2, 3, 4])
```
- `reshape()` :- reshapes the array.

```
>>> matrix_array.reshape(1,4)
array([[1, 2, 3, 4]])
```
- `dtype` :- returns data type of the array.
```
>>> matrix_array.dtype
dtype('int64')
```
- We can pass `dtype` as argument when creating the array. For example `int32` will occupy less memory.
```
>>> numpy_example = np.array([1,2,3,4], dtype=np.int32)
>>> numpy_example
array([1, 2, 3, 4], dtype=int32)
```
- `astype` :- allows to convert one data type to other.

- Type `coercion`. Numpy will automatically convert `numbers` to strings. And `int` to `float`.

```
>>> numpy_example = np.array([1,2,3,4], dtype=np.int32)
>>> numpy_example
array([1, 2, 3, 4], dtype=int32)
>>> numpy_example.astype(np.float32)
array([1., 2., 3., 4.], dtype=float32)
```
## Numpy Data Types
- `np.int64` :- has 64 bits. Default bit size.
- `np.int32`
- `np.float64`
- `np.float32`

## Numpy  Operations

### Indexing
- Indexing 2D array, the format is `[<row>, <col>]`. If only `[<row>]` all columns are selected in that row. If we want all rows in 1 column `[:,<col>]`

```
>>> indexing_example = np.array([
...     [
...             1,2,3,4,5
...     ],
...     [
...             6,7,8,9,10
...     ]
... ])
>>> indexing_example[0]
array([1, 2, 3, 4, 5])
>>> indexing_example[0,2]
np.int64(3)
>>> indexing_example[:,2]
array([3, 8])
```

### Slicing
- Slicing :- 1D array `[<start>:<stop>]`. 2D Array `[<row_start>:<row_stop>, <col_start>:<col_stop>]`. Also we can provide step value `[<row_start>:<row_stop>:<step_value>, <col_start>:<col_stop>:<step_value>]`

### Sorting

- Sort. By default sort based on 'column'. So each row is taken and column values are sorted in `ascending` order. To sort based on `rows` we need to under `labels`. By default `rows` are `axis=0` and `columns` are `axis=1`.

```
>>> sort_example = np.array([[5,4,3,2,1],[10,9,8,7,6]])
>>> sort_example
array([[ 5,  4,  3,  2,  1],
       [10,  9,  8,  7,  6]])
>>> np.sort(sort_example)
array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10]])

# Sort based on row
>>> np.sort(sort_example,axis=0)
array([[ 5,  4,  3,  2,  1],
       [10,  9,  8,  7,  6]])
```

### Filtering
- Filtering using indexing. Returns array of elements.
```
>>> numbers_array = np.array([1,2,3,4,5,6,7,8,9])
>>> even_numbers_bool = numbers_array % 2 == 0
>>> even_numbers_bool
array([False,  True, False,  True, False,  True, False,  True, False])
>>> even_numbers = numbers_array[even_numbers_bool]
>>> even_numbers
array([2, 4, 6, 8])
```
- Filtering using `np.where`. Returns array of indexes.
       - `np.where` can also be used to replace values.

```
>>> numbers_array = np.array([1,2,3,4,5,6,7,8,9])
>>> np.where(numbers_array % 2 == 0)
(array([1, 3, 5, 7]),)
>>> even_numbers = numbers_array[np.where(numbers_array % 2 == 0)]
>>> even_numbers
array([2, 4, 6, 8])
```

```
# Replace 'even' numbers with 'even', else keep the current value.
>>> np.where(numbers_array %2 == 0, "even", numbers_array)
array(['1', 'even', '3', 'even', '5', 'even', '7', 'even', '9'],
      dtype='<U21')
```

### Adding and Removing Elements

#### Concatenate
- Concatenating. We can concatenate two arrays using `np.concatenate((<array_1>,<array_2>))`
       - For "column" concatenation(axis=1), number of `rows` in both arrays needs to match.
       - For "rows" concatenation(axis=0)(default), number of `columns` in both array needs to match.

```
# In below example we can concatenate row wise(one array below another) because columns match but not rows.
# Numpy automatically selects 'axis=0' because 'axis=1' column concatenation throws error because 1 array has '3' rows but 2 array has only 2 rows. 

>>> array_1
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> array_1.shape
(3, 3)
>>> array_2
array([[10, 11, 12],
       [13, 14, 15]])
>>> array_2.shape
(2, 3)
>>> np.concatenate((array_1,array_2))
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9],
       [10, 11, 12],
       [13, 14, 15]])
>>> np.concatenate((array_1,array_2),axis=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    np.concatenate((array_1,array_2),axis=1)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: all the input array dimensions except for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 3 and the array at index 1 has size 2
```

```
# In below example we can concatenate column wise(one array side by another) because rows match but not columns.
>>> array_1
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> array_1.shape
(3, 3)
>>> array_3 = np.array([[21,22],[23,24],[25,26]])
>>> array_3.shape
(3, 2)
>>> np.concatenate((array_1,array_3),axis=1)
array([[ 1,  2,  3, 21, 22],
       [ 4,  5,  6, 23, 24],
       [ 7,  8,  9, 25, 26]])
>>> np.concatenate((array_1,array_3))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    np.concatenate((array_1,array_3))
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
ValueError: all the input array dimensions except for the concatenation axis must match exactly, but along dimension 1, the array at index 0 has size 3 and the array at index 1 has size 2
```

#### Delete
- np.delete(<array>,<slice_index>,<axis_to_be_deleted>)

```
# Row deletion. We use axis=0(First axis). Delete the second row(1).
>>> array_1
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> np.delete(array_1,1,axis=0)
array([[1, 2, 3],
       [7, 8, 9]])
```
```
# Column deletion. We use axis=1(Second axis), Delete the second column(1).
>>> array_1
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> np.delete(array_1,1,axis=1)
array([[1, 3],
       [4, 6],
       [7, 9]])
```

### Aggregating Methods
- `sum` sums all numbers. If parameter `axis=0` aggregates across rows. If parameter `axis=1` aggregates across columns.

```
>>> import numpy as np
>>> numbers = np.array([[1,2,3],[4,5,6],[7,8,9]])
>>> numbers
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> numbers.sum()
np.int64(45)
>>> numbers.sum(axis=0)
array([12, 15, 18])
>>> numbers.sum(axis=1)
array([ 6, 15, 24])
```
- `min`, `max` :- finds `min` or `max` out of all elements.
- `mean`.
- `sum`
- `cumsum` :- 

### Vectorized Operations
- Single number in Math is called as 'scalar'.
- Add 9(Scalar) to every element of array.
```
>>> numbers
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> numbers + 9
array([[10, 11, 12],
       [13, 14, 15],
       [16, 17, 18]])
```
- Vectorized Python functions like `len`.

```
>>> llms
array(['chatgpt', 'claude', 'gemini'], dtype='<U7')
>>> vectorize_upper = np.vectorize(str.upper)
>>> vectorize_upper(llms)
array(['CHATGPT', 'CLAUDE', 'GEMINI'], dtype='<U7')
```

### Broadcasting 
- `broadcasting` allows mathematical operations of arrays of different sizes. Below 'add' array is 'broadcasted'.

```
>>> number_arrays
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> add_array = np.array([[1],[2],[3]])
>>> add_array
array([[1],
       [2],
       [3]])
>>> number_arrays + add_array
array([[ 2,  3,  4],
       [ 6,  7,  8],
       [10, 11, 12]])
```
- `broadcasting` rules :- 
       - compare array dimensions from 'right' to 'left'.
       - two dimensions are compatible when 'one' of dimension is either '1' or both dimensions are equal. Example (10,5) and (10,1) are compatible. (10,5) and (5,10) are not compatible.


### Saving and Loading Numpy Arrays
- `numpy` files can be saved as `.npy` format.
- `load` numpy file.
```
with open("numbers.numpy", "r") as f:
       numbers_array = np.load(f)
```
- `save` numpy file.

```
with open("numbers.numpy","r") as f:
       np.save(f)
```

### Array modifications
- Used in AI/ML techniques like `data augmentation`. `data augmentation` is process of adding additional data by performing small changes on existing data.
- `flip`.
```
>>> import numpy as np
>>> numbers_arrays = np.array([[1,2,3],[4,5,6],[7,8,9]])
>>> numbers_arrays
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> np.flip(numbers_arrays)
array([[9, 8, 7],
       [6, 5, 4],
       [3, 2, 1]])
>>> np.flip(numbers_arrays,axis=0)
array([[7, 8, 9],
       [4, 5, 6],
       [1, 2, 3]])
>>> np.flip(numbers_arrays,axis=1)
array([[3, 2, 1],
       [6, 5, 4],
       [9, 8, 7]])
```
- `transpose`

```
>>> numbers_arrays
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> np.transpose(numbers_arrays)
array([[1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]])
```

### Stacking and Splitting 
- `split`
- `stack` :- stack list of arrays.