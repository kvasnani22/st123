import streamlit as st

st.title("Hello Streamlit")

st.write("provide the details")
st.text_input("What is your name")
if st.button("Say hello"):
    st.success(f"hello {name})
