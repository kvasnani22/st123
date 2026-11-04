import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit")

st.write("Welcome to the first app")
st.sidebar.header("Controls")
name = st.sidebar.text_input("Please enter your name")
hobby= st.sidebar.text_input("Please enter your hobby")

greet=st.sidebar.button("Say hello")
if greet:
    if name and hobby:
        st.success(f"great {name} enjoy {hobby}")
    else:
        st.warning("Please fill name and hobby both")

st.divider()
st.header("Data explorer")

data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)
select= st.selectbox("which data do you require in line chart",["A","B","C"])

st.dataframe(data)
st.line_chart(data[select])

