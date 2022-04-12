from ray import method
import streamlit as st
import  pandas as pd
import numpy as np
from .utils_funcs import *
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

def PCAAnalysis():
    df = get_data()
    df = df.drop('Label',axis=1)
    n = df.shape[1]
    my_form = st.sidebar.form(key='Options')
    my_form.header("Choose # of PC components")
    n_components = my_form.slider('Choose Number of PCA components', 0,n,2,1)
    submitted = my_form.form_submit_button('Submit')
    if submitted:    
        explained_variance, df_byvar = get_pca_report(df,n_components)

        col1, col2 = st.columns(2)
        with col1: 
            st.header('Variance Explained per PC component')
            x = [f'PC_{i+1}' for i in range(n_components)]
            y = explained_variance * 100
            y_cumsum = np.cumsum(y)
            fig_bar = make_subplots(specs=[[{"secondary_y": True}]])
            fig_bar = fig_bar.add_trace(go.Bar(x=x, y = y,showlegend=False), secondary_y=False)
            fig_bar = fig_bar.add_trace(go.Scatter(x=x, y = y_cumsum, mode='markers+lines', showlegend=False), secondary_y=True)

            fig_bar.update_xaxes(title = '<b> PC Components')
            fig_bar.update_yaxes(title = '<b> Individual Variance Explained (%)')
            fig_bar.update_yaxes(title = '<b> Cumulative Explained Variance (%)', secondary_y=True)
            st.plotly_chart(fig_bar)
            st.markdown(download_plotly_fig(fig_bar, 'pca_heatmap'), unsafe_allow_html=True)
        with col2:
            st.header('Feature Importance')
            fig = get_corr_plot(df_byvar, None)
            fig.update_xaxes(tickangle=0)
            fig.update_layout(title_text=f'<b>Feature Importance')
            st.plotly_chart(fig)
            st.markdown(download_plotly_fig(fig, 'pca_heatmap'), unsafe_allow_html=True)


        


