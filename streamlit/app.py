import streamlit as st
import pandas as pd
import numpy as np


## title of the application
st.title("Hello World")

## header of the application
st.header("This is a header")

# to run the file
# streamlit run app.py

## display text
st.write("Hello World")

df=pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

## dsiplay dataframe
st.write('here is the data frame')
st.write(df) 

## create a line chart
chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)