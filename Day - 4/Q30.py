import matplotlib.pyplot as plt
import numpy as np

# Sample data
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]
groups = ['G1', 'G2', 'G3', 'G4', 'G5']

# Define the width of the bars
bar_width = 0.35

# Define the positions of the bars
index = np.arange(len(groups))

# Create the bar plot
plt.figure(figsize=(10, 6))

# Plot bars for men
plt.bar(index, means_men, bar_width, label='Men', color='blue')

# Plot bars for women, adjusting the x position by the width of the bars
plt.bar(index + bar_width, means_women, bar_width, label='Women', color='green')

# Adding labels and title
plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(index + bar_width / 2, groups)  # Adjust x-ticks to be centered

# Adding legend
plt.legend()

# Display the plot
plt.show()
