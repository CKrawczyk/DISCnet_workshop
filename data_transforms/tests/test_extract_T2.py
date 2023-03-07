import unittest
import pandas as pd
import json
from data_transforms.extract import T2


class TestExtraxtT2(unittest.TestCase):
     def test_correct_answer(self):
        '''Test run_all give expected value'''

        shared_df_data = {'classification_id' : [0], 'user_id' : [0], 'subject_ids' : [0]}
        shared_df = pd.DataFrame(data = shared_df_data)

        annotated_df_data = {'annotations' : ['[{"task":"T0","task_label":"What is the cat doing?","value":"Playing"},{"task":"T1","value":"hungry","task_label":"How many cats are in the image (use numbers not words)?"},{"task":"T2","task_label":"Locate the eye(s)","value":[{"x":418.25,"y":167.96665954589844,"tool":0,"frame":0,"details":[],"tool_label":"Eye"},{"x":392.25,"y":164.96665954589844,"tool":0,"frame":0,"details":[],"tool_label":"Eye"}]},{"task":"T3","task_label":"Circle the nose","value":[{"r":6.708203932499369,"x":403.25,"y":176.96665954589844,"tool":0,"angle":153.434948822922,"frame":0,"details":[],"tool_label":"Nose"}]},{"task":"T4","task_label":"Draw a box around the ear(s)","value":[{"x":409.25,"y":133.96665954589844,"tool":0,"frame":0,"width":26,"height":20,"details":[],"tool_label":"Ear"},{"x":370.25,"y":123.96665954589844,"tool":0,"frame":0,"width":25,"height":26,"details":[],"tool_label":"Ear"}]}]']}
        annotated_df = pd.DataFrame(data = annotated_df_data)['annotations'].apply(json.loads)

        expected_df_data = {'classification_id' : [0], 'user_id' : [0], 'subject_ids' : [0], 'T2_coords' : [[(418.25, 167.96665954589844), (392.25, 164.96665954589844)]]}
        expected_df = pd.DataFrame(data = expected_df_data)

        result_df=T2(shared_df, annotated_df)

        self.assertTrue(expected_df.equals(result_df))

   