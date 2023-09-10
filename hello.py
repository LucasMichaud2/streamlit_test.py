import streamlit as st
import pandas as pd
import numpy as np

objective_url = 'https://raw.githubusercontent.com/LucasMichaud2/streamlit_test.py/main/Objectives_updated-Table%201.csv'
df_objective = pd.read_csv(objective_url)

data_url =  'https://raw.githubusercontent.com/LucasMichaud2/streamlit_test.py/main/GAMNED_dataset_V2.2.csv'
df_data = pd.read_csv(data_url)

st.dataframe(df_objective)

class GAMNED_UAE:


  def __init__(self, data, rating):
    self.df_data = data[data['country'] == 'uae']
    self.df_rating = rating
    self.obj_list = ['branding', 'consideration', 'conversion']

  def get_age_data(self):
    column_names = ['channel', '13-17', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']
    col1 = ['instagram', 'facebook', 'linkedin', 'snapchat', 'youtube']
    col2 = [8, 4.7, 0, 20, 0]
    col3 = [31, 21.5, 21.7, 38.8, 15]
    col4 = [30, 34.3, 60, 22.8, 20.7]
    col5 = [16, 19.3, 10, 13.8, 16.7]
    col6 = [8, 11.6, 5.4, 3.8, 11.9]
    col7 = [4, 7.2, 2.9, 0, 8.8]
    col8 = [3, 5.6, 0, 0, 9]

    df_age = pd.DataFrame(col1, columns = ['channel'])
    df_age['13-17'] = col2
    df_age['18-24'] = col3
    df_age['25-34'] = col4
    df_age['35-44'] = col5
    df_age['45-54'] = col6
    df_age['55-64'] = col7
    df_age['65+'] = col8

    return df_age



  def uniform_channel(self):
    # make sure we have one exhaustive channel list
    channel_list = pd.concat([self.df_data['channel'], self.df_rating['channel']], axis=0)
    channel_list = channel_list.unique().tolist()
    return channel_list


  def get_mean_rating(self):
    # Get the rating df and output the mean value for each channel
    # The df is all the channels and mean rating in relation to (branding,
    # consideration and conversion)
    mean_ratings = self.df_rating.drop('formats', axis=1)
    mean_ratings = mean_ratings.groupby('channel').mean().reset_index()
    return mean_ratings

  def get_data_freq(self):
    # get the freq of channel used in data for each objectives
    df_freq = self.df_data[['objectif', 'channel']]
    stack_list = []
    for i in self.obj_list:
      temp_df = df_freq[df_freq['objectif'] == i]
      stack_list.append(temp_df['channel'].value_counts())
    df_freq = pd.DataFrame(stack_list)
    df_freq = df_freq.T
    df_freq.columns = self.obj_list
    df_freq = df_freq / df_freq.sum()
    df_freq = df_freq*10
    df_freq = df_freq.reset_index()
    df_freq.rename(columns={'index': 'channel'}, inplace=True)
    return df_freq

  def get_channel_rating(self, input_age, df_age, df_freq, df_rating):
    # Get the final rating of channel and formats depending on age group
    # and objective

    age_column = df_age[input_age].tolist()
    age_channel = df_age['channel'].tolist()

    age_dic = {
        'channel': age_channel,
        'branding': age_column,
        'consideration': age_column,
        'conversion': age_column
    }
    age_table = pd.DataFrame(age_dic)
    age_table.iloc[0:, 1:] =  age_table.iloc[0:, 1:] / 10

    temp1 = pd.concat([df_freq, age_table], axis=0)
    temp1 = pd.concat([temp1, df_rating], axis=0)

    df_channel_rating = temp1.groupby('channel').sum()
    #df_channel_rating.columns = ['channel', 'branding', 'consideration', 'converison']
    df_channel_rating = df_channel_rating.reset_index()

    return df_channel_rating


  def get_format_rating(self, channel_rating):
    # combine format and channel rating

    for index, row in channel_rating.iterrows():

      a_value = row['channel']
      self.df_rating.loc[self.df_rating['channel'] == a_value, self.obj_list] += row[self.obj_list]

    return self.df_rating


  def get_objective(self, input_obj, df_rating):

    df_heatmap = df_rating[['channel', 'formats', input_obj]]
    df_heatmap = df_heatmap.sort_values(by=input_obj, ascending=False)
    return df_heatmap


  def get_target(self):

    target_dic = {
        'channel': ['linkedin', 'search', 'video', 'native ads'],
        'branding': [10, 10, 10, 10],
        'consideration': [10, 10, 10, 10],
        'conversion': [10, 10, 10, 10]
    }

    df_target = pd.DataFrame(target_dic)

    return df_target

  def add_target(self, df_target, channel_rating):

      total_rating = pd.concat([channel_rating, df_target], axis=0)
      total_rating = total_rating.groupby('channel').sum()

      return total_rating

# Getting Variables

gamned_class = GAMEND_UAE(df_data, df_objective)



age_list = ['none', '13-17', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']
age_df = pd.DataFrame(age_list)

objective_list = ['none', 'branding', 'consideration', 'conversion']
objective_df = pd.DataFrame(objective_list)


st.title('GAMNED Marketing Tool')

st.sidebar.title('Parameters')

selected_objective = st.sidebar.selectbox('Select an objective', objective_df)
selected_age = st.sidebar.selectbox("Select an age", age_df)

'''
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
'''
