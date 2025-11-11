#!/usr/bin/env python3
"""
Module for plotting a line graph.

This module contains code to plot y = x^3 as a solid red line
with x-axis ranging from 0 to 10.
"""

import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# Plot y as a solid red line
plt.plot(y, 'r-')

# Set x-axis range from 0 to 10
plt.xlim(0, 10)

# Display the plot
plt.show()
