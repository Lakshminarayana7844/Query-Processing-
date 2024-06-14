import pandas as pd

# Load the dataset
data = {
    'Year': [1986, 1986, 1985, 1986, 1987],
    'WHO region': ['Western Pacific', 'Americas', 'Africa', 'Americas', 'Americas'],
    'Country': ['Viet Nam', 'Uruguay', "Côte d'Ivoire", 'Colombia', 'Saint Kitts and Nevis'],
    'Beverage Types': ['Wine', 'Other', 'Wine', 'Beer', 'Beer'],
    'Display Value': [0.00, 0.50, 1.62, 4.27, 1.98]
}

df = pd.DataFrame(data)

# Display the dimensions or shape of the DataFrame
print("Dimensions/Shape of the DataFrame:", df.shape)

# Extracting column names from the DataFrame
column_names = df.columns.tolist()
print("\nColumn Names:")
for col in column_names:
    print(col)
