import unittest
from data_transforms.extract import T4
import json
import pandas as pd


class TestT4(unittest.TestCase):
    def test_first(self):
        '''Test T4'''
        df = pd.read_csv("many-tools-classifications.csv")
        a = df[['classification_id', 'user_id', 'subject_ids']]
        b = df['annotations'].apply(json.loads)

        expected = [(409.25, 133.96665954589844), (370.25, 123.96665954589844)]

        result = T4(a, b)
        result = result["coords"].iloc[0]

        self.assertEqual(result, expected)

    def test_last(self):
        '''Test T4'''
        df = pd.read_csv("many-tools-classifications.csv")
        a = df[['classification_id', 'user_id', 'subject_ids']]
        b = df['annotations'].apply(json.loads)

        expected = [(300.25, 97.96665954589844), (406.25, 74.96665954589844)]

        result = T4(a, b)
        result = result["coords"].iloc[13]

        self.assertEqual(result, expected)
