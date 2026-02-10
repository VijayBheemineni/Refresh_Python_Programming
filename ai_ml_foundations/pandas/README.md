# Pandas

Pandas is a powerful data manipulation and analysis library, providing DataFrames and Series for working with structured data.

## Topics

- DataFrames and Series
- Data loading and saving
- Data cleaning and preprocessing
- Grouping and aggregation
- Merging and joining datasets

## Install Pandas
```
pip install pandas
```
## Pandas Basics
- High level data manipulation tool built on `NumPy`.

### Creation of data frame.

- Creating `DataFrame` from dictionary. In this case the 'columns' of structured data are 'keys' and 'values' are values of column. `pandas` labels the rows as 0,1,2,3 by default. We can set this using `llms.index = ['A','G','O','M']`.

```
>>> import pandas as pd
>>> data = {
... 'company':['anthropic','google','openai','meta'],
... 'models':['claude','gemini','chatgpt','llama']
... }
>>> llms = pd.DataFrame(data)
>>> llms
     company   models
0  anthropic   claude
1     google   gemini
2     openai  chatgpt
3       meta    llama

# Setting Index. Instead of default row value 0,1,2,3,
>>> llms.index = ['A','G','O','M']
>>> llms
     company   models
A  anthropic   claude
G     google   gemini
O     openai  chatgpt
M       meta    llama
```
- Creating `DataFrame` from CSV file.

```
>>> import pandas as pd
# Below we are asking 'pandas' to use first column values as 'index' values.
>>> llms = pd.read_csv('llms.csv', index_col=0)
>>> llms
     Company     Model
_                     
A  Anthropic    Claude
G     Google    Gemini
O     OpenAI   ChatGpt
M       Meta     Llama
```

### Index and select data
#### Column 
- Lets suppose we want entire column. We use `[]` to provide the column name. This returns `Panda Series`. `Panda Series` is like a list of values or more like numpy array.
```
>>> llms['Company']
_
A    Anthropic
G       Google
O       OpenAI
M         Meta
Name: Company, dtype: str
>>> type(llms['Company'])
<class 'pandas.Series'>
```
- If we want `DataFrame` then we need to use '[[]]'

```
>>> llms[['Company']]
     Company
_           
A  Anthropic
G     Google
O     OpenAI
M       Meta

>>> type(llms[['Company']])
<class 'pandas.DataFrame'>
```
- Select multiple columns and get a `DataFrame`

```
>>> llms[['Company','Model']]
     Company     Model
A  Anthropic    Claude
G     Google    Gemini
O     OpenAI   ChatGpt
M       Meta     Llama
>>> type(llms[['Company','Model']])
<class 'pandas.DataFrame'>
```

#### Rows
- Get data from particular rows.

```
>>> llms
     Company     Model
A  Anthropic    Claude
G     Google    Gemini
O     OpenAI   ChatGpt
M       Meta     Llama
>>> llms[0:3]
     Company     Model
A  Anthropic    Claude
G     Google    Gemini
O     OpenAI   ChatGpt
>>> type(llms[0:3])
<class 'pandas.DataFrame'>
```

#### Rows and columns
- Generally we want feature like 'NumPy' like `array[rows, columns]`. We can do this kind of access using `loc(label)` or `iloc`(integer) methods.

#### Rows
- Get a row based on index. For example 'A'. This returns `Panda Series`.

```
>>> llms
     Company     Model
A  Anthropic    Claude
G     Google    Gemini
O     OpenAI   ChatGpt
M       Meta     Llama
>>> llms.loc["A"]
Company    Anthropic
Model         Claude
Name: A, dtype: str
>>> type(llms.loc["A"])
<class 'pandas.Series'>

>>> llms.loc[["A"]]
     Company    Model
A  Anthropic   Claude

>>> type(llms.loc[["A"]])
<class 'pandas.DataFrame'>
```
- Multiple rows.

```
>>> llms.loc[["A", "G"]]
     Company    Model
A  Anthropic   Claude
G     Google   Gemini
>>> type(llms.loc[["A","G"]])
<class 'pandas.DataFrame'>
```
- We want to select data from particular rows and columns. We need to define of format `llms.loc[[<ROWS>],[<Columns>]]

```
>>> llms.loc[["A"],["Company"]]
     Company
A  Anthropic
>>> type(llms.loc[["A"],["Company"]])
<class 'pandas.DataFrame'>
```
- Get all rows for a column.
```
>>> llms.loc[:,['Company']]
     Company
A  Anthropic
G     Google
O     OpenAI
M       Meta
```
- Get all columns for a row.
```
>>> llms.loc[['A'],:]
     Company    Model
A  Anthropic   Claude
```

### Misc Commands
- Get all columns. 

```
llms.columns
```