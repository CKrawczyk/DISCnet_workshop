import unittest
from data_transforms.extract import T3
import pandas as pd
import json

fname = 'data_transforms/tests/many-tools-classifications.csv'
df = pd.read_csv(fname)

# Convert string of list of dicts.
# Is a pandas Series.
annot_df = df['annotations'].apply(json.loads)
shared_df = df[['classification_id', 'user_id', 'subject_ids']]


class TestT3(unittest.TestCase):
    def test_T3(self):
        '''Test if T3 works'''

        new_df = T3(shared_df, annot_df)
        result = [
            new_df['classification_id'][0],
            new_df['user_id'][0],
            new_df['subject_ids'][0],
            new_df['r'][0],
            new_df['x'][0],
            new_df['y'][0],
        ]
        expected = [420702379, 108, 458030, 6.708204, 403.25, 176.966660]

        self.assertEqual(result, expected)
