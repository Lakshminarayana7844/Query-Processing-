import pandas as pd
import numpy as np

# Step 1: Create a DataFrame with ten rows and four columns with random values
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))

# Step 2: Introduce NaN values randomly
nan_indices = [(np.random.randint(10), np.random.randint(4)) for _ in range(5)]
for row, col in nan_indices:
    df.iat[row, col] = np.nan

# Step 3: Define a function to highlight NaN values
def highlight_nan(data):
    # Create a DataFrame of styles, with 'background-color: yellow;' for NaNs
    style = data.isna().replace({True: 'background-color: yellow;', False: ''})
    return style

# Apply the function to the DataFrame
styled_df = df.style.apply(highlight_nan, axis=None)

# Save the styled DataFrame to an HTML file
styled_df.to_html('styled_nan_dataframe.html')

print("Styled DataFrame with NaN values highlighted has been saved to 'styled_nan_dataframe.html'.")
