import pandas as pd

# Load the CSV file into a DataFrame

# Function to modify the 'created_at' value
def modify_created_at(value):
    if value.startswith("2023-08") or value.startswith("2023-07"):
        return 10
    elif value.startswith("2023-01"):
        return 9
    elif value.startswith("2022-09") or value.startswith("2022-08"):
        return 8
    elif value.startswith("2022-04") or value.startswith("2022-05"):
        return 7
    elif value.startswith("2022-01"):
        return 6
    elif value.startswith("2021-09") or value.startswith("2021-10"):
        return 5
    elif value.startswith("2021-03") or value.startswith("2021-02"):
        return 4
    elif value.startswith("2020-11") or value.startswith("2020-10"):
        return 3
    elif value.startswith("2020-07") or value.startswith("2020-06"):
        return 2
    else:
        return value

def parse_generation(csvFile):
    df = pd.read_csv(csvFile)
    # Apply the function to the 'created_at' column
    df['created_at'] = df['created_at'].apply(modify_created_at)
    # Save the modified DataFrame to a new CSV file
    df.to_csv("generationKey.csv", index=False)
    return "generationKey.csv"

import pandas as pd

# Load the CSV file into a DataFrame

# Function to modify the 'created_at' value
def modify_created_at_paris(value):

    if isinstance(value, str):
        
        if value.startswith("2019-05") or value.startswith("2019-06"):
            return 1
        if value.startswith("2019-07") or value.startswith("2019-08") or value.startswith("2019-09") or value.startswith("2019-11"):
            return 2
        if value.startswith("2020-01") or value.startswith("2020-02") or value.startswith("2020-03"):
            return 3
        if value.startswith("2020-06") or value.startswith("2020-07"):
            return 4
        if value.startswith("2020-08") or value.startswith("2020-09") or value.startswith("2020-10"):
            return 5
        if value.startswith("2021-01") or value.startswith("2021-02") or value.startswith("2021-03"):
            return 6
        if value.startswith("2021-06"): 
            return 7
        if value.startswith("2021-07") or value.startswith("2021-08"):
            return 8
        if value.startswith("2021-09") or value.startswith("2021-10"):
            return 9
        if value.startswith("2021-12") or value.startswith("2022-01") or value.startswith("2022-03"):
            return 10
        if value.startswith("2022-05") or value.startswith("2022-06") or value.startswith("2022-07"):
            return 11
        if value.startswith("2022-08") or value.startswith("2022-09"):
            return 12
        if value.startswith("2023-02"):
            return 13
        if value.startswith("2023-06") or value.startswith("2023-07"):
            return 14
        if value.startswith("2023-08") or value.startswith("2023-09"):
            return 15
        else:
            return -1
    else:
        return -42

def parse_generation_paris(csvFile):
    df = pd.read_csv(csvFile)
    # Apply the function to the 'created_at' column
    df['created_at'] = df['created_at'].apply(modify_created_at_paris)
    # Save the modified DataFrame to a new CSV file
    df.to_csv("generationKey.csv", index=False)
    return "generationKey.csv"