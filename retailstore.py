import streamlit as st
import pandas as pd
st.title("Retail store")
st.write('Browse products, record purchase and sales')
products= pd.read_csv('products.csv')
st.subheader('Products info')
st.dataframe(products)
st.divider()
st.subheader("Quick sales counter")
if "sales" not in st.session_state:
    st.session_state.sales=0
if st.button("Sell"):
    st.session_state.sales +=1

st.write(f" sales is {st.session_state.sales})






