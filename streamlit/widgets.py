import streamlit as st
import pandas as pd
import numpy as np


st.title("Streamlit text input")

name = st.text_input("Enter your name")
age=st.slider("Select your age",0,100,18)

options =["Male","Female","Other"]
gender=st.selectbox("Select your gender",options)
if age:
    st.write(f"You are {age} years old")
if name:
    st.write(f"Hello {name} you are {age} years old and your gender is {gender} ")

data={
    "Name":["John",'Jane','Joe','Jack'],
    "Age":[28,25,30,35],
    "City":["New York","London","Paris","Tokyo"],
    "Salary":[10000,8000,9000,12000]
}

df=pd.DataFrame(data)
## save data to csv file

df.to_csv("data.csv" )

st.write(df)

upload_file=st.file_uploader("Upload a file",type=["csv","xlsx"])
if upload_file is not None:
    df=pd.read_csv(upload_file)
    st.write(df)

