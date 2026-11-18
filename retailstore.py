import streamlit as st
st.title("Retail store")
st.write('Browse products, record purchase and sales')
products= pd.read_csv('products.csv')
st.subheader('Products info')
st.dataframe(products)

