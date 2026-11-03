import streamlit as st

st.title("Hello Streamlit")

st.write("provide the details")
st.text_input("What is your name")
if st.button("Say hello"):
    if name:
        st.success(f"hello {name}")
