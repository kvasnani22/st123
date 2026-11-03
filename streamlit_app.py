import streamlit as st

st.title("Hello Streamlit")

st.write("Welcome to the first app")

name = st.text_input("Please enter your name")
hobby= st.text_input("Please enter your hobby")
age= st.text_input("What is the age")
if age:
    if age == False:
        st.warning("Age should be in number")

if st.button("Say hello"):
    if name and hobby:
        st.success(f"great {name} enjoy {hobby}")
    else:
        st.warning("Please fill name and hobby both")


