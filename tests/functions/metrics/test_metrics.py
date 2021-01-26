

import os
import sys
import unittest
import numpy as np
import pandas as pd
import pandas.testing as pd_testing


base_path_ = sys.path.append(os.path.join('C://', 'Users', 'jnisa', 'Desktop', 'A&C-Training', 'training', 'app', 'functions', 'metrics'))


from metrics import ValidationMetrics as vm


class TestMetricsApplication(unittest.TestCase):


    # replace_nan_int tests

    def test_replace_nan_int_basic(self):
        
        data_ = [
            ['col1', 'col2', 'col3'],
            [23,     np.nan, 'John'],
            [1,      3,      'Bert'],
            [14,     2,      'Sophia'],
            [42,     1,      'Hannah']
        ]
        
        headers_ = data_.pop(0)

        data_expected_ = [
            ['col1', 'col2', 'col3'],
            [23,     2.0,    'John'],
            [1,      3.0,    'Bert'],
            [14,     2.0,    'Sophia'],
            [42,     1.0,    'Hannah']
        ]

        headers_expected_ = data_expected_.pop(0)

        df_expected_ = pd.DataFrame(data_expected_, columns=headers_expected_).reset_index(drop=True)

        df_result_ = getattr(vm, 'replace_nan_int')(pd.DataFrame(data_, columns=headers_), 'col2')

        pd_testing.assert_frame_equal(df_expected_, df_result_)


    def test_replace_nan_int_simple(self):
        
        data_ = [
            ['col1', 'col2', 'col3'],
            [23,     np.nan, 'John'],
            [1,      27.123, 'Bert'],
            [14,     np.nan, 'Sophia'],
            [42,     23.345, 'Hannah']
        ]
        
        headers_ = data_.pop(0)

        data_expected_ = [
            ['col1', 'col2', 'col3'],
            [23,     25.23,  'John'],
            [1,      27.123, 'Bert'],
            [14,     25.23,  'Sophia'],
            [42,     23.345, 'Hannah']
        ]

        headers_expected_ = data_expected_.pop(0)

        df_expected_ = pd.DataFrame(data_expected_, columns=headers_expected_).reset_index(drop=True)

        df_result_ = getattr(vm, 'replace_nan_int')(pd.DataFrame(data_, columns=headers_), 'col2')

        pd_testing.assert_frame_equal(df_expected_, df_result_)


    def test_replace_nan_int_complex(self):
        
        data_ = [
            ['col1', 'col2',    'col3'],
            [23,     np.nan,    'John'],
            [1,      np.nan,    'Bert'],
            [14,     np.nan,    'Sophia'],
            [42,     np.nan,    'Hannah']
        ]
        
        headers_ = data_.pop(0)

        data_expected_ = [
            ['col1', 'col2',    'col3'],
            [23,     np.nan,    'John'],
            [1,      np.nan,    'Bert'],
            [14,     np.nan,    'Sophia'],
            [42,     np.nan,    'Hannah']
        ]

        headers_expected_ = data_expected_.pop(0)

        df_expected_ = pd.DataFrame(data_expected_, columns=headers_expected_).reset_index(drop=True)

        df_result_ = getattr(vm, 'replace_nan_int')(pd.DataFrame(data_, columns=headers_), 'col2')

        pd_testing.assert_frame_equal(df_expected_, df_result_)


    # replace_nan_str tests

    def test_replace_nan_str_basic(self):
        
        data_ = [
            ['col1', 'col2', 'col3'],
            [23,     0.5,    'John'],
            [1,      3.0,    'Bert'],
            [14,     2.0,    'Sophia'],
            [42,     1.0,    np.nan]
        ]
        
        headers_ = data_.pop(0)

        data_expected_ = [
            ['col1', 'col2', 'col3'],
            [23,     0.5,    'John'],
            [1,      3.0,    'Bert'],
            [14,     2.0,    'Sophia']
        ]
        headers_expected_ = data_expected_.pop(0)

        df_expected_ = pd.DataFrame(data_expected_, columns=headers_expected_).reset_index(drop=True)

        df_result_ = getattr(vm, 'replace_nan_str')(pd.DataFrame(data_, columns=headers_), 'col3')

        pd_testing.assert_frame_equal(df_expected_, df_result_)


    def test_replace_nan_str_simple(self):
        
        data_ = [
            ['col1', 'col2', 'col3'],
            [23,     0.5,    'John'],
            [1,      3.0,    np.nan],
            [14,     2.0,    np.nan],
            [42,     1.0,    'Hannah']
        ]
        
        headers_ = data_.pop(0)

        data_expected_ = [
            ['col1', 'col2', 'col3'],
            [23,     0.5,    'John'],
            [42,     1.0,    'Hannah']
        ]
        headers_expected_ = data_expected_.pop(0)

        df_expected_ = pd.DataFrame(data_expected_, columns=headers_expected_).reset_index(drop=True)

        df_result_ = getattr(vm, 'replace_nan_str')(pd.DataFrame(data_, columns=headers_), 'col3')

        pd_testing.assert_frame_equal(df_expected_, df_result_)

    
    def test_replace_nan_str_complex(self):
        
        data_ = [
            ['col1', 'col2', 'col3'],
            [23,     0.5,    np.nan],
            [1,      3.0,    np.nan],
            [14,     2.0,    np.nan],
            [42,     1.0,    np.nan]
        ]
        
        headers_ = data_.pop(0)

        data_expected_ = [
            ['col1', 'col2', 'col3'],
        ]
        headers_expected_ = data_expected_.pop(0)

        df_expected_ = pd.DataFrame(data_expected_, columns=headers_expected_).reset_index(drop=True)

        df_result_ = getattr(vm, 'replace_nan_str')(pd.DataFrame(data_, columns=headers_), 'col3')

        pd_testing.assert_frame_equal(df_expected_, df_result_, check_dtype=False)


    # filter_freqs tests

    def test_select_freqs_simple(self):

        data_ = [
            ['col1', 'col2',    'col3'],
            [23,     '20MHz',   'John'],
            [1,      '20MHz',   'Bert'],
            [14,     '10MHz',   'Sophia'],
            [42,     '5MHz',    'Hannah']
        ]
        
        headers_ = data_.pop(0)

        data_expected_ = [
            ['col1', 'col2',    'col3'],
            [14,     '10MHz',   'Sophia'],
            [42,     '5MHz',    'Hannah']
        ]

        headers_expected_ = data_expected_.pop(0)

        df_expected_ = pd.DataFrame(data_expected_, columns=headers_expected_).reset_index(drop=True)

        df_result_ = getattr(vm, 'filter_20mhz_frq')(pd.DataFrame(data_, columns=headers_), 'col2')

        pd_testing.assert_frame_equal(df_expected_, df_result_)


    def test_select_freqs_complex(self):

        data_ = [
            ['col1', 'col2',    'col3'],
            [23,     '20MHz',   'John'],
            [1,      '20MHz',   'Bert'],
            [14,     '20MHz',   'Sophia'],
            [42,     '20MHz',   'Hannah']
        ]
        
        headers_ = data_.pop(0)

        data_expected_ = [
            ['col1', 'col2',    'col3'],
        ]

        headers_expected_ = data_expected_.pop(0)

        df_expected_ = pd.DataFrame(data_expected_, columns=headers_expected_).reset_index(drop=True)

        df_result_ = getattr(vm, 'filter_20mhz_frq')(pd.DataFrame(data_, columns=headers_), 'col2')

        pd_testing.assert_frame_equal(df_expected_, df_result_, check_dtype=False)
