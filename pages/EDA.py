from ray import method
import streamlit as st
import  pandas as pd
import numpy as np
from .utils_funcs import *
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

def EDAAnalysis():
    df = get_data()
    df['Label'] = df['Label'].astype('category')
    st.sidebar.header('Select Analysis Type')
    analysis_type = st.sidebar.selectbox('',
                                     ['Univariate Analysis',
                                      'Bivariate Analysis', 
                                      ]
                                     )
    if analysis_type == 'Univariate Analysis':
        my_form = st.sidebar.form(key='Options')
        my_form.header("Select Visual Type")
        varibale      = my_form.selectbox(label = "", options= df.columns.tolist())  
        visulual_type = my_form.selectbox(label = "", options= ['line','histogram','box'])
        submitted     = my_form.form_submit_button('Submit')
        if submitted:
            if visulual_type == 'line':
                fig = px.line(df, y = varibale,color='Label', title=f'Line plot of {varibale}')
                st.plotly_chart(fig)
            if visulual_type == 'histogram':
                fig = px.histogram(df, x = varibale, color='Label',title=f'Distribuion plot of {varibale}')
                st.plotly_chart(fig)
            if visulual_type == 'box':
                fig = px.box(df, y = varibale,color='Label', title=f'Box plot of {varibale}')
                st.plotly_chart(fig)
    elif analysis_type == 'Bivariate Analysis':

        my_form = st.sidebar.form(key='Options')
        my_form.header("Select Visual Type")
        varibales      = my_form.multiselect(label = "", options= df.columns.tolist())  
        visulual_type = my_form.selectbox(label = "", options= ['scatter','histogram','box'])
        submitted     = my_form.form_submit_button('Submit')
        if submitted:
            if visulual_type == 'scatter':
                fig = px.scatter(df, x = varibales[0], y = varibales[-1],
                color='Label',
                title=f'Scatter plot of {varibales[0]}-vs-{varibales[-1]}'
                )
                st.plotly_chart(fig)
