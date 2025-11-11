#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

# Define the data
people = ['Farrah', 'Fred', 'Felicia']
fruits = ['apples', 'bananas', 'oranges', 'peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

# Create the stacked bar chart
bar_width = 0.5
x_pos = np.arange(len(people))

# Create bottom array for stacking
bottom = np.zeros(len(people))

# Plot each fruit type
for i in range(len(fruits)):
    plt.bar(x_pos, fruit[i], bar_width, bottom=bottom, 
             color=colors[i], label=fruits[i])
    bottom += fruit[i]

# Set labels and title
plt.xlabel('Person')
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')

# Set x-axis ticks and labels
plt.xticks(x_pos, people)

# Set y-axis range and ticks
plt.ylim(0, 80)
plt.yticks(range(0, 81, 10))

# Add legend
plt.legend()

# Display the plot
plt.show()
