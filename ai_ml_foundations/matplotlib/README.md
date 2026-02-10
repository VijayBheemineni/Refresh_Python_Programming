# Matplotlib

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

## Topics

- Basic plotting
- Customizing plots
- Subplots and layouts
- Different plot types (line, bar, scatter, histogram)
- Saving figures

## Install Matplotlib
```
pip install matplotlib
```

## Matplotlib basics
- `matplotlib` is a library for creating visulizations.
- Customization of Matplotlib
    - Axis lables :- `plt.xlabel`, `plt.ylabel`.
    - Title :- `plt.title`
    - Ticks :- start of numbering xaxis and yaxis. plt.yticks([2,4,6,8],[10,20,30,40])

### Line Plot
- Generally its better when 'time' is on x-axis.
```
# Default 'line' plot
>>> import matplotlib.pyplot as plt
>>> x_axis = [0,1]
>>> y_axis = [0,1]
>>> plt.plot(x_axis,y_axis)
[<matplotlib.lines.Line2D object at 0x106c774d0>]
>>> plt.xlabel("X Axis")
Text(0.5, 47.04444444444444, 'X Axis')
>>> plt.ylabel("Y Axis")
>>> plt.title("Hello Matplotlib")
Text(0.5, 1.0, 'Hello Matplotlib')
>>> plt.show()
```

### Scatter plot
- is better we are trying a correlation between two variables.
```
>>> x_axis = [0,1]
>>> y_axis = [0,1]
>>> plt.scatter(x_axis,y_axis)
<matplotlib.collections.PathCollection object at 0x106cb01a0>
>>> plt.ylabel("Y Axis")
Text(85.06944444444443, 0.5, 'Y Axis')
>>> plt.xlabel("X Axis")
Text(0.5, 47.04444444444444, 'X Axis')
>>> plt.title("Hello Scatter Matplotlib")
Text(0.5, 1.0, 'Hello Scatter Matplotlib')
>>> plt.show()
```

### Histogram
- Shows distribution of variables.

```
import matplotlib.pyplot as plt
numbers = [1,2,3,4,5,6,7,8,9,2,4,6,7,1,1,9,5,1,1,1,1]
# Second parameter number of bins. By default 10
plt.hist(numbers,3)
plt.show()
```