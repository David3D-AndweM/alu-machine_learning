#!/usr/bin/env python3
"""
Module for creating a scatter plot.

This module creates a scatter plot of Men's Height vs Weight
with magenta points and proper axis labels.
"""

import numpy as np
import matplotlib.pyplot as plt

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y += 180

# Create scatter plot with magenta points
plt.scatter(x, y, c='magenta')

# Set axis labels
plt.xlabel('Height (in)')
plt.ylabel('Weight (lbs)')

# Set title
plt.title("Men's Height vs Weight")

# Display the plot
plt.show()
