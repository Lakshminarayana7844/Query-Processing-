import pandas as pd
import matplotlib.pyplot as plt

# Sample financial data
data = {
    'Date': ['10-03-16', '10-04-16', '10-05-16', '10-06-16', '10-07-16'],
    'Open': [774.25, 776.030029, 779.309998, 779, 779.659973],
    'High': [776.065002, 778.710022, 782.070007, 780.47998, 779.659973],
    'Low': [769.5, 772.890015, 775.650024, 775.539978, 770.75],
    'Close': [772.559998, 776.429993, 776.469971, 776.859985, 775.080017]
}

# Convert the data to DataFrame
df = pd.DataFrame(data)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Filter the data for the specified date range
start_date = '2016-10-03'
end_date = '2016-10-07'
mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
filtered_df = df.loc[mask]

# Plotting the line charts for Open, High, Low, and Close prices
plt.figure(figsize=(10, 6))
plt.plot(filtered_df['Date'], filtered_df['Open'], label='Open', marker='o')
plt.plot(filtered_df['Date'], filtered_df['High'], label='High', marker='o')
plt.plot(filtered_df['Date'], filtered_df['Low'], label='Low', marker='o')
plt.plot(filtered_df['Date'], filtered_df['Close'], label='Close', marker='o')

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Financial Data of Alphabet Inc. (Oct 3, 2016 - Oct 7, 2016)')
plt.legend()

# Display the plot
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
