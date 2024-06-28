import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x_values = np.random.rand(100)
y_values = 2 * x_values + np.random.normal(0, 0.1, 100)  

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x_values, y_values, alpha=0.7)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of X vs. Y')
plt.grid(True)
plt.show()
