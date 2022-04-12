import streamlit as st

def about():
    text = r'''
    This is a dashboard built to explore and analyze tabular data!.

    It consists the following analysis types:

    * EDA
    * Correlation Analysis

    * PCA (Principal Component Analysis) 

    One can browse to these analysis by selecting in the sidebar for further exploration and analysis.
    
    Happy Data Analysis!!     
    '''
    st.write(text)