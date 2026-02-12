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