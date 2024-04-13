import pandas as pd
import glob

def combine_csvs_in_folder(folder_path, output_file):
    # Generate a file pattern for matching CSV files
    file_pattern = f"{folder_path}/*.csv"
    
    # Use glob to find all files matching the pattern
    file_list = glob.glob(file_pattern)
    
    # Initialize an empty list to store dataframes
    dfs = []
    
    # Loop through the list of file paths
    for file in file_list:
        # Read the current CSV file into a dataframe and append it to the list
        dfs.append(pd.read_csv(file))
    
    # Concatenate all dataframes in the list
    combined_df = pd.concat(dfs, ignore_index=True)
    
    # Write the combined dataframe to a new CSV file
    combined_df.to_csv(output_file, index=False)
    print(f"Combined CSV saved as: {output_file}")

# Example usage
folder_path = 'combine-these-csvs'  # Specify the folder containing CSV files
output_path = 'combined.csv'  # Define the output file path
combine_csvs_in_folder(folder_path, output_path)
