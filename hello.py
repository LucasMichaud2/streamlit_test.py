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
df_min = df['consideration'].min()
df_max = df['consideration'].max()
df['consideration'] = ((df['consideration'] - df_min) / (df_max-df_min))*100
                             
st.dataframe(df)

st.bar_chart(df, x='Formats', y='consideration')



with st.sidebar:
  st.write('this is a side bar')
  with st.container():
    st.write('this is a container')


import streamlit as st

st.title("Colored Box Example")

# Define colors
color1 = "#FF5733"
color2 = "#33FF57"
color3 = "#5733FF"

# Create colored boxes using Markdown with CSS
st.markdown(
    f"""
    <div style='display: flex;'>
        <div style='background-color:{color1}; width: 100px; height: 100px; margin-right: 10px;'></div>
        <div style='background-color:{color2}; width: 100px; height: 100px; margin-right: 10px;'></div>
        <div style='background-color:{color3}; width: 100px; height: 100px;'></div>
    </div>
    """,
    unsafe_allow_html=True
)

