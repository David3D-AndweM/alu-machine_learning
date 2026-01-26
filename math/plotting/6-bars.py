#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

people = ['Farrah', 'Fred', 'Felicia']
fruits = ['apples', 'bananas', 'oranges', 'peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

bar_width = 0.5
x_pos = np.arange(len(people))

bottom = np.zeros(len(people))

for i in range(len(fruits)):
    plt.bar(x_pos, fruit[i], bar_width, bottom=bottom, 
             color=colors[i], label=fruits[i])
    bottom += fruit[i]

plt.xlabel('Person')
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')

plt.xticks(x_pos, people)

plt.ylim(0, 80)
plt.yticks(range(0, 81, 10))

plt.legend()

plt.show()
