import streamlit as st
import pandas as pd
st.title("CSV dashboard")
st.write("Upload the CSV to analyse")
st.sidebar.header("Controls")
st.sidebar.subheader("Controls sub header2")
st.sidebar.write(" controls write")
uploaded = st.sidebar.file_uploader("Upload a CSV", type=["csv"])
if uploaded is None:
    st.info("upload as CSV")
    st.stop()

df= pd.read_csv(uploaded)
st.subheader("Preview")
st.dataframe(df)