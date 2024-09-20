import numpy as np
import pandas as pd
import glob
import os
import openpyxl

# Assigning the path to the folder variable
folder = r'insert folder path'

# Getting the list of CSV files from the assigned path
csv_files = glob.glob(os.path.join(folder, '*.csv'))

list_of_dfs = []
for file in csv_files:
    try:
        # Read the CSV file
        df = pd.read_csv(file)
        
        # Check if the required columns exist
        required_columns = ['Wavenumber', 'Depth', 'Prominence', 'Width']
        if all(col in df.columns for col in required_columns):
            # Add the filename to the dataframe, but only for the first row
            df.loc[0, 'filename'] = os.path.basename(file).split('.')[0]
            df['filename'] = df['filename'].fillna('')
            
            # Move the filename column to the first position
            cols = list(df.columns)
            cols.insert(0, cols.pop(cols.index('filename')))
            df = df.reindex(columns=cols)
            
            # Append the dataframe to the list
            list_of_dfs.append(df)
        else:
            print(f"Skipping file {file} as it does not contain all required columns.")
    except pd.errors.EmptyDataError:
        print(f"Skipping file {file} as it is empty.")
    except pd.errors.ParserError:
        print(f"Skipping file {file} as it is not a valid CSV file.")

# Concatenate the dataframes
if list_of_dfs:
    combined_df = pd.concat(list_of_dfs, ignore_index=True)
    
    # Check if the output file already exists
    output_file = os.path.join(folder, 'combined_data.xlsx')
    if os.path.exists(output_file):
        # If the file exists, read the existing data and append to it
        existing_df = pd.read_excel(output_file)
        combined_df = pd.concat([existing_df, combined_df], ignore_index=True)
    
    # Write the combined dataframe to an Excel file
    combined_df.to_excel(output_file, index=False)
    print(f"Data written to {output_file}")
else:
    print("No valid CSV files found.")
