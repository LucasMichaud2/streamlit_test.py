import streamlit as st
import pandas as pd
import numpy as np

csv_url = 'https://raw.githubusercontent.com/LucasMichaud2/streamlit_test.py/main/final_csv.csv'
df = pd.read_csv(csv_url)

st.title('My first Dashboard')

st.dataframe(df)

df['Formats'] = df['channel'] + ' ' + df['formats']
df = df.drop(columns=['channel'])
df = df.drop(columns=['formats'])
df['consideration'] = np.exp(df['consideration']
                             
st.dataframe(df)

st.bar_chart(df, x='Formats', y='consideration')

