

import os
import sys
import unittest
import numpy as np
import pandas as pd
import pandas.testing as pd_testing


base_path_ = sys.path.append(os.path.join('C://', 'Users', 'jnisa', 'Desktop', 'A&C-Training', 'training', 'app', 'functions', 'enrichment'))


from enrichment import enrichment


class TestDataEnrichment(unittest.TestCase):


    def test_enrichment_simple(self):
        
        data_ = [
            ['col1', 'col2', 'col3',      'col4'],
            [23,     np.nan, 'John',      '20MHz'],
            [np.nan, 3.0,    'Kirill',    '15MHz'],
            [14,     np.nan, 'Sophia',    '20MHz'],
            [42,     1.0,    'Bert',      '10MHz']
        ]

        headers_ = data_.pop(0)

        data_expected_ = [
            ['col1', 'col2', 'col3',    'col4'],
            [26.33,  3.0,    'Kirill',  '15MHz'],
            [42,     1.0,    'Bert',    '10MHz'],
        ]

        headers_expected_ = data_expected_.pop(0)

        df_expected_ = pd.DataFrame(data_expected_, columns=headers_expected_).reset_index(drop=True)

        df_result_ = enrichment(pd.DataFrame(data_, columns=headers_).reset_index(drop=True))

        pd_testing.assert_frame_equal(df_expected_, df_result_)


    def test_enrichment_complex(self):
        
        data_ = [
            ['col1', 'col2', 'col3',    'col4'],
            [23,     np.nan, 'John',    '20MHz'],
            [1,      3.0,     np.nan,   '15MHz'],
            [14,     2.0,    'Sophia',  '20MHz'],
            [42,     1.0,    'Bert',    '20MHz']
        ]

        headers_ = data_.pop(0)

        data_expected_ = [
            ['col1', 'col2', 'col3',    'col4'],
        ]

        headers_expected_ = data_expected_.pop(0)

        df_expected_ = pd.DataFrame(data_expected_, columns=headers_expected_).reset_index(drop=True)

        df_result_ = enrichment(pd.DataFrame(data_, columns=headers_).reset_index(drop=True))

        pd_testing.assert_frame_equal(df_expected_, df_result_, check_dtype=False)
