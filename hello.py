import streamlit as st
import pandas as pd

csv_url = 'https://raw.githubusercontent.com/LucasMichaud2/streamlit_test.py/main/final_csv.csv'
df = pd.read_csv(csv_url)

st.title('My first Dashboard')

st.dataframe(df)

df['Formats'] = df['channel'] + ' ' + df['formats]

st.bar_chart(df)

