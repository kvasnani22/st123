import streamlit as st

st.title("Hello Streamlit")

st.write("Welcome to the first app")

name = st.text_input("Please enter your name")
if st.button("Say hello"):
    if name:
        st.success(f"greet now {name}")
    else:
        st.warning("Please give your name first")


