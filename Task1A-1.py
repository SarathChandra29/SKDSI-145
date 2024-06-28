import pandas as pd
import numpy as np

data_new = {
    'X': [1, 2, np.nan, 4, 5, np.nan, 7],
    'Y': [np.nan, 2, 3, 4, np.nan, 6, 7],
    'Z': ['foo', 'bar', 'baz', np.nan, 'qux', 'quux', 'corge'],
    'W': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
}

df_new = pd.DataFrame(data_new)
print("Original DataFrame:")
print(df_new)

missing_data_new = df_new.isna()
print("\nMissing Data in DataFrame:")
print(missing_data_new)

df_dropna_rows_new = df_new.dropna()
print("\nDataFrame after dropping rows with any missing data:")
print(df_dropna_rows_new)

df_dropna_cols_new = df_new.dropna(axis=1)
print("\nDataFrame after dropping columns with any missing data:")
print(df_dropna_cols_new)

df_fillna_new = df_new.fillna(value={'X': df_new['X'].mean(), 'Y': df_new['Y'].mean(), 'Z': 'missing', 'W': 0})
print("\nDataFrame after filling missing data:")
print(df_fillna_new)

df_with_duplicates_new = df_new.append(df_new.iloc[2], ignore_index=True)
print("\nDataFrame with Duplicates:")
print(df_with_duplicates_new)

duplicates_new = df_with_duplicates_new.duplicated()
print("\nDuplicates in DataFrame:")
print(duplicates_new)

df_no_duplicates_new = df_with_duplicates_new.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(df_no_duplicates_new)