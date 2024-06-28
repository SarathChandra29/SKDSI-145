import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Group A': [4, 7, 1, 8, 5],
    'Group B': [5, 2, 8, 3, 6],
    'Group C': [7, 5, 3, 4, 9]
}
index = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']

# Creating a DataFrame
df = pd.DataFrame(data, index=index)

# Side-by-side bar plot
ax1 = df.plot(kind='bar', figsize=(10, 6))
ax1.set_xlabel('Items')
ax1.set_ylabel('Values')
ax1.set_title('Side-by-Side Bar Plot')
plt.xticks(rotation=0)
plt.show()

# Stacked bar plot
ax2 = df.plot(kind='bar', stacked=True, figsize=(10, 6))
ax2.set_xlabel('Items')
ax2.set_ylabel('Values')
ax2.set_title('Stacked Bar Plot')
plt.xticks(rotation=0)
plt.show()
