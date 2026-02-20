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
### Filtering
- Filtering based on column values. Below we will filter out companies which start with 'A'.

```
>>> import pandas as pd
>>> llms = pd.read_csv('llms.csv', index_col=0)
>>> llms
     Company     Model
A  Anthropic    Claude
G     Google    Gemini
O     OpenAI   ChatGpt
M       Meta     Llama
>>> llms["Company"].str.startswith("A")
A     True
G    False
O    False
M    False
Name: Company, dtype: bool
>>> companies_start_with_a = llms["Company"].str.startswith("A")
>>> llms[companies_start_with_a]
     Company    Model
A  Anthropic   Claude
```
### Iterate rows
- Iterate the rows of dataframe using `iterrows`. This method returns `row label` and `row` as output.

```
>>> for row_label, row in llms.iterrows():
...     print(f"{row_label} : {row}")
... 
A : Company    Anthropic
Model         Claude
Name: A, dtype: str
G : Company     Google
Model       Gemini
Name: G, dtype: str
O : Company      OpenAI
Model       ChatGpt
Name: O, dtype: str
M : Company      Meta
Model       Llama
Name: M, dtype: str

# Select particular column values only.
>>> for row_label, row in llms.iterrows():
...     print(f"{row_label} : {row['Company']}")
... 
A : Anthropic
G : Google
O : OpenAI
M : Meta
```

### Add new columns
```
>>> llms["company_model"] = llms["Company"] + "_" + llms["Model"]
>>> llms
     Company     Model      company_model
A  Anthropic    Claude  Anthropic_ Claude
G     Google    Gemini     Google_ Gemini
O     OpenAI   ChatGpt    OpenAI_ ChatGpt
M       Meta     Llama        Meta_ Llama

# Add new column using 'apply' method.
>>> llms["UpperCase_CompanyName"] = llms["Company"].apply(str.upper)
>>> llms
     Company     Model      company_model UpperCase_CompanyName
A  Anthropic    Claude  Anthropic_ Claude             ANTHROPIC
G     Google    Gemini     Google_ Gemini                GOOGLE
O     OpenAI   ChatGpt    OpenAI_ ChatGpt                OPENAI
M       Meta     Llama        Meta_ Llama                  META

```
### Misc Commands
- Get all columns. 

```
llms.columns
```

## Importing Data from files

### CSV, TSV files
- `read_csv` is used to 'csv/tsv' kind of files. We can use optional parameter `sep='\t'` to load `tsv` file.
- Using optional parameter `usecols` we can limit optional columns to be loaded.

```
>>> llms_companies = pd.read_csv('llms.csv', usecols=col_names)
>>> llms_companies
     Company
0  Anthropic
1     Google
2     OpenAI
3       Meta

# By using column numbers
>>> llms_companies = pd.read_csv('llms.csv', usecols=[1])
>>> llms_companies
     Company
0  Anthropic
1     Google
2     OpenAI
3       Meta
```
- Using optional parameter `nrows` to limit number of rows.

```
>>> llms_rows = pd.read_csv('llms.csv',nrows=2)
>>> llms_rows
  Unnamed: 0    Company    Model
0          A  Anthropic   Claude
1          G     Google   Gemini
```
- Limiting rows using `nrows` or `skiprows`. 
```
>>> llms
  Unnamed: 0    Company     Model
0          A  Anthropic    Claude
1          G     Google    Gemini
2          O     OpenAI   ChatGpt
3          M       Meta     Llama
>>> llms_rows = pd.read_csv('llms.csv',nrows=2, skiprows=1)
>>> llms_rows
   A Anthropic    Claude
0  G    Google    Gemini
1  O    OpenAI   ChatGpt
```
- We can use optional parameter `header=None` for files which don't have column names.
- Assign columns names we use `names` which takes list of column names.

### Handling errors and missing data
- When importing data by default infers column data types. `dtypes` attributes shows datatypes of columns.
- For `read_csv` we can pass optional parameter `dtype` which defines column types. `dtype` is a dictionary of column names and data types.

```
>>> llms=pd.read_csv('llms.csv',dtype={"Company": str, "Model": str})
>>> llms.dtypes
Unnamed: 0    str
Company       str
Model         str
dtype: object
```
- `pandas` automatically interprets some values as missing or NA. We can use `na_values` parameters. For example `na_values={"ModelVersion": 0}`
- Lines that `pandas` can't parse. We can use `error_bad_lines=False` to skip unparseable records. We can use `warn_bad_lines=True` to see messages when records are missed.