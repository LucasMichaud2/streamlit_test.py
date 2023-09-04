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
color1 = "#FFFF00"
color2 = "#FFBB00"
color3 = "#440000"

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

def round_5(x):
  return round(x/5) * 5
df['consideration'] = df['consideration'].apply(round_5)

st.dataframe(df)

color_dictionary = {
    0: '#FFFF00', 5: '#FFE000', 10: '#FFA300', 15: '#FF8500', 20: '#FF6600',
    25: '#FF4700', 30: '#FF2800', 35: '#FF0900', 40: '#EE0000', 45: '#DD0000',
    50: '#CC0000', 55: '#BB0000', 60: '#AA0000', 65: '#990000', 70: '#880000',
    75: '#770000', 80: '#660000', 85: '#550000', 90: '#440000', 95: '#330000', 
    100: '#220000'
}

df['mapped_colors'] = df['consideration'].map(color_dictionary)

st.dataframe(df)


st.markdown(
  f"""
  <div style='display: flex;'>
      <div style='background-color:{df.at[0, 'mapped_colors']}; width: 100px; height: 50px; margin-riht: 10px;'></div>
  </div>
  """,
  unsafe_allow_html=True
)
