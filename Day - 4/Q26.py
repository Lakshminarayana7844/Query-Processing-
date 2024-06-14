import matplotlib.pyplot as plt

# Sample data for the plots
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]
y3 = [3, 5, 7, 9, 12]
y4 = [2, 4, 6, 8, 10]

# Create a figure with 2 rows and 2 columns of subplots
plt.figure(figsize=(10, 8))

# First subplot
plt.subplot(2, 2, 1)  # (rows, columns, panel number)
plt.plot(x, y1, label='Line 1', color='blue')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Plot 1')
plt.legend()
plt.grid(True)

# Second subplot
plt.subplot(2, 2, 2)
plt.plot(x, y2, label='Line 2', color='red')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Plot 2')
plt.legend()
plt.grid(True)

# Third subplot
plt.subplot(2, 2, 3)
plt.plot(x, y3, label='Line 3', color='green')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Plot 3')
plt.legend()
plt.grid(True)

# Fourth subplot
plt.subplot(2, 2, 4)
plt.plot(x, y4, label='Line 4', color='purple')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Plot 4')
plt.legend()
plt.grid(True)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
