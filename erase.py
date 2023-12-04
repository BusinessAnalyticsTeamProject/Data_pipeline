import pandas as pd

# Load the CSV file into a DataFrame
# df = pd.read_csv('final.csv')

# # Remove rows where 'created_at' is -1
# df_filtered = df[df['created_at'] != -1]

# # Save the filtered DataFrame back to a CSV file
# df_filtered.to_csv('filtered_file.csv', index=False)

# input_file = 'feed.csv'
# output_file = 'user_feedback_data_campus_1.csv'

# with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
#     for line in infile:
#         # Remove the trailing comma if it exists
#         line = line.rstrip(',\n') + '\n'
#         outfile.write(line)

df = pd.read_csv('filtered_file.csv', header=None)  # Adjust the file path

# Remove duplicate rows
df_cleaned = df.drop_duplicates()

# Save the cleaned DataFrame back to a CSV file
df_cleaned.to_csv('Final.csv', index=False, header=False)