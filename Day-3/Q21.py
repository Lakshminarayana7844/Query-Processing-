import pandas as pd

# Sample DataFrame
data = {'Column': ['Apple', 'Banana', 'Grape', 'Orange', 'Kiwi']}
df = pd.DataFrame(data)

# Specified character column to swap cases
column_name = 'Column'

# Swap the cases of the specified column
df[column_name] = df[column_name].str.swapcase()

print("DataFrame with cases swapped:")
print(df)
