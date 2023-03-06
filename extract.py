import pandas as pd
import json
import argparse

def T0(shared_df, annotations_df):
    '''
    Extract the required variables for task 0.
    '''
    new_df = pd.concat([shared_df, annotations_df.apply(lambda x: x[0]['value'])],
                       axis=1)
    return new_df.rename(columns={'annotations':"Answer"})

# Parse file name for script.
parser = argparse.ArgumentParser()
parser.add_argument('--fname', help='Path to file.', required=True)
args = parser.parse_args()

# Load origonal file.
df = pd.read_csv(args.fname)

# Convert string of list of dicts.
# Is a pandas Series.
annot_df = df['annotations'].apply(json.loads)
shared_df = df[['classification_id', 'user_id', 'subject_ids']]

# Define dictionary of functions to apply.
func_dict = {"T0": T0}

# Loop over functions
for fi in func_dict.keys():
    # Define new array.
    new_df = func_dict[fi](shared_df, annot_df)
    new_df.to_csv(f"{fi}.csv")

