import streamlit as st
import pandas as pd

csv_url = 'https://raw.githubusercontent.com/LucasMichaud2/streamlit_test.py/blob/main/final_csv.csv'
df = pd.read_csv(csv_url)


st.title('Hello World')

st.dataframe(df)
