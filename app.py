from pages.about import  about
# from pages.timeseries import TimeSeriesnAnalysis
from pages.EDA import EDAAnalysis
from pages.correlation import CorrelationAnalysis
# from pages.population import  PopulationAnalysis
from pages.PCA import PCAAnalysis
from pages.BYOD import *
from pages.utils_funcs import *

import streamlit as st


def main():
    st.set_page_config(layout="wide")
    st.sidebar.markdown(f"<h2 style='text-align: left; color: green;'>Select Analysis Type</h2>", unsafe_allow_html=True)
    analysis_type = st.sidebar.radio('',
                                     ['About',
                                    #   'Time Series',
                                      'EDA', 
                                      'Correlation',
                                    #   'Population',
                                      'PCA',
                                    #   'BYOD [Bring Your Own Data]'
                                      ]
                                     )

    if analysis_type == 'About':
        about()
    else:
        df = get_data()
        st.header('Display data!')
        st.dataframe(df)
        try:
            if analysis_type == 'EDA':
                EDAAnalysis()
            elif analysis_type == 'Correlation':
                CorrelationAnalysis()
            elif analysis_type == 'PCA':
                url = r'https://medium.com/@gaurav_bio/creating-visualizations-to-better-understand-your-data-and-models-part-1-a51e7e5af9c0'
                text=f'Check out this [link]({url}) for Feature Importance using PCA'#.format(link=a_link)
                st.header(text)
                PCAAnalysis()
            else:
                pass
        except:
            pass

if __name__ == "__main__":
    # st.set_page_config(layout="wide")
    main()