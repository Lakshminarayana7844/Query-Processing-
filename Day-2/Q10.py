import pandas as pd
import numpy as np

# Create a DataFrame with ten rows and four columns with random values
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))

# Define a function to highlight negative values in red and positive values in black
def highlight_values(data):
    # Create a DataFrame of colors, where the colors are based on the values of `data`
    color = np.where(data < 0, 'color: red;', 'color: black;')
    return pd.DataFrame(color, index=data.index, columns=data.columns)

# Apply the function to the DataFrame
styled_df = df.style.apply(highlight_values, axis=None)

# Save the styled DataFrame to an HTML file
styled_df.to_html('styled_dataframe.html')

print("Styled DataFrame has been saved to 'styled_dataframe.html'.")
