import pandas as pd
import numpy as np

# Sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', None],
    'Age': [25, np.nan, 30, 29],
    'City': ['New York', 'Los Angeles', None, 'Chicago']
}
df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

# Identify missing data
print("\nMissing values per column:\n", df.isnull().sum())

# Fill missing numeric values with the mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill missing strings with a placeholder
df['Name'] = df['Name'].fillna("Unknown")
df['City'] = df['City'].fillna("Unknown")

print("\nData after handling missing values:\n", df)
