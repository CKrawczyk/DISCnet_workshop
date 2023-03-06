import pandas as pd
import json
import argparse

def T0(row):
    '''
    Extract the required variables for task 0.
    '''
    return row[0]['value']

# Parse file name for script.
parser = argparse.ArgumentParser()
parser.add_argument('--fname', help='Path to file.', required=True)
args = parser.parse_args()

# Load origonal file.
df = pd.read_csv(args.fname)

# Convert string of list of dicts.
# Is a pandas Series.
annot_df = df['annotations'].apply(json.loads)

# Define dictionary of functions to apply.
func_dict = {"T0": T0}

# Loop over functions
for fi in func_dict.keys():
    # Define new array.
    new_df = pd.concat([df[['classification_id', 'user_name']],
                        annot_df.apply(func_dict[fi])],
                       axis=1)
    new_df.to_csv(f"{fi}.csv")

