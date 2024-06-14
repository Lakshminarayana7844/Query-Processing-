import matplotlib.pyplot as plt

# Sample data for multiple lines
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]
y3 = [3, 5, 7, 9, 12]

# Plotting the lines with different colors and widths
plt.plot(x, y1, label='Line 1', color='blue', linewidth=2)
plt.plot(x, y2, label='Line 2', color='red', linewidth=4)
plt.plot(x, y3, label='Line 3', color='green', linewidth=6)

# Adding labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Multiple Lines with Different Widths and Colors')

# Adding legend
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
