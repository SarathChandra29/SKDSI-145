import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(0, 10, 100)
y1_values = np.sin(x_values)
y2_values = np.cos(x_values)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(x_values, y1_values, label='sin(x)', color='blue', linestyle='-')
ax1.set_title('Sine Function')
ax1.set_xlabel('x-axis')
ax1.set_ylabel('sin(x)')
ax1.grid(True)
ax1.legend(loc='upper right')
ax1.set_xticks(np.arange(0, 11, 1))
ax1.set_yticks(np.arange(-1, 1.5, 0.5))
ax1.set_xticklabels([f'{i}' for i in range(11)])
ax1.set_yticklabels([f'{i:.1f}' for i in np.arange(-1, 1.5, 0.5)])
ax1.annotate('Max Value', xy=(np.pi/2, 1), xytext=(np.pi/2+1, 0.8),
             arrowprops=dict(facecolor='black', shrink=0.05))

ax2.plot(x_values, y2_values, label='cos(x)', color='red', linestyle='--')
ax2.set_title('Cosine Function')
ax2.set_xlabel('x-axis')
ax2.set_ylabel('cos(x)')
ax2.grid(True)
ax2.legend(loc='upper right')
ax2.set_xticks(np.arange(0, 11, 1))
ax2.set_yticks(np.arange(-1, 1.5, 0.5))
ax2.set_xticklabels([f'{i}' for i in range(11)])
ax2.set_yticklabels([f'{i:.1f}' for i in np.arange(-1, 1.5, 0.5)])
ax2.annotate('Min Value', xy=(np.pi, -1), xytext=(np.pi+1, -0.8),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()
plt.savefig('line_plot_with_annotations.png')
plt.show()
