"""
Concept: Matplotlib Visuals

This example demonstrates creating and customizing plots with matplotlib.
Students will learn about visualization, labeling, and file I/O operations.
"""

# Task 3 - Matplotlib Visuals (Example File)
# This file demonstrates creating and customizing a plot

import matplotlib.pyplot as plt
import numpy as np
import os

# Create outputs directory if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Create basic data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a simple plot
plt.plot(x, y)
plt.savefig("outputs/basic_plot.jpg")
plt.close()
print("Basic plot saved as 'outputs/basic_plot.jpg'")

# Create a plot with customizations (Uncomment Below)
# -------------------------------------------
# plt.figure(figsize=(10, 6))
# plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)
# plt.xlabel('X values')
# plt.ylabel('Y values')
# plt.title('Sine Wave Function')
# plt.legend()
# plt.grid(True, alpha=0.3)
# plt.savefig('outputs/customized_plot.jpg')
# plt.close()
# print("Customized plot saved as 'outputs/customized_plot.jpg'")

# Create multiple plots on same figure (Uncomment Below)
# -------------------------------------------
# plt.figure(figsize=(12, 8))
#
# # Plot 1: Sine wave
# plt.subplot(2, 2, 1)
# plt.plot(x, np.sin(x), 'b-', label='sin(x)')
# plt.title('Sine Wave')
# plt.legend()
# plt.grid(True, alpha=0.3)
#
# # Plot 2: Cosine wave
# plt.subplot(2, 2, 2)
# plt.plot(x, np.cos(x), 'r-', label='cos(x)')
# plt.title('Cosine Wave')
# plt.legend()
# plt.grid(True, alpha=0.3)
#
# # Plot 3: Combined plot
# plt.subplot(2, 2, 3)
# plt.plot(x, np.sin(x), 'b-', label='sin(x)')
# plt.plot(x, np.cos(x), 'r-', label='cos(x)')
# plt.title('Sine and Cosine')
# plt.legend()
# plt.grid(True, alpha=0.3)
#
# # Plot 4: Scatter plot
# plt.subplot(2, 2, 4)
# x_scatter = np.random.randn(50)
# y_scatter = np.random.randn(50)
# plt.scatter(x_scatter, y_scatter, alpha=0.6, color='green')
# plt.title('Random Scatter')
# plt.grid(True, alpha=0.3)
#
# plt.tight_layout()
# plt.savefig('outputs/multiple_plots.jpg')
# plt.close()
# print("Multiple plots saved as 'outputs/multiple_plots.jpg'")

# Save plot to file (Uncomment Below)
# -------------------------------------------
# plt.figure(figsize=(10, 6))
# plt.plot(x, np.sin(x), label='sin(x)', color='blue', linewidth=2)
# plt.plot(x, np.cos(x), label='cos(x)', color='red', linewidth=2)
# plt.xlabel('X values')
# plt.ylabel('Y values')
# plt.title('Trigonometric Functions')
# plt.legend()
# plt.grid(True, alpha=0.3)
#
# # Save the plot
# plt.savefig('outputs/trigonometric_plot.jpg', dpi=300, bbox_inches='tight')
# print("Plot saved as 'outputs/trigonometric_plot.jpg'")
# plt.close()

# Advanced customization (Uncomment Below)
# -------------------------------------------
# fig, ax = plt.subplots(figsize=(12, 8))
#
# # Create multiple lines with different styles
# ax.plot(x, np.sin(x), 'b-', linewidth=2, label='sin(x)')
# ax.plot(x, np.cos(x), 'r--', linewidth=2, label='cos(x)')
# ax.plot(x, np.sin(x) * np.cos(x), 'g:', linewidth=3, label='sin(x) * cos(x)')
#
# # Customize the plot
# ax.set_xlabel('X values', fontsize=12)
# ax.set_ylabel('Y values', fontsize=12)
# ax.set_title('Advanced Trigonometric Functions', fontsize=14, fontweight='bold')
# ax.legend(fontsize=10)
# ax.grid(True, alpha=0.3)
# ax.set_xlim(0, 10)
# ax.set_ylim(-1.5, 1.5)
#
# # Add text annotation
# ax.annotate('Maximum of sin(x)', xy=(np.pi/2, 1), xytext=(np.pi/2 + 1, 1.2),
#             arrowprops=dict(arrowstyle='->', color='black'),
#             fontsize=10)
#
# plt.tight_layout()
# plt.savefig('outputs/advanced_plot.jpg', dpi=300, bbox_inches='tight')
# print("Advanced plot saved as 'outputs/advanced_plot.jpg'")
# plt.close()
