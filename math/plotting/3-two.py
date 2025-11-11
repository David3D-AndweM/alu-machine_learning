#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

# Plot both lines
plt.plot(x, y1, 'r--', label='C-14')
plt.plot(x, y2, 'g-', label='Ra-226')

# Set axis labels
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')

# Set title
plt.title('Exponential Decay of Radioactive Elements')

# Set axis ranges
plt.xlim(0, 20000)
plt.ylim(0, 1)

# Add legend in upper right corner
plt.legend(loc='upper right')

# Display the plot
plt.show()
