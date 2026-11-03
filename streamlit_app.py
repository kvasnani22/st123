import streamlit as st

st.title("Hello Streamlit")

st.write("Welcome to the first app")

name = st.text_input("Please enter your name")
hobby= st text_input("Please enter your hobby")
if st.button("Say hello"):
    if name and hobby:
        st.success(f"great {name} enjoy {hobby}")
    else:
        st.warning("Please fill name and hobby both")


