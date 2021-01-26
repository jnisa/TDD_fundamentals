

import os
import sys
import unittest
import numpy as np
import pandas as pd
import pandas.testing as pd_testing


base_path_ = sys.path.append(os.path.join('C://', 'Users', 'jnisa', 'Desktop', 'A&C-Training', 'training', 'app', 'functions', 'engine'))


from engine import validation_engine


class TestValidationEngine(unittest.TestCase):

    def test_validation_engine_simple(self):

        data_ = [
            ['col1', 'col2', 'col3',    'col4'],
            [23,     np.nan, 'John',    '20MHz'],
            [1,      3.0,     np.nan,   '15MHz'],
            [14,     2.0,    'Sophia',  '20MHz'],
            [42,     1.0,    'Hannah',  '5MHz']
        ]
        
        headers_ = data_.pop(0)

        expected_ = {
            'col1': [],
            'col2': ['replace_nan_int'],
            'col3': ['replace_nan_str'],
            'col4': ['filter_20mhz_frq']
        }

        result_ = validation_engine(pd.DataFrame(data_, columns=headers_).reset_index(drop=True))

        self.assertEqual(expected_, result_)


    def test_validation_engine_complex(self):

        data_ = [
            ['col1',    'col2',     'col3',    'col4'],
            [np.nan,    np.nan,     '20MHz',   '10MHz'],
            [1,         3.0,        np.nan,    '15MHz'],
            [123,       2.0,        'Sophia',  np.nan],
            [42,        '20MHz',    'Hannah',  '5MHz']
        ]
        
        headers_ = data_.pop(0)

        expected_ = {
            'col1': ['replace_nan_int'],
            'col2': ['replace_nan_str', 'filter_20mhz_frq'],
            'col3': ['replace_nan_str', 'filter_20mhz_frq'],
            'col4': ['replace_nan_str']
        }

        result_ = validation_engine(pd.DataFrame(data_, columns=headers_).reset_index(drop=True))

        self.assertEqual(expected_, result_)
