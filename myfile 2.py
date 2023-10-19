import pandas as pd
df=pd.read_csv('salesdata.csv')
print(df)

import pandas as pd
df=pd.read_csv('salesdata.csv')
new_df=df.dropna()
print(new_df.to_string())

import pandas as pd
df=pd.read_csv('salesdata.csv')
df['Total Sales'] = df['Units Sold'] * df['Unit Price']
print(df.to_string())

import pandas as pd
df=pd.read_csv('salesdata.csv')
df['Total Sales'] = df['Units Sold'] * df['Unit Price']
print(df.to_string())
total_sales_by_category = df.groupby('Product Category')['Total Sales'].sum()
print(total_sales_by_category)

output_file_path = "transformed_sales_data.csv"
new_df.to_csv(output_file_path, index=False)


summary_stats = df.groupby('Product Category')['Total Sales'].agg(['mean', 'median', 'std'])
print(summary_stats)
