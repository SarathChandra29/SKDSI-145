import pandas as pd
import numpy as np

date_range_custom = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
data_values = np.random.randn(len(date_range_custom))

# Create a time series DataFrame
time_series_data = pd.DataFrame(data_values, index=date_range_custom, columns=['Value'])

# Display the first few rows of the DataFrame
print(time_series_data.head())
