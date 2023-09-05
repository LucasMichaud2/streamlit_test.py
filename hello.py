import streamlit as st
import pandas as pd
import numpy as np


csv_url = 'https://raw.githubusercontent.com/LucasMichaud2/streamlit_test.py/main/final_csv.csv'
df = pd.read_csv(csv_url)
options = df['channel'

st.title('My first Dashboard')

st.sidebar.title('This is a sidebar')

selected_option = st.sidebar.selectbox("Select an option", options)

st.dataframe(df[df['channel'] == selected_option])


df['Formats'] = df['channel'] + ' ' + df['formats']
df = df.drop(columns=['channel'])
df = df.drop(columns=['formats'])
df_min = df['consideration'].min()
df_max = df['consideration'].max()
df['consideration'] = ((df['consideration'] - df_min) / (df_max-df_min))*100
                             
st.dataframe(df)

st.bar_chart(df, x='Formats', y='consideration')

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
    0: '#F1C40F', 5: '#F4D03F', 10: '#F7DC6F', 15: '#F9E79F', 20: '#FAD7A0',
    25: '#F8C471', 30: '#F5B041', 35: '#F39C12', 40: '#E67E22', 45: '#D35400',
    50: '#EC7063', 55: '#E74C3C', 60: '#CB4335', 65: '#B03A2E', 70: '943126',
    75: '#78281F', 80: '#8E44AD', 85: '#7D3C98', 90: '#6C3483', 95: '#5B2C6F', 
    100: '#4A235A'
}

df['mapped_colors'] = df['consideration'].map(color_dictionary)

st.dataframe(df)


st.markdown(
  f"""
  <div style='display: flex;'>
      <div style='background-color:{df.at[0, 'mapped_colors']}; width: {'100px'}; height: {'75px'}; margin-riht: {'50px'}; font-size:{'10px'};
      display: flex; align-items: {'center'}; justify-content: {'center'}; border-radius: {'20px'};'>{df.at[0, 'Formats']}</div>
      <div style='background-color:{df.at[5, 'mapped_colors']}; width: 100px; height: 50px; margin-riht: 10px;'></div>
      <div style='background-color:{df.at[10, 'mapped_colors']}; width: 100px; height: 50px; margin-riht: 10px;'></div>
      <div style='background-color:{df.at[15, 'mapped_colors']}; width: 100px; height: 50px; margin-riht: 10px;'></div>
      <div style='background-color:{df.at[18, 'mapped_colors']}; width: 100px; height: 50px;'></div>
  </div>
  """,
  unsafe_allow_html=True
)
