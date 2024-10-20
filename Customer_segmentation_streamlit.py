import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Welcome to my First streamlit app ")
st.title("Customer Segmentation Analysis ")

data=r"E:\Nmims notes and lectures\Semester I\R_assignments\pyhton codes\cutomer segmentation files\cleaned_train.csv"
df=pd.read_csv(data)
df.head()

def separate_categorical_numerical(df):

    """
    Separate the categorical and numerical columns of a pandas DataFrame.
    
    Parameters:
    df (pandas.DataFrame): The input DataFrame.
    
    Returns:
    tuple: A tuple containing two pandas DataFrames, one for the categorical columns and one for the numerical columns.
    """
    # Select the columns with data type 'object', which are assumed to be categorical
    categorical_cols = df.select_dtypes(include=['object']).columns
    # Select the columns with data types other than 'object', which are assumed to be numerical
    numerical_cols = df.select_dtypes(exclude=['object']).columns
    # Return two separate DataFrames, one for the categorical columns and one for the numerical columns

    return categorical_cols, numerical_cols

cat_cols, num_cols = separate_categorical_numerical(df.drop("ID", axis=1))
print(cat_cols, num_cols)

seg_col = 'Segmentation'
col_pairs = [(seg_col, col) for col in cat_cols if col != seg_col]
