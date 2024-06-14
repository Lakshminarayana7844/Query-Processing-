import matplotlib.pyplot as plt

# Read data from the text file
with open('/Users/lakshminarayanamandi/Downloads/Movies/QP/text1.txt', 'r') as file:
    lines = file.readlines()

# Extract x and y values from the data
x = []
y = []
for line in lines:
    values = line.split()
    x.append(int(values[0]))
    y.append(int(values[1]))

# Plotting the line
plt.plot(x, y)

# Adding labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Line Plot with Labels')

# Display the plot
plt.show()
