import pandas as pd
import numpy as np

# Step 1: Create a DataFrame with ten rows and four columns with random values
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))

# Step 2: Define a function to set the background color to black and font color to yellow
def set_styles(val):
    return 'background-color: black; color: yellow;'

# Apply the function to the DataFrame using applymap
styled_df = df.style.applymap(set_styles)

# Save the styled DataFrame to an HTML file
styled_df.to_html('styled_dataframe.html')

print("Styled DataFrame has been saved to 'styled_dataframe.html'.")
