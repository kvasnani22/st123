import streamlit as st
import pandas as pd
st.title("day 5 loading")
if "count" not in st.session_state:
    st.session_state.count =0

if st.button("+1"):
    count =+1

st.subheader(f'count is{count}')