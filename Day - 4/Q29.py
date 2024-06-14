import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

# Assign a unique color for each bar
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'orange']

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(languages, popularity, color=colors)

# Add labels and title
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages')

# Display the plot
plt.show()
