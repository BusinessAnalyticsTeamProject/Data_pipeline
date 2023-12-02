import pandas as pd

# Paths to your CSV files

def merge_csvfile(file_path1, file_path2, mergedfileName, key):
    file1 = file_path1
    file2 = file_path2

    # Read the CSV files into DataFrames
    df1 = pd.read_csv(file_path1)
    df2 = pd.read_csv(file_path2)

    # Merge the DataFrames on the 'login' column
    merged_df = pd.merge(df1, df2, on=key)
    
    
    # Save the merged DataFrame to a new CSV file
    merged_df.to_csv(mergedfileName, index=False)
    
    return mergedfileName


