
Extraction of specified columns

# Replace 'your_file.csv' with the actual path to your CSV file


import pandas as pd
import os

# Read the CSV file into a DataFrame
df = pd.read_csv('gastresult_without_nan.csv')

# Extract rows with adjusted p-values less than 0.05
positive_logFC_df = df[df['adj.P.Val'] < 0.05]

# Extract specific columns for the positive logFC rows
selected_columns_df = positive_logFC_df[['ID', 'adj.P.Val', 'P.Value', 't', 'B', 'logFC', 'Gene.symbol', 'Gene.title']]

# Display the DataFrame with selected columns
print(selected_columns_df)

# Check if the DataFrame is empty
if selected_columns_df.empty:
    print("The DataFrame is empty. No data to save.")
else:
    try:
        # Save the selected columns DataFrame to a CSV file
        selected_columns_df.to_csv("file.csv", index=False)
        print("File saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

# Confirm the working directory
print("Current working directory:", os.getcwd())
# cleaning of the file
import pandas as pd

# Load the data file
df3 = pd.read_csv('gastnewdown.csv')

print(df3)

# Remove rows where the 'Description' column starts with 'uncharacterised' or 'uncharacterized'
df3_cleaned = df3[~df3['Description'].str.contains(r'^\s*uncharacteri[sz]ed', case=False, na=False)]

# Save the cleaned DataFrame to a new CSV file
df3_cleaned.to_csv('gastnewdown_cleaned.csv', index=False)

print(df3_cleaned.head())

# Remove duplicate rows based on 'Gene.symbol'
data_no_duplicates = df3.drop_duplicates(subset='Gene.title', keep='first')

# # # Save the DataFrame without duplicates back to the original file
data_no_duplicates.to_csv('gastnewk_withoutdup.csv', index=True)

