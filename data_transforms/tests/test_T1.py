import unittest
from data_transforms.extract import T1
import pandas as pd
import numpy as np


class TestExtractT1(unittest.TestCase):
    def test_extract_t1(self):
        df_in_shared = pd.DataFrame([["id1_1", "id1_2", "id1_3"], ["id2_1", "id2_2", "id2_3"]], columns = ["id1", "id2", "id3"])
        df_in_annotated = pd.DataFrame([[[{}, {"value":2}]], [[{}, {"value":"hungry"}]]], columns = "annotations")

        df_expected = pd.concat(
            [
                df_in_shared,
                pd.DataFrame([[2], [np.nan]], columns = "number of cats")
            ],
            axis=1
        )

        df_out = T1(df_in_shared, df_in_annotated)

        pd.testing.assert_frame_equal(df_out, df_expected)