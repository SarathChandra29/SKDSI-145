import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)
data_dict = {
    'Group': np.random.choice(['A', 'B', 'C', 'D', 'E'], 100),
    'Measure': np.random.randn(100)
}
df_boxplot = pd.DataFrame(data_dict)

# Create a box plot
plt.figure(figsize=(12, 6))
sns.boxplot(x='Group', y='Measure', data=df_boxplot)
plt.xlabel('Group')
plt.ylabel('Measure')
plt.title('Box Plot of Measure by Group')
plt.grid(True)
plt.show()
