import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

#loading data
@st.cache_data
def get_data():
    df=pd.read_csv("cars.csv")
    return df

#accessing data
df = get_data()


#used siderbar
use_category=st.sidebar.radio("Select Category:",options=df["Foreign_Local_Used"], default=df["Foreign_Local_Used"])

#Automation siderbar
automation=st.sidebar.radio("Select Automation:",options=df["Automation"], default=df["Automation"])

#seat makesiderbar
sit_make=st.sidebar.radio("Select Seat Make:",options=df["seat-make"], default=df["seat-make"])

#manufacturer siderbar
manufacturer=st.sidebar.multiselect("Select Manufacturer:",options=df["manufacturer"], default=df["manufacturer"])

#converting data into data frame
st.dataframe(df)