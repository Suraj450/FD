import pandas as pd
import numpy as np

df1=pd.read_csv('data.csv', nrows=10)
df1=df1.drop(['isFlaggedFraud','step'], axis=1)
arr=df1.to_numpy()
arr

col2=df1['nameOrig'].to_numpy()
col2
def my_function():
    return arr

def my_function2():
    return col2

