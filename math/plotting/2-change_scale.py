#!/usr/bin/env python3
"""
Module for plotting with logarithmic scale.

This module creates a line graph showing exponential decay of C-14
with logarithmic y-axis scaling.
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# Plot the line
plt.plot(x, y)

# Set axis labels
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')

# Set title
plt.title('Exponential Decay of C-14')

# Set logarithmic scale for y-axis
plt.yscale('log')

# Set x-axis range from 0 to 28650
plt.xlim(0, 28650)

# Display the plot
plt.show()
