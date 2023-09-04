pip install streamlit matplotlib pandas seaborn


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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


# Sample data for the heatmap
data = {
    'A': [10, 20, 30],
    'B': [40, 50, 60],
    'C': [70, 80, 90]
}

# Create a DataFrame
df_heatmap = pd.DataFrame(data)

# Calculate the correlation matrix
corr_matrix = df_heatmap.corr()

# Create the heatmap using seaborn
plt.figure(figsize=(6, 4))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)

# Display the heatmap using Streamlit
st.title('Heatmap Example')
st.pyplot()
