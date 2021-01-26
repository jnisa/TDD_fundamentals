

import numpy as np
import pandas as pd


class ValidationMetrics:


    def replace_nan_int(df, col):

        '''
        Replace nan values of a given column by the mean value

        :param df: pandas DataFrame
        :param col: float type column that possesses nan values
        '''
        
        df[col] = df[col].fillna(value=round(df[col].mean(skipna=True), 2)).reset_index(drop=True) 

        return df


    def replace_nan_str(df, col):

        '''
        Remove the records that have nan values in the given column

        :param df: pandas DataFrame
        :param col: str type column that possesses nan values
        '''

        return df.drop([i for i, val in enumerate(pd.isnull(df[col]).to_list()) if val == True]).reset_index(drop=True)


    def filter_20mhz_frq(df, col):

        '''
        Remove the input frequency band value from the column provided

        :param df: pandas DataFrame
        :param col: Frequency Band column
        '''

        return df.drop([i for i, val in enumerate(df[col].to_list()) if val == '20MHz']).reset_index(drop=True)
