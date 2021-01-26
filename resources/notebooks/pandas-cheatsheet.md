## **`pandas` cheatsheet**

In the first day of the course you will be challenged to establish an Exploratory Data Analysis and a Data Visualization process. Those must be handled throughout the use of the `pandas` python library. To that purpose here is a cheatsheet where you can check the basic operations that can be made with it.

### **List of the commands**

>- `pandas.DataFrame(data)` - create a new DataFrame.

```console
>>> import pandas as pd
>>> data_ = {'col1': [1, 2], 'col2': [3, 4]}
>>> df_v1_ = pd.DataFrame(data)
>>> data_ = [['col1', 'col2', 'col3'], [1, 2, 3], [4, 5, 6]]
>>> headers_ = data.pop(0)
>>> df_v2_ = pd.DataFrame(data_, columns=headers_)
```

>- `pandas.DataFrame(data).to_csv('path_to_csv')` - to save the DataFrame as a .csv file in your local directory. The DataFrame can be saved in other formats like parquet and for that purpose, it is only required the change from `to_csv` to `to_parquet`.

```console
>>> df_v1.to_csv('C://Users/leonidas/Desktop/data-engineer-fundaments/first-pd-df.csv')
```

>- `pandas.read_csv('path_to_csv')` - to create a DataFrame from a .csv file. Similarly to the previous command, a `pandas` DataFrame can be created from other file formats.

```console
>>> df_ = pd.read_csv('C://Users/leonidas/Desktop/data-engineer-fundamentals/first-pd-df.csv')
```

>- `df.head(n)` - to display the first n records of the DataFrame.

```console
>>> df_.head(10)
```

>- `df.drop(['value1', 'value3'])` - drop values from the rows (if the value of the axis is 0) or columns (if the value of the axis is 1) of DataFrame.

```console
>>> df_.drop('value1', axis=1)
```

>- `df.columns` - to obtain or rename the columns of the DataFrame.

```console
>>> df_v1_.columns.to_list()
>>> ['col1', 'col2']
>>> df_v2_.columns = ['day_1', 'day_2', 'day_3']
```

>- `df.sort_values(by=[column_name])` - to sort the values of a certain column.

```console
>>> df_v2.sort_values(by='day_3', ascending=False)
```

For further insights you can always check the [official documentation](https://pandas.pydata.org/pandas-docs/stable/index.html) of `pandas` library.
