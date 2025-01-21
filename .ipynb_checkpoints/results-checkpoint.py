import sys
print(sys.executable)
print(sys.version)

import pandas as pd

# Read the CSV file into a DataFrame (replace 'your_file.csv' with the actual file path)
df = pd.read_csv('results.csv')

# Display the first few rows to understand the data structure
print("Original DataFrame:")
print(df.head())

# Select the columns in the desired order
selected_columns = [
    'Date', 'UTS', 'YS', 'EL', 'Unit Weight', 'Transvers Height', 
    'Longitudinal Hight', 'Rib spacing', 'Length'
]

# Create a new DataFrame with the selected columns
new_table = df[selected_columns]

# Display the new table
print("\nNew Table with Selected Columns:")
print(new_table)
