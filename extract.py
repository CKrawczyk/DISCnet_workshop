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
    new_df = pd.concat(
        [
            shared_df,
            annotations_df.apply(lambda x: x[0]['value'])  # Selects annotaions for T0 only.
        ],
        axis=1
    )
    return new_df.rename(columns={'annotations': "Answer"})


def T2(shared_df, annotations_df):
    '''
    Extract the required variables for task 2.
    '''
    coords = []
    for i in range(0, len(annotations_df)):
        img_coords = []
        for j in range(0, len(annotations_df[i][2]["value"])):
            img_coords.append((annotations_df[i][2]["value"][j]['x'], annotations_df[i][2]["value"][j]['y']))
        coords.append([img_coords])
    new_df = pd.concat([shared_df, pd.DataFrame(coords, columns=["T2coords"])],
                       axis=1)
    return new_df

def T4(shared_df, annotations_df):
    """
    Extract required variables for task 4.
    """
    coords = []
    heights = []
    widths = []
    # dfnew=pd.DataFrame(data=None,columns=['x1','y1','w1','h1','x2','y2','w2','h2'])
    for i in range(len(annotations_df)):
        img_coords = []
        img_heights = []
        img_widths = []
        for j in range(0, len(annotations_df[i][4]["value"])):
            img_coords.append((annotations_df[i][4]["value"][j]['x'], annotations_df[i][4]["value"][j]['y']))
            img_heights.append(annotations_df[i][4]["value"][j]["height"])
            img_widths.append(annotations_df[i][4]["value"][j]["width"])

        coords.append([img_coords])
        heights.append([img_heights])
        widths.append([img_widthsm])

    new_df = pd.concat([shared_df, pd.DataFrame(coords, heights, widths, columns=["coords", "heights", "widths"])],
                       axis=1)
    return new_df


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
func_dict = {
    "T0": T0, 
    "T2": T2, 
    "T4": T4
}
# Loop over functions
for fi in func_dict.keys():
    # Define new array.
    new_df = func_dict[fi](shared_df, annot_df)
    new_df.to_csv(f"{fi}.csv")
