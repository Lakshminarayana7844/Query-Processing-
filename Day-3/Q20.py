import pandas as pd

# Sample DataFrame
data = {'Column': ['apple', 'banana', 'grape', 'orange', 'kiwi']}
df = pd.DataFrame(data)

# Substring to search for
substring = 'ra'

# Find index of rows containing the substring in the 'Column' column
index_list = df[df['Column'].str.contains(substring)].index.tolist()

print("Indexes of rows containing the substring '{}':".format(substring))
print(index_list)
