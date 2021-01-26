

import sys
import numpy as np


sys.path.append('C://Users/jnisa/Desktop/A&C-Training/training/app/functions/engine/')
from engine import validation_engine


sys.path.append('C://Users/jnisa/Desktop/A&C-Training/training/app/functions/metrics/')
from metrics import ValidationMetrics


def enrichment(df):
    '''
    Enrichment of the dataset according with the validation pipeline established

    :param df: pandas DataFrame that needs to be analysed and enriched 
    '''

    action_points_ = validation_engine(df)

    for key in action_points_.keys():

        for function in action_points_[key]:

            df = getattr(ValidationMetrics, function)(df, key)

    return df