import pandas as pd

data_new = [10, 20, 30, 40, 50, 60]
index_new = pd.MultiIndex.from_tuples([('A', 1), ('A', 2), ('B', 1), ('B', 2), ('C', 1), ('C', 2)])
series_new = pd.Series(data_new, index=index_new)
print("Series with MultiIndex:")
print(series_new)

subset_A_new = series_new.loc['A']
print("\nSubset A:")
print(subset_A_new)

subset_A_inner_2_new = series_new.loc[('A', 2)]
print("\nSubset A, Inner 2:")
print(subset_A_inner_2_new)

subset_B_new = series_new.loc['B']
print("\nSubset B:")
print(subset_B_new)

subset_C_inner_1_new = series_new.loc[('C', 1)]
print("\nSubset C, Inner 1:")
print(subset_C_inner_1_new)

subset_B_xs_new = series_new.xs('B')
print("\nSubset B using xs:")
print(subset_B_xs_new)

subset_inner_2_new = series_new.xs(2, level=1)
print("\nSubset Inner Level 2 using xs:")
print(subset_inner_2_new)