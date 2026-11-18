import streamlit as st
import pandas as pd
st.title('Expense tracker')
st.subheader('Expenses')
expenses= pd.read_csv('expenses.csv')
st.dataframe(expenses)


