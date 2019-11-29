#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 17:12:05 2019

@author: martoso
"""

import pandas as pd

df = pd.read_csv('/home/martoso/Desktop/Git/data_science/Decision_Tree/census.csv')


def check_missing_data(df):
    columns = df.columns
    for i in columns:
       print('Column: {} has {} NaN value'.format(i, pd.isna(df[i]).sum(axis = 0)))
    return ''

check_missing_data(df)