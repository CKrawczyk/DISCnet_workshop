import unittest
from data_transforms.extract import T0
import pandas as pd
import json


class TestT0(unittest.TestCase):

    test_df = pd.read_csv("many-tools-classifications.csv")
    test_annot = test_df['annotations'].apply(json.loads)
    test_shared = test_df[[
        'classification_id',
        'user_id',
        'subject_ids'
        ]]

    def test_shared_df(self):
        '''
        Test that the shared data is unchanged.
        '''
        new_df = T0(
            self.test_shared,
            self.test_annot
            )
        self.assertTrue(
            self.test_shared.equals(new_df[[
                'classification_id',
                'user_id',
                'subject_ids'
                ]]))

    def test_answer_extraction(self):
        '''
        Test that the answer is extracted from the annotations string correctly.
        '''
        new_df = T0(
            self.test_shared,
            self.test_annot
            )
        self.assertEqual(new_df['Answer'].iloc[0], "Playing")
        self.assertEqual(new_df['Answer'].iloc[-2], "Other")
