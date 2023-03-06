'''
Executable data extraction script.

Usage:

python extract.py --fname <abs_path_to_file>
'''

import pandas as pd
import json
import argparse


def T0(shared_df, annotations_df):
    '''
    Extract the required variables for task 0.
    '''
    new_df = pd.concat([shared_df, annotations_df.apply(lambda x: x[0]['value'])],
                       axis=1)
    return new_df.rename(columns={'annotations': "Answer"})

def discnet_t3(shared_df):
    # Create empty array
    df_t3 = np.zeros((len(shared_df),3))
    # Add r, x, y to array, ignore empty lines
    for i in range(len(shared_df)):
        try:
            df_t3[i,0] = shared_df.iloc[i][3]['value'][0]['r']
            df_t3[i,1] = shared_df.iloc[i][3]['value'][0]['x']
            df_t3[i,2] = shared_df.iloc[i][3]['value'][0]['y']
        except:
            pass
    # Mark empty lines as Nan
    df_t3[df_t3 == 0] = np.nan
    # Transfer into Pd dataframe
    d_pre = {'r': df_t3[:,0], 'x': df_t3[:,1],'y': df_t3[:,2]}
    df_t3_pre = pd.DataFrame(data=d_pre)
    return df_t3_pre


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
