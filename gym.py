import streamlit as st
import pandas as pd
st.title("Gym")
st.subheader('Members list')
members = pd.read_csv('members.csv')
st.dataframe(members)