'''
Does stuff.

Usage:

python extract.py --fname <abs_path_to_file>
'''

import pandas as pd
import json
import argparse
import numpy as np


def T0(shared_df, annotations_df):
    '''
    Extract answer to the question "What is the cat doing?" for task 0.

    Args:
        shared_df (pandas.Dataframe): ``pandas.Dataframe`` that contains quantities that will
         be shared across all ``.csv`` files.
        annotations_df (pandas.Dataframe): ``ps.Series`` with ``annotations for
         each classification.

    Returns:
        new_df (pandas.Dataframe):  ``pandas.Dataframe`` with ``shared_df``
         quantities and answer to "What is the cat doing?".
    '''
    new_df = pd.concat(
        [
            shared_df,
            annotations_df.apply(lambda x: x[0]['value'])  # Selects annotaions for T0 only.
        ],
        axis=1
    )
    return new_df.rename(columns={'annotations': "Answer"})


def T1(shared_df, annotations_df):
    '''
    Extract answer to the question "How many cats are in the image?" for task 1.
     Args:
         shared_df (pandas.Dataframe): ``pandas.Dataframe`` that contains quantities that will
          be shared across all ``.csv`` files.
         annotations_df (pandas.Dataframe): ``ps.Series`` with ``annotations`` for
          each classification.
     Returns:
         new_df (pandas.Dataframe):  ``pandas.Dataframe`` with ``shared_df``
          quantities and answer to "How many cats are in the image?".
          Answers which cannot be converted to integers are stored as numpy nan values instead.
    '''

    def is_number(x):
        try:
            return int(x)
        except ValueError:
            return np.nan

    new_df = pd.concat(
        [
            shared_df,
            annotations_df.apply(lambda x: is_number(x[1]['value']))  # Selects annotations for T1 only.
        ],
        axis=1
    )
    return new_df.rename(columns={'annotations': "Number of cats"})


def T2(shared_df, annotations_df):
    '''
    Extract the required variables for task 2. i.e the x and y coordinates of the eye locations.
    Parameters
    ----------
    shared_df :  DataFrame
        DataFrame containing only 'classification_id', 'user_id', and 'subject_ids'.
    annotations_df : DataFrame
        DataFrame containing relevent data.

    Returns
    -------
    DataFrame
        DataFrame containing the 'classification_id', 'user_id', and 'subject_ids' and lists of tuples of
        x and y coordinates of the eye locations.

    '''
    coords = []
    for i in range(0, len(annotations_df)):
        img_coords = []
        for j in range(0, len(annotations_df[i][2]["value"])):
            # Extracts the x and y coordinates from the data frame.
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
        widths.append([img_widths])

    new_df = pd.concat([shared_df, pd.DataFrame(coords, heights, widths, columns=["coords", "heights", "widths"])],


def T3(shared_df, annotations_df):

    '''
    Extract the required variables for task 3. i.e the radius of the nose x and y coordinates of the nose.
    Parameters
    ----------
    shared_df :  DataFrame
        DataFrame containing only 'classification_id', 'user_id', and 'subject_ids'.
    annotations_df : DataFrame
        DataFrame containing relevent data.
    Returns
    -------
    DataFrame
        DataFrame containing the 'classification_id', 'user_id', and 'subject_ids' and radius, x, y coordinates
        of nose.
    '''
    # Create empty array
    df_t3 = np.zeros((len(shared_df), 3))
    # Add r, x, y to array, ignore empty lines
    for i in range(len(shared_df)):
        try:
            df_t3[i, 0] = shared_df.iloc[i][3]['value'][0]['r']
            df_t3[i, 1] = shared_df.iloc[i][3]['value'][0]['x']
            df_t3[i, 2] = shared_df.iloc[i][3]['value'][0]['y']
        except Exception:
            pass
    # Mark empty lines as Nan
    df_t3[df_t3 == 0] = np.nan
    # Transfer into Pd dataframe
    d_pre = {'r': df_t3[:, 0], 'x': df_t3[:, 1], 'y': df_t3[:, 2]}
    df_t3_pre = pd.DataFrame(data=d_pre)

    new_df = pd.concat([shared_df, df_t3_pre],
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
    "T4": T4,
    "T3": T3,
}

# Loop over functions
for fi in func_dict.keys():
    # Define new array.
    new_df = func_dict[fi](shared_df, annot_df)
    new_df.to_csv(f"{fi}.csv")
