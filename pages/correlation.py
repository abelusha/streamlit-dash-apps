from ray import method
import streamlit as st
import  pandas as pd
import numpy as np
from .utils_funcs import *
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots


def CorrelationAnalysis():
    df = get_data()
    df = df.drop('Label',axis=1)
    my_form = st.sidebar.form(key='Options')
    my_form.header("Correlation Methods")
    corr_type = my_form.selectbox(label = 'Choose Correlation type', options=['pearson', 'spearman'])
    corr_cols = [None] + df.columns.tolist()
    corr_with  = my_form.selectbox(label = 'Choose Correlation Column', options= corr_cols)
    submitted = my_form.form_submit_button('Submit')
    st.header(f'Show {corr_type.capitalize()} Correlation heatmap!')
    if submitted:
        df_corr = df.corr(method = corr_type)
        fig = get_corr_plot(df_corr, corr_with=corr_with)
        st.plotly_chart(fig)
        st.markdown(download_plotly_fig(fig, f'{corr_type}-correlation_heatmap'), unsafe_allow_html=True)


