import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# web app title
st.markdown(''' 
            # **Exploratory Data Analysis** 
            This app is developed by Salman Virani.
            This app is called **EDA App**''')

# how to upload a file from pc

with st.sidebar.header("Upload your dataset(.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your dataset", type=["csv", "txt"])
    df = sns.load_dataset('titanic')
    st.sidebar.markdown("[Example CSV file](df)")

# profiling report for pandas

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative = True)
    st.header('**Input Df**')
    st.write(df)
    st.write('---')
    st.header('**Profiling Report with Pandas**')
    st_profile_report(pr)
else:
    st.info('No file uploaded')
    if st.button('Press to use example'):
        @st.cache
        def load_data():
            a = pd.DataFrame(np.random.rand(100, 5),
                             columns = ['a', 'b', 'c', 'd', 'e'])
            return a
        df = load_data()
        pr = ProfileReport(df, explorative = True)
        st.head('**Input DatadFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)







