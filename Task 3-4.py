import pandas as pd

current_period = pd.Period('2024-01', freq='M')
future_period_custom = current_period + 3
print("Future Period:", future_period_custom)
past_period_custom = current_period - 2
print("Past Period:", past_period_custom)

# Constructing range of periods
periods_range_custom = pd.period_range(start='2024-01', end='2024-12', freq='M')
print("Periods Range:", periods_range_custom)
