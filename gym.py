import streamlit as st
import pandas as pd
st.title("Gym")
st.subheader('Members list')
members = pd.read_csv('members.csv')
st.dataframe(members)
st.divider()
if "checkins" not in st.session_state:
    st.session_state.checkins=0
if st.button("check-in"):
    st.session_state.checkins+=1

st.write(" checkin is +=1")

    