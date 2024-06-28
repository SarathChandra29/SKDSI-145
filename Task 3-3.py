import pandas as pd

# Generating date range with UTC timezone
start_date_custom = '2024-01-01'
end_date_custom = '2024-01-05'
date_index_utc = pd.date_range(start=start_date_custom, end=end_date_custom, freq='D', tz='UTC')
print(date_index_utc)

# Localizing timezone to America/New_York
date_index_localized = pd.date_range(start=start_date_custom, end=end_date_custom, freq='D')
date_index_localized = date_index_localized.tz_localize('America/New_York')
print(date_index_localized)

# Converting timezone to Europe/London
date_index_converted = date_index_localized.tz_convert('Europe/London')
print(date_index_converted)

# Combining two different timezones
date_index1_utc = pd.date_range(start=start_date_custom, periods=3, freq='D', tz='UTC')
date_index2_ny = pd.date_range(start=start_date_custom, periods=3, freq='D', tz='America/New_York')
combined_index = date_index1_utc.union(date_index2_ny)
print(combined_index)
