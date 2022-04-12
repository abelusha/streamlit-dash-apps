import pandas as pd
import numpy as np
from io import StringIO, BytesIO
import base64
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

@st.cache(allow_output_mutation=True)
def get_data():
    url = 'https://raw.githubusercontent.com/abelusha/AutoEncoders-for-Anomaly-Detection/master/JADS_CarrerDay_Data.cvs'
    df = pd.read_csv(url, index_col=0)
    return df

# @st.cache(allow_output_mutation=True)
# def get_plot_type(df, plot_type):
#     if plot


@st.cache(allow_output_mutation=True)
def get_corr_plot(dff_corr, corr_with):
    dff_corr = dff_corr.round(3)
    if corr_with is not None:
        x = [corr_with]
        y = list(dff_corr.index)
        z = dff_corr[[corr_with]].values
        height = 800
        width  = 750
        tickangle = None
        text = f'<b>{corr_with} correlations'
    else:
        x = list(dff_corr.columns)
        y = list(dff_corr.index)
        z = dff_corr.values
        height = 800
        width  = 800
        tickangle = -90
        text = f'<b>Correlation Matrix'

    z_text = np.around(z, decimals=2)
    fig = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=z_text, colorscale='aggrnyl', showscale = True)
    fig.update_layout(title={
        'text': text,
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        height=height,
        width=width
    )
    fig.update_xaxes(side="bottom", tickangle=tickangle,tickfont_size=16)
    fig.update_yaxes(tickfont_size=16)
    return fig


## PCA util func

def get_pca_report(df, n_components):
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import RobustScaler, StandardScaler

    std_scaler = StandardScaler()
    pca = PCA(n_components=n_components)

    X = df.copy()
    X_scaled = std_scaler.fit_transform(X)
    
    X_pca = pca.fit_transform(X_scaled)
    x_dot_x_pca = np.dot(X_scaled.T, X_pca)
    df_pca = pd.DataFrame(x_dot_x_pca, columns=[f'PC_{i + 1}' for i in range(n_components)],
                       index=X.columns)


    # Normalize, Reindex, & Sort
    df_norm = (df_pca.copy() - df_pca.mean()) / df_pca.std()
    df_norm = df_norm.sort_values(list(df_norm.columns), ascending=False)

    # Absolute value of normalized (& sort)
    df_abs = df_norm.copy().abs().set_index(df_norm.index)
    df_abs = df_abs.sort_values(by=list(df_abs.columns), ascending=False)

    explained_var = pca.explained_variance_ratio_
    df_byvar = df_abs.copy() * explained_var
    df_byvar = df_byvar.sort_values(by=list(df_norm.columns), ascending=False)

    return explained_var, df_byvar


## Download Plots
def download_plotly_fig(fig,plot_name=None):
    if plot_name is None:
        plot_name = ''
    mybuff = StringIO()
    fig.write_html(mybuff, include_plotlyjs='cdn')
    mybuff = BytesIO(mybuff.getvalue().encode())
    b64 = base64.b64encode(mybuff.read()).decode()
    href = f'<a href="data:text/html;charset=utf-8;base64, {b64}" download="{plot_name} plot.html">Download html plot</a>'
    return href