
import numpy as np


def validation_engine(df):
    '''
    Engine that computes in what metrics a given DataFrame fails

    :param df: pandas DataFrame that needs to be analysed regarding each column
    :param abacus_: dictionary that possesses the columns and whose functions must be applied to them 
    '''

    abacus_ = {}

    for col in list(df.columns):

        metrics_ = []

        if not ('object' in str(df[col].dtype)):

            if np.isnan(df[col].to_list()).any():

                metrics_.append('replace_nan_int')

        else:

            if (np.nan in df[col].to_list()):

                metrics_.append('replace_nan_str')

            if '20MHz' in df[col].to_list():

                metrics_.append('filter_20mhz_frq')

        abacus_[col] = metrics_

    return abacus_