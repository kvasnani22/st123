import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit")

st.write("Welcome to the first app")

name = st.text_input("Please enter your name")
hobby= st.text_input("Please enter your hobby")

if st.button("Say hello"):
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
st.dataframe(data)
st.line_chart(data)

