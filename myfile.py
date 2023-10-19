# This is a Python comment.
print("Hello, World!")


import pandas as pd
data = {
    'ProductID': [1, 2, 3, 4, 5],
    'ProductName': ['Widget A', 'Widget B', 'Widget C', 'Widget A', 'Widget B'],
    'UnitPrice': [10.0, 15.0, 12.0, 10.0, 15.0],
    'QuantitySold': [100, 150, 120, 80, 100],
    'CustomerID': [101, 102, 103, 104, 105],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
#Let's create a sample dataset for this scenario:

import pandas as pd
df=pd.read_csv(salesdata.csv)
print(df)
#Read Data from CSV

df.head(): Display the first few rows of the DataFrame.
print("\n Display the last few rows of the DataFrame")
print(df.head(3))

df.tail(): Display the last few rows of the DataFrame.
print("\n Display the last few rows of the DataFrame.")
print(df.tail(3))

df.shape: Get the dimensions (rows, columns) of the DataFrame.
rows,columns =df.shape
print(df.shape)

df.info(): Display information about the DataFrame, including data types.
df=pd.DataFrame(data)
print("\n  Display information about the DataFrame, including data types")
print(df.info())

df.describe(): Generate summary statistics for numeric columns.
description = df.describe()
print(description)
print( df.describe())

df.columns: Access the column names.
columns = df.columns
print(columns)

df=pd.DataFrame(data, index=['day1','day2','day3','day4','day5'])
print("\n  Access the row index")
index = df.index
print(index)
print(df)


name_column = df['ProductID']
print(name_column)

df=pd.DataFrame(data, index=['day1','day2','day3','day4','day5'])
print("\n Access rows and columns by label")
print(df.loc['day1'])

df.set_index('ProductName', inplace=True)
row_data = df.loc['Widget A']
print(f"Data for 'Widget A':\n{row_data}")


df=pd.DataFrame(data)
print(df.isnull())


df.dropna(inplace=True)
print(df)


df=pd.DataFrame(data)
df['TotalSales'] = df['UnitPrice'] * df['QuantitySold']
print(f"Create a new column for total sales.:\n{df}")


df['TotalSales'] = df['UnitPrice'] * df['QuantitySold']
total_sales_bycategory = df.groupby('ProductID')['TotalSales'].sum()
print(f"Calculate total sales for each product..:\n{df}")


df_sort = df.sort_values(by="Date",ascending=False)
print(f"Sort the DataFrame by date in descending order..:\n{df_sort}")

output_file_path = "transformed_salesdata.csv"
new_df.to_csv(output_file_path, index=False)
print(f"Save the transformed DataFrame to a CSV file using:\n{new_df}")


import pandas as pd
df=pd.read_csv('transformed_salesdata.csv')
pivottable=df.pivot_table(index='ProductID',values='QuantitySold', aggfunc='sum')
print(pivottable)

df_stack =df.stack()
df_unstack=df_stack.unstack()
print(df_stack )


df_query=df.query('QuantitySold > 100')
print(f"filtering based on expressions\n{df_query}")


df_grouped=df.groupby('ProductName')['QuantitySold'].agg(['mean','median','std'])
print(f" custom aggregation functions\n{df_grouped}")


df_duplicates =df.duplicated()
remove_duplicates=df.drop_duplicates()
print(f"find  duplicates\n{df_duplicates}")
print(f"remove duplicates\n{remove_duplicates}")


new_date_rng = pd.date_range(start='1/1/2023', periods=5, freq='D')
df['Date'] = new_date_rng
df.set_index('Date', inplace=True)
resampled_df = df.resample('3D').sum()
print(f"time series function\n{resampled_df}")


df_rolling = df['QuantitySold'].rolling (window = 2).mean()
print(f"time series function\n{df_rolling}")


