import pandas as pd

# Using Start date and End date
start_date_custom = '2024-01-01'
end_date_custom = '2024-12-31'
date_index_custom = pd.date_range(start=start_date_custom, end=end_date_custom)
print(date_index_custom)

# Using Start date and Periods
start_date_period = '2024-01-01'
periods = 365  # for a full year
date_index_period = pd.date_range(start=start_date_period, periods=periods)
print(date_index_period)

# Using End date and Periods
end_date_period = '2024-12-31'
periods_end = 365  # for a full year
date_index_end_period = pd.date_range(end=end_date_period, periods=periods_end)
print(date_index_end_period)

# Using Frequency
start_date_freq = '2024-01-01'
end_date_freq = '2024-12-31'
date_index_freq = pd.date_range(start=start_date_freq, end=end_date_freq, freq='D')  # 'D'Generates dates on daily basis
print(date_index_freq)
