import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

# Create the horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(languages, popularity, color=['blue', 'green', 'red', 'cyan', 'magenta', 'yellow'])

# Add labels and title
plt.xlabel('Popularity (%)')
plt.ylabel('Programming Languages')
plt.title('Popularity of Programming Languages')

# Display the plot
plt.show()
