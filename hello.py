import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from streamlit_elements import elements, mui, html, nivo


objective_url = 'https://raw.githubusercontent.com/LucasMichaud2/streamlit_test.py/main/Objectives_updated-Table%201.csv'
df_objective = pd.read_csv(objective_url)

data_url =  'https://raw.githubusercontent.com/LucasMichaud2/streamlit_test.py/main/GAMNED_dataset_V2.2.csv'
df_data = pd.read_csv(data_url)

age_url = 'https://raw.githubusercontent.com/LucasMichaud2/streamlit_test.py/main/Global_data-Table%201.csv'
age_date = pd.read_csv(age_url)

gamned_logo_url = 'https://raw.github.com/LucasMichaud2/streamlit_test.py/main/Logo_G_Gamned_red_baseline.jpg'


header_col1, header_col2 = st.columns(2)

with header_col1:
  st.image(gamned_logo_url)

with header_col2:
  st.text(' ')
  st.text(' ')
  st.text(' ')
  st.text(' ')
  st.text(' ')
  st.text(' ')
  st.text(' ')
  st.text(' ')
  st.text(' ')
  st.text(' ')
  st.text(' ')
  st.text(' ')
  st.text(' ')
  st.text(' ')
  st.text(' ')
  st.text(' ')
  st.text(' ')
  st.text(' ')
  
 
  st.title('Marketing Tool')

  

class GAMNED_UAE:


  def __init__(self, data, rating):
    self.df_data = data[data['country'] == 'uae']
    self.df_rating = rating
    self.obj_list = ['branding', 'consideration', 'conversion']

  def get_age_data(self):
    column_names = ['channel', '13-17', '18-24', '25-34', '35-44', '45-54', '55-64', '65+', '13-17, 18-24', '13-17, 18-24, 25-34',
                   '13-17, 18-24, 25-34, 35-44',
                   '13-17, 18-24, 25-34, 35-44, 45-54', 
                   '13-17, 18-24, 25-34, 35-44, 45-54, 55-64', 
                   '13-17, 18-24, 25-34, 35-44, 45-54, 55-64, 65+', 
                   'all',
                   '18-24, 25-34', 
                   '18-24, 25-34, 35-44', 
                   '18-24, 25-34, 35-44, 45-54', 
                   '18-24, 25-34, 35-44, 45-54, 55-64',
                   '18-24, 25-34, 35-44, 45-54, 55-64, 65+',
                   '25-34, 35-44',
                   '25-34, 35-44, 45-54',
                   '25-34, 35-44, 45-54, 55-64', 
                   '25-34, 35-44, 45-54, 55-64, 65+',
                   '35-44, 45-54', 
                   '35-44, 45-54, 55-64', 
                   '35-44, 45-54, 55-64, 65+', 
                   '45-54, 55-64', 
                   '45-54, 55-64, 65+',
                   '55-64, 65+',
                   '']
    col1 = ['instagram', 'facebook', 'linkedin', 'snapchat', 'youtube']
    col2 = [8, 4.7, 0, 20, 0]
    col3 = [31, 21.5, 21.7, 38.8, 15]
    col4 = [30, 34.3, 60, 22.8, 20.7]
    col5 = [16, 19.3, 10, 13.8, 16.7]
    col6 = [8, 11.6, 5.4, 3.8, 11.9]
    col7 = [4, 7.2, 2.9, 0, 8.8]
    col8 = [3, 5.6, 0, 0, 9]
    col9 = [x + y for x, y in zip(col2, col3)]
    col10 = [x + y for x, y in zip(col9, col4)]
    col11 = [x + y for x, y in zip(col10, col5)]
    col12 = [x + y for x, y in zip(col11, col6)]
    col13 = [x + y for x, y in zip(col12, col7)]
    col14 = [x + y for x, y in zip(col13, col8)]
    col15 = [x + y for x, y in zip(col3, col4)]
    col16 = [x + y for x, y in zip(col15, col5)]
    col17 = [x + y for x, y in zip(col6, col6)]
    col18 = [x + y for x, y in zip(col17, col7)]
    col19 = [x + y for x, y in zip(col18, col8)]
    col20 = [x + y for x, y in zip(col4, col5)]
    col21 = [x + y for x, y in zip(col20, col6)]
    col22 = [x + y for x, y in zip(col21, col7)]
    col23 = [x + y for x, y in zip(col22, col8)]
    col24 = [x + y for x, y in zip(col5, col6)]
    col25 = [x + y for x, y in zip(col24, col7)]
    col26 = [x + y for x, y in zip(col25, col8)]
    col27 = [x + y for x, y in zip(col6, col7)]
    col28 = [x + y for x, y in zip(col27, col8)]
    col29 = [x + y for x, y in zip(col7, col8)]
    col30 = [0, 0, 0, 0, 0]
    
    
    

    df_age = pd.DataFrame(col1, columns = ['channel'])
    df_age['13-17'] = col2
    df_age['18-24'] = col3
    df_age['25-34'] = col4
    df_age['35-44'] = col5
    df_age['45-54'] = col6
    df_age['55-64'] = col7
    df_age['65+'] = col8
    df_age['13-17, 18-24'] = col9
    df_age['13-17, 18-24, 25-34'] = col10
    df_age['13-17, 18-24, 25-34, 35-44'] = col11
    df_age['13-17, 18-24, 25-34, 35-44, 45-54'] = col12
    df_age['13-17, 18-24, 25-34, 35-44, 45-54, 55-64'] = col13
    df_age['13-17, 18-24, 25-34, 35-44, 45-54, 55-64, 65+'] = col14
    df_age['all'] = col14
    df_age['18-24, 25-34'] = col15
    df_age['18-24, 25-34, 35-44'] = col16
    df_age['18-24, 25-34, 35-44, 45-54'] = col17
    df_age['18-24, 25-34, 35-44, 45-54, 55-64'] = col18
    df_age['18-24, 25-34, 35-44, 45-54, 55-64, 65+'] = col19
    df_age['25-34, 35-44'] = col20
    df_age['25-34, 35-44, 45-54'] = col21
    df_age['25-34, 35-44, 45-54, 55-64'] = col22
    df_age['25-34, 35-44, 45-54, 55-64, 65+'] = col23
    df_age['35-44, 45-54'] = col24
    df_age['35-44, 45-54, 55-64'] = col25
    df_age['35-44, 45-54, 55-64, 65+'] = col26
    df_age['45-54, 55-64'] = col27
    df_age['45-54, 55-64, 65+'] = col28
    df_age['55-64, 65+'] = col29
    df_age[''] = col30
    
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

def round_5(x): 
  return round(x/5) * 5

excluded_channel_list = ['youtube', 'instagram', 'display', 'facebook', 'linkedin', 'search', 'snapchat', 'tiktok', 'native ads', 'twitter', 'twitch',
                    'in game advertising', 'amazon', 'audio', 'waze', 'dooh', 'connected tv']

color_dictionary = {
    0: '#F1C40F', 5: '#F4D03F', 10: '#F7DC6F', 15: '#F9E79F', 20: '#FAD7A0',
    25: '#F8C471', 30: '#F5B041', 35: '#F39C12', 40: '#E67E22', 45: '#D35400',
    50: '#EC7063', 55: '#E74C3C', 60: '#CB4335', 65: '#B03A2E', 70: '#943126',
    75: '#78281F', 80: '#8E44AD', 85: '#7D3C98', 90: '#6C3483', 95: '#5B2C6F',
    100: '#4A235A'
}

age_list = ['13-17', '18-24', '25-34', '35-44', '45-54', '55-64', '65+', 'all']
age_df = pd.DataFrame(age_list)

objective_list = ['branding', 'consideration', 'conversion']
objective_df = pd.DataFrame(objective_list)

target_list = ['b2c', 'b2b']
target_df = pd.DataFrame(target_list)

st.text(' ')
st.sidebar.title('Heatmap Parameters')

selected_objective = st.sidebar.selectbox('Select an objective', objective_df)
selected_age = st.sidebar.multiselect("Select an age", age_df)
selected_age = ', '.join(selected_age)
selected_target = st.sidebar.selectbox('Select target', target_df)
excluded_channel = st.sidebar.multiselect("Channel to exclude", excluded_channel_list)
st.sidebar.title('Budget Parameters')
input_budget = st.sidebar.number_input('Budget', value=0)
channel_number = st.sidebar.number_input('Number of channels', value=0)




# Getting Variables

gamned_class = GAMNED_UAE(df_data, df_objective)
df_age = gamned_class.get_age_data()
df_freq = gamned_class.get_data_freq()
df_rating = gamned_class.get_mean_rating()
df_rating1 = gamned_class.get_channel_rating(selected_age, df_age, df_freq, df_rating)
if selected_target == 'b2b':
  df_b2b = gamned_class.get_target()
  df_rating1 = gamned_class.add_target(df_b2b, df_rating1)
  df_rating1 = df_rating1.reset_index()
df_rating2 = gamned_class.get_format_rating(df_rating1)
df_rating3 = gamned_class.get_objective(selected_objective, df_rating2)
df_rating3 = df_rating3[~df_rating3['channel'].isin(excluded_channel)]
df_rating3 = df_rating3.reset_index(drop=True)
st.dataframe(df_rating3)
full_format_rating = df_rating3.copy()
format_rating = df_rating3.copy()
format_rating['format'] = format_rating['channel'] + ' - ' + format_rating['formats']
format_rating = format_rating[['channel', 'formats', 'format', selected_objective]]
min_format = full_format_rating[selected_objective].min()
max_format = full_format_rating[selected_objective].max()
format_rating['norm'] = (format_rating[selected_objective] - min_format) / (max_format - min_format)*100
format_rating['norm'] = format_rating['norm'].apply(round_5)
format_rating['mapped_colors'] = format_rating['norm'].map(color_dictionary)
format_rating = format_rating.reset_index()
format_rating = format_rating.drop(['index'], axis=1)
column_format_drop = ['format', 'norm', 'mapped_colors']
displayed_format = format_rating.drop(columns=column_format_drop)


################################# Second heatmap #######################################

second_heatmap = format_rating.head(36)
heatmap_data = second_heatmap['norm']
heatmap_labels = second_heatmap['format']

st.dataframe(second_heatmap)

################################## Computing Scores ###################################

channel_count = pd.DataFrame(df_rating3.groupby('channel')['formats'].count())
channel_count = channel_count.reset_index()
col_names = ['channel', 'count']
channel_count.columns = col_names

agg_rating = df_rating3.drop(['formats'], axis=1)
agg_rating1 = agg_rating.groupby('channel').sum()
agg_rating1 = agg_rating1.reset_index()
agg_rating2 = agg_rating1.sort_values(by='channel')
channel_count2 = channel_count.sort_values(by='channel')
agg_rating2['average'] = agg_rating2[selected_objective] / channel_count2['count']
agg_rating3 = agg_rating2.sort_values(by='average', ascending=False)
cost_rating = agg_rating3.copy()
agg_rating4 = agg_rating3.copy()
agg_rating_min = agg_rating3['average'].min()
agg_rating_max = agg_rating3['average'].max()
agg_rating3['average'] = ((agg_rating3['average'] - agg_rating_min) / (agg_rating_max - agg_rating_min))*100
output_rating = agg_rating3.copy()


                        

#################################### Building Heatmap ####################################

heat_map = output_rating.drop([selected_objective], axis=1)
#heat_map1 = heat_map.groupby('channel').sum()
#heat_map2= heat_map1.sort_values(by=selected_objective, ascending=False)
heat_map['average'] = heat_map['average'].apply(round_5)

heat_map['mapped_colors'] = heat_map['average'].map(color_dictionary)
heat_map = heat_map.reset_index()
heat_map2 = heat_map.head(10)


##################################### Max Channel Budget ##################################

min_display = 5000
min_inread_video = 5000
min_youtube = 4000
min_facebook = 4000
min_tiktok = 4000
min_instagram = 3000
min_linkedin = 4000
min_snapchat = 3000
min_search = 1000

##################################### Buidling Budget #####################################

cost_rating = cost_rating.drop([selected_objective], axis=1)
cost_rating = cost_rating.sort_values(by='average', ascending=False)
cost_rating = cost_rating.reset_index()
cost_rating_std = cost_rating['average'].std()
cost_rating_mean = cost_rating['average'].mean()
cost_rating['norm'] = (cost_rating['average'] - cost_rating_mean) / cost_rating_std
df_price_rating = cost_rating.copy()
threshold = cost_rating['norm'].max() - 0.50*cost_rating['norm'].max()

# df_allowance now contains the DataFrame with the specified columns dropped

##################################### Imposed budget ######################################

if channel_number == 0:
  if input_budget < 5001 and selected_objective == 'consideration':
    disp_allow = input_budget - 500
    budget_lib1 = {
      'channel': ['display', 'search'],
      'allowance': [disp_allow, 500]
    }
    df_allowance = pd.DataFrame(budget_lib1)
    
  elif input_budget < 5001:
    df_selection = cost_rating.head(1)
    df_budget = df_selection.copy()
    average_max = df_budget['average'].max()
    average_min = df_budget['average'].min()
    average_diff = average_max - average_min
    df_budget['distribution'] = df_budget['average'] / df_budget['average'].sum()
    df_budget['distribution'] = df_budget['distribution'].apply(lambda x: round(x, 2))
    df_budget['allowance'] = input_budget * df_budget['distribution']
    columns_to_drop = ['average', 'index', 'norm', 'distribution']
    df_allowance = df_budget.drop(columns=columns_to_drop)
    
  elif input_budget < 10001 and input_budget > 5000:
    df_selection = cost_rating.head(2)
    df_budget = df_selection.copy()
    average_max = df_budget['average'].max()
    average_min = df_budget['average'].min()
    average_diff = average_max - average_min
    df_budget['distribution'] = df_budget['average'] / df_budget['average'].sum()
    df_budget['distribution'] = df_budget['distribution'].apply(lambda x: round(x, 2))
    df_budget['allowance'] = input_budget * df_budget['distribution']
    columns_to_drop = ['average', 'index', 'norm', 'distribution']
    df_allowance = df_budget.drop(columns=columns_to_drop)

  elif input_budget < 15001 and input_budget > 10000:
    #df_selection = cost_rating[cost_rating['norm'] > threshold]
    df_selection = cost_rating.head(3)
    df_budget = df_selection.copy()
    average_max = df_budget['average'].max()
    average_min = df_budget['average'].min()
    average_diff = average_max - average_min
    df_budget['distribution'] = df_budget['average'] / df_budget['average'].sum()
    df_budget['distribution'] = df_budget['distribution'].apply(lambda x: round(x, 2))
    df_budget['allowance'] = input_budget * df_budget['distribution']
    columns_to_drop = ['average', 'index', 'norm', 'distribution']
    df_allowance = df_budget.drop(columns=columns_to_drop)


  elif input_budget < 20001 and input_budget > 15000:
    #df_selection = cost_rating[cost_rating['norm'] > threshold]
    df_selection = cost_rating.head(4)
    df_budget = df_selection.copy()
    average_max = df_budget['average'].max()
    average_min = df_budget['average'].min()
    average_diff = average_max - average_min
    df_budget['distribution'] = df_budget['average'] / df_budget['average'].sum()
    df_budget['distribution'] = df_budget['distribution'].apply(lambda x: round(x, 2))
    df_budget['allowance'] = input_budget * df_budget['distribution']
    columns_to_drop = ['average', 'index', 'norm', 'distribution']
    df_allowance = df_budget.drop(columns=columns_to_drop)

  elif input_budget < 25001 and input_budget > 20000:
    #df_selection = cost_rating[cost_rating['norm'] > threshold]
    df_selection = cost_rating.head(5)
    df_budget = df_selection.copy()
    average_max = df_budget['average'].max()
    average_min = df_budget['average'].min()
    average_diff = average_max - average_min
    df_budget['distribution'] = df_budget['average'] / df_budget['average'].sum()
    df_budget['distribution'] = df_budget['distribution'].apply(lambda x: round(x, 2))
    df_budget['allowance'] = input_budget * df_budget['distribution']
    columns_to_drop = ['average', 'index', 'norm', 'distribution']
    df_allowance = df_budget.drop(columns=columns_to_drop)

  else:
    df_selection = cost_rating.head(6)
    df_budget = df_selection.copy()
    average_max = df_budget['average'].max()
    average_min = df_budget['average'].min()
    average_diff = average_max - average_min
    df_budget['distribution'] = df_budget['average'] / df_budget['average'].sum()
    df_budget['distribution'] = df_budget['distribution'].apply(lambda x: round(x, 2))
    df_budget['allowance'] = input_budget * df_budget['distribution']
    columns_to_drop = ['average', 'index', 'norm', 'distribution']
    df_allowance = df_budget.drop(columns=columns_to_drop)
    
else:
  df_selection = cost_rating.head(channel_number)
  df_budget = df_selection.copy()
  average_max = df_budget['average'].max()
  average_min = df_budget['average'].min()
  average_diff = average_max - average_min
  df_budget['distribution'] = df_budget['average'] / df_budget['average'].sum()
  df_budget['distribution'] = df_budget['distribution'].apply(lambda x: round(x, 2))
  df_budget['allowance'] = input_budget * df_budget['distribution']
  columns_to_drop = ['average', 'index', 'norm', 'distribution']
  df_allowance = df_budget.drop(columns=columns_to_drop)



#################################### First Bubble Chart ###################################

merged_df = agg_rating4.merge(df_allowance, on='channel', how='inner')
merged_df[selected_objective] = merged_df[selected_objective].apply(lambda x: round(x, 1))
merged_df['average'] = merged_df['average'].apply(lambda x: round(x, 1))
merged_df['average'] = merged_df['average'] * 5 / 25
merged_df[selected_objective] = merged_df[selected_objective] * 5 / 150
                                                                    





##################################### Budget Rules ########################################




  
#elif input_budget < 100001 and input_budget > 5001:
  #if df_allowance.shape[0] > 2:
    #df_budget = df_budget.head(2)
    #df_budget['allowance'] = input_budget * df_budget['distribution']
    #df_allowance = df_budget.drop(columns=columns_to_drop)

  



##################################### taking out the code and name ########################

name0 = format_rating.at[0, 'format']
color0 = format_rating.at[0, 'mapped_colors']
name1 = format_rating.at[1, 'format']
color1 = format_rating.at[1, 'mapped_colors']
name2 = format_rating.at[2, 'format']
color2 = format_rating.at[2, 'mapped_colors']
name3 = format_rating.at[3, 'format']
color3 = format_rating.at[3, 'mapped_colors']
name4 = format_rating.at[4, 'format']
color4 = format_rating.at[4, 'mapped_colors']
name5  = format_rating.at[5, 'format']
color5 = format_rating.at[5, 'mapped_colors']
name6  = format_rating.at[6, 'format']
color6 = format_rating.at[6, 'mapped_colors']
name7  = format_rating.at[7, 'format']
color7 = format_rating.at[7, 'mapped_colors']
name8  = format_rating.at[8, 'format']
color8 = format_rating.at[8, 'mapped_colors']
name9  = format_rating.at[9, 'format']
color9 = format_rating.at[9, 'mapped_colors']
name10  = format_rating.at[10, 'format']
color10 = format_rating.at[10, 'mapped_colors']
name11  = format_rating.at[11, 'format']
color11 = format_rating.at[11, 'mapped_colors']
name12  = format_rating.at[12, 'format']
color12 = format_rating.at[12, 'mapped_colors']
name13  = format_rating.at[13, 'format']
color13 = format_rating.at[13, 'mapped_colors']
name14  = format_rating.at[14, 'format']
color14 = format_rating.at[14, 'mapped_colors']
name15  = format_rating.at[15, 'format']
color15 = format_rating.at[15, 'mapped_colors']
name16  = format_rating.at[16, 'format']
color16 = format_rating.at[16, 'mapped_colors']
name17  = format_rating.at[17, 'format']
color17 = format_rating.at[17, 'mapped_colors']
name18  = format_rating.at[18, 'format']
color18 = format_rating.at[18, 'mapped_colors']
name19  = format_rating.at[19, 'format']
color19 = format_rating.at[19, 'mapped_colors']
name20  = format_rating.at[20, 'format']
color20 = format_rating.at[20, 'mapped_colors']
name21  = format_rating.at[21, 'format']
color21 = format_rating.at[21, 'mapped_colors']
name22  = format_rating.at[22, 'format']
color22 = format_rating.at[22, 'mapped_colors']
name23  = format_rating.at[23, 'format']
color23 = format_rating.at[23, 'mapped_colors']
name24  = format_rating.at[24, 'format']
color24 = format_rating.at[24, 'mapped_colors']
name25  = format_rating.at[25, 'format']
color25 = format_rating.at[25, 'mapped_colors']
name26  = format_rating.at[26, 'format']
color26 = format_rating.at[26, 'mapped_colors']
name27  = format_rating.at[27, 'format']
color27 = format_rating.at[27, 'mapped_colors']
name28  = format_rating.at[28, 'format']
color28 = format_rating.at[28, 'mapped_colors']
name29  = format_rating.at[29, 'format']
color29 = format_rating.at[29, 'mapped_colors']
name30  = format_rating.at[30, 'format']
color30 = format_rating.at[30, 'mapped_colors']
name31  = format_rating.at[31, 'format']
color31 = format_rating.at[31, 'mapped_colors']
name32  = format_rating.at[32, 'format']
color32 = format_rating.at[32, 'mapped_colors']
name33  = format_rating.at[33, 'format']
color33 = format_rating.at[33, 'mapped_colors']
name34  = format_rating.at[34, 'format']
color34 = format_rating.at[34, 'mapped_colors']
name35  = format_rating.at[35, 'format']
color35 = format_rating.at[35, 'mapped_colors']
name36  = format_rating.at[36, 'format']
color36 = format_rating.at[36, 'mapped_colors']
name37  = format_rating.at[37, 'format']
color37 = format_rating.at[37, 'mapped_colors']
name38  = format_rating.at[38, 'format']
color38 = format_rating.at[38, 'mapped_colors']
name39  = format_rating.at[39, 'format']
color39 = format_rating.at[39, 'mapped_colors']


#####################################   Pie Chart freq ####################################

df_freq['branding'] = df_freq['branding'].round(1)
df_freq['consideration'] = df_freq['consideration'].round(1)
df_freq['conversion'] = df_freq['conversion'].round(1)


st.text(' ')


# Display the scrollable table
st.title("Top Formats")

displayed_format = displayed_format[~displayed_format['channel'].isin(excluded_channel)]
displayed_format = displayed_format.reset_index(drop=True)

st.dataframe(displayed_format)


st.text(' ')

st.title("Heatmap")

heatmap_size = 6
heatmap_data = heatmap_data.reset_index()
data_matrix = heatmap_data["norm"].values.reshape(heatmap_size, heatmap_size)
plt.figure(figsize=(25, 25))
sns.heatmap(data_matrix, cmap="flare", annot=False, xticklabels=False, yticklabels=False, cbar=False)
for i in range(heatmap_size):
  for j in range(heatmap_size):
    label = format_rating.at[i+j, 'channel'] + '\n' + '\n' + format_rating.at[i+j, 'formats']
    font_prop = fm.FontProperties(weight='bold', size=17)
    plt.text(j + 0.5, i + 0.5, label, ha='center', color='white', fontsize=17, fontproperties=font_prop)
    
st.pyplot(plt)



st.text(' ')

st.title('Budget Allocation')

budget_column1, budget_column2 = st.columns(2)



with budget_column1:
  
  st.dataframe(df_allowance)

custom_colors1 = sns.color_palette('Blues', n_colors=len(df_allowance))

with budget_column2:

  if input_budget == 0:
    st.text('Awaiting for budget...')

  else: 
  
    fig4, ax4 = plt.subplots()
    ax4.pie(df_allowance['allowance'], labels=df_allowance['channel'], startangle=90, wedgeprops=dict(width=0.4), colors=custom_colors1, autopct='%1.1f%%', pctdistance=0.85,
           textprops=dict(color="black"))
    
    
    center_circle = plt.Circle((0,0), 0.7, fc='white')
    fig4.gca().add_artist(center_circle)
    
    middle_text = ax4.text(0, 0, f"Total: {input_budget} USD", ha='center', va='center', fontsize=12, color='black', weight='bold')
    
    ax4.axis('equal')
    
    st.pyplot(fig4)

st.text(' ')

sns.set_palette("Set1")



#df_bubble['average'] = df_bubble['average'] * 5 / 25

if input_budget != 0:
  
  plt.figure(figsize=(8, 6))
  ax = sns.scatterplot(data=merged_df, x='average', y=selected_objective, size='allowance', sizes=(10, 10000), alpha=1.0, legend=False, hue=merged_df['channel'])
  
  for index, row in merged_df.iterrows():
    label = row['channel']  # Get the label from the 'label' column
    ax.annotate(label, (row['average'], row[selected_objective]), fontsize=12, ha='center')

  plt.xlim(merged_df['average'].min() - 0.5, merged_df['average'].max() + 0.5)
  plt.ylim(merged_df[selected_objective].min() - 0.5, merged_df[selected_objective].max() + 0.5)
  plt.gcf().set_facecolor('none')
  st.pyplot(plt)

             
 
else:
  st.text('Waiting for budget')

st.text(' ')



#################################### Bubble graph test #################################






################################ Cost Test ############################################

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
  
  price_youtube = st.number_input('Youtube $', step=0.1, value=1.0)
  price_nativead = st.number_input('Native Ads $', step=0.1, value=1.0)

with col2:

  price_display = st.number_input('Display $', step=0.1,  value=1.0)
  price_amazon = st.number_input('Amazon $', step=0.1, value=1.0)

with col3:

  
  price_instagram = st.number_input('Instagram $', step=0.1, value=1.0)
  price_tiktok = st.number_input('TikTok $', step=0.1, value=1.0)
  

with col4:

  price_facebook = st.number_input('Facebook $', step=0.1, value=1.0)
  price_twitter = st.number_input('Twitter $', step=0.1, value=1.0)
  

with col5:
  
  price_linkedin = st.number_input('Linkedin $', step=0.1, value=1.0)
  price_connectedtv = st.number_input('Connected TV $', step=0.1,  value=1.0)

with col6:

  price_search = st.number_input('Search $', step=0.1, value=1.0)
  price_snapchat = st.number_input('Snapchat $', step=0.1, value=1.0)

pcol1, pcol2, pcol3, pcol4, pcol5 = st.columns(5)

with pcol1:

  price_gamead = st.number_input('In game ad $', step=0.1, value=1.0)

with pcol2:

  price_twitch = st.number_input('Twitch $', step=0.1, value=1.0)

with pcol3:

  price_dooh = st.number_input('DOOH $', step=0.1, value=1.0)

with pcol4:

  price_audio = st.number_input('Audio $', step=0.1, value=1.0)

with pcol5:

  price_waze = st.number_input('Waze $', step=0.1, value=1.0)


###################################### Creating Dictinary ###################################

price_dict = {
  'youtube': price_youtube, 'display': price_display, 'instagram': price_instagram, 'facebook': price_facebook,
  'linkedin': price_linkedin, 'search': price_search, 'native ads': price_nativead, 'amazon': price_amazon,
  'tiktok': price_tiktok, 'twitter': price_twitter, 'connected tv': price_connectedtv, 'snapchat': price_snapchat,
  'in game advertising': price_gamead, 'twitch': price_twitch, 'dooh': price_dooh, 'audio': price_audio,
  'waze': price_waze
}

######################################## Mapping prices #####################################

df_price_rating['price'] = df_price_rating['channel'].map(price_dict)
df_price_rating = df_price_rating.drop(['norm'], axis=1)
df_price_rating['average'] = df_price_rating['average'].apply(lambda x: round(x, 2))
def square_value(x):
    return x ** 2

df_price_rating['Squared Average'] = df_price_rating['average'].apply(square_value)
df_price_rating['ratio'] = df_price_rating['Squared Average'] / df_price_rating['price']
df_price_rating = df_price_rating.sort_values(by='ratio', ascending=False)





######################################## Making the allowance ################################

if channel_number == 0:
  if input_budget < 5001 and selected_objective == 'consideration':
    disp_allow2 = input_budget - 500
    budget_lib2 = {
      'channel': ['display', 'search'],
      'allowance': [disp_allow2, 500]
    }
    df_allowance2 = pd.DataFrame(budget_lib2)
    
  elif input_budget < 5001:
    df_selection2 = df_price_rating.head(1)
    df_budget2 = df_selection2.copy()
    ratio_max = df_budget2['ratio'].max()
    ratio_min = df_budget2['ratio'].min()
    ratio_diff = ratio_max - ratio_min
    df_budget2['distribution'] = df_budget2['ratio'] / df_budget2['ratio'].sum()
    df_budget2['distribution'] = df_budget2['distribution'].apply(lambda x: round(x, 2))
    df_budget2['allowance'] = input_budget * df_budget2['distribution']
    df_bubble = df_budget2.copy()
    columns_to_drop2 = ['average', 'index', 'Squared Average', 'ratio', 'distribution']
    df_allowance2 = df_budget2.drop(columns=columns_to_drop2)

  elif input_budget < 10001 and input_budget > 5000:
    df_selection2 = df_price_rating.head(2)
    df_budget2 = df_selection2.copy()
    ratio_max = df_budget2['ratio'].max()
    ratio_min = df_budget2['ratio'].min()
    ratio_diff = ratio_max - ratio_min
    df_budget2['distribution'] = df_budget2['ratio'] / df_budget2['ratio'].sum()
    df_budget2['distribution'] = df_budget2['distribution'].apply(lambda x: round(x, 2))
    df_budget2['allowance'] = input_budget * df_budget2['distribution']
    df_bubble = df_budget2.copy()
    columns_to_drop2 = ['average', 'index', 'Squared Average', 'ratio', 'distribution']
    df_allowance2 = df_budget2.drop(columns=columns_to_drop2)

  elif input_budget < 15001 and input_budget > 10000:
    df_selection2 = df_price_rating.head(3)
    df_budget2 = df_selection2.copy()
    ratio_max = df_budget2['ratio'].max()
    ratio_min = df_budget2['ratio'].min()
    ratio_diff = ratio_max - ratio_min
    df_budget2['distribution'] = df_budget2['ratio'] / df_budget2['ratio'].sum()
    df_budget2['distribution'] = df_budget2['distribution'].apply(lambda x: round(x, 2))
    df_budget2['allowance'] = input_budget * df_budget2['distribution']
    df_bubble = df_budget2.copy()
    columns_to_drop2 = ['average', 'index', 'Squared Average', 'ratio', 'distribution']
    df_allowance2 = df_budget2.drop(columns=columns_to_drop2)

  elif input_budget < 20001 and input_budget > 15000:
    df_selection2 = df_price_rating.head(4)
    df_budget2 = df_selection2.copy()
    ratio_max = df_budget2['ratio'].max()
    ratio_min = df_budget2['ratio'].min()
    ratio_diff = ratio_max - ratio_min
    df_budget2['distribution'] = df_budget2['ratio'] / df_budget2['ratio'].sum()
    df_budget2['distribution'] = df_budget2['distribution'].apply(lambda x: round(x, 2))
    df_budget2['allowance'] = input_budget * df_budget2['distribution']
    df_bubble = df_budget2.copy()
    columns_to_drop2 = ['average', 'index', 'Squared Average', 'ratio', 'distribution']
    df_allowance2 = df_budget2.drop(columns=columns_to_drop2)

  elif input_budget < 25001 and input_budget > 15000:
    df_selection2 = df_price_rating.head(5)
    df_budget2 = df_selection2.copy()
    ratio_max = df_budget2['ratio'].max()
    ratio_min = df_budget2['ratio'].min()
    ratio_diff = ratio_max - ratio_min
    df_budget2['distribution'] = df_budget2['ratio'] / df_budget2['ratio'].sum()
    df_budget2['distribution'] = df_budget2['distribution'].apply(lambda x: round(x, 2))
    df_budget2['allowance'] = input_budget * df_budget2['distribution']
    df_bubble = df_budget2.copy()
    columns_to_drop2 = ['average', 'index', 'Squared Average', 'ratio', 'distribution']
    df_allowance2 = df_budget2.drop(columns=columns_to_drop2)

  else:
    df_selection2 = df_price_rating.head(6)
    df_budget2 = df_selection2.copy()
    ratio_max = df_budget2['ratio'].max()
    ratio_min = df_budget2['ratio'].min()
    ratio_diff = ratio_max - ratio_min
    df_budget2['distribution'] = df_budget2['ratio'] / df_budget2['ratio'].sum()
    df_budget2['distribution'] = df_budget2['distribution'].apply(lambda x: round(x, 2))
    df_budget2['allowance'] = input_budget * df_budget2['distribution']
    df_bubble = df_budget2.copy()
    columns_to_drop2 = ['average', 'index', 'Squared Average', 'ratio', 'distribution']
    df_allowance2 = df_budget2.drop(columns=columns_to_drop2)
  
    
else:
  df_selection2 = df_price_rating.head(channel_number)
  df_budget2 = df_selection2.copy()
  ratio_max = df_budget2['ratio'].max()
  ratio_min = df_budget2['ratio'].min()
  ratio_diff = ratio_max - ratio_min
  df_budget2['distribution'] = df_budget2['ratio'] / df_budget2['ratio'].sum()
  df_budget2['distribution'] = df_budget2['distribution'].apply(lambda x: round(x, 2))
  df_budget2['allowance'] = input_budget * df_budget2['distribution']
  df_bubble = df_budget2.copy()
  columns_to_drop2 = ['average', 'index', 'Squared Average', 'ratio', 'distribution']
  df_allowance2 = df_budget2.drop(columns=columns_to_drop2)


st.title('Pricing Optimization')

  
st.dataframe(df_allowance2)

######################################## bubble chart ##########################################


sns.set_palette("Spectral")

column_budget_drop = ['index', 'ratio', 'distribution']
df_bubble = df_bubble.drop(columns=column_budget_drop)
df_bubble['average'] = df_bubble['average'] * 5 / 25
df_bubble['price'] = 1 / df_bubble['price']


if input_budget != 0:
  df_bubble['allowance'] = df_bubble['allowance']
  plt.figure(figsize=(8, 6))
  ax = sns.scatterplot(data=df_bubble, x='average', y='price', size='allowance', sizes=(10, 10000), alpha=1.0, legend=False, hue=df_bubble['channel'])
  
  for index, row in df_bubble.iterrows():
    label = row['channel']  # Get the label from the 'label' column
    ax.annotate(label, (row['average'], row['price']), fontsize=12, ha='center')

  plt.xlim(df_bubble['average'].min() - 0.5, df_bubble['average'].max() + 0.5)
  plt.ylim(df_bubble['price'].min() - 0.5, df_bubble['price'].max() + 0.5)
  plt.gcf().set_facecolor('none')
  st.pyplot(plt)

             

else:
  st.text('Waiting for budget')




with elements("new_element"):

  mui.Typography("Hello world")


with elements("multiple_children"):

    # You have access to Material UI icons using: mui.icon.IconNameHere
    #
    # Multiple children can be added in a single element.
    #
    # <Button>
    #   <EmojiPeople />
    #   <DoubleArrow />
    #   Hello world
    # </Button>

    mui.Button(
        mui.icon.EmojiPeople,
        mui.icon.DoubleArrow,
        "Button with multiple children"
    )

    # You can also add children to an element using a 'with' statement.
    #
    # <Button>
    #   <EmojiPeople />
    #   <DoubleArrow />
    #   <Typography>
    #     Hello world
    #   </Typography>
    # </Button>

    with mui.Button:
        mui.icon.EmojiPeople()
        mui.icon.DoubleArrow()
        mui.Typography("Button with multiple children")




with elements("nivo_charts"):

    # Streamlit Elements includes 45 dataviz components powered by Nivo.

    from streamlit_elements import nivo

    DATA = [
        { "taste": "fruity", "chardonay": 93, "carmenere": 61, "syrah": 114 },
        { "taste": "bitter", "chardonay": 91, "carmenere": 37, "syrah": 72 },
        { "taste": "heavy", "chardonay": 56, "carmenere": 95, "syrah": 99 },
        { "taste": "strong", "chardonay": 64, "carmenere": 90, "syrah": 30 },
        { "taste": "sunny", "chardonay": 119, "carmenere": 94, "syrah": 103 },
    ]


    with mui.Box(sx={"height": 500}):
        nivo.Radar(
            data=DATA,
            keys=[ "chardonay", "carmenere", "syrah" ],
            indexBy="taste",
            valueFormat=">-.2f",
            margin={ "top": 70, "right": 80, "bottom": 40, "left": 80 },
            borderColor={ "from": "color" },
            gridLabelOffset=36,
            dotSize=10,
            dotColor={ "theme": "background" },
            dotBorderWidth=2,
            motionConfig="wobbly",
            legends=[
                {
                    "anchor": "top-left",
                    "direction": "column",
                    "translateX": -50,
                    "translateY": -40,
                    "itemWidth": 80,
                    "itemHeight": 20,
                    "itemTextColor": "#999",
                    "symbolSize": 12,
                    "symbolShape": "circle",
                    "effects": [
                        {
                            "on": "hover",
                            "style": {
                                "itemTextColor": "#000"
                            }
                        }
                    ]
                }
            ],
            theme={
                "background": "#FFFFFF",
                "textColor": "#31333F",
                "tooltip": {
                    "container": {
                        "background": "#FFFFFF",
                        "color": "#31333F",
                    }
                }
            }
        )




##################################### Formatting for Nivo Heatmap #####################################


with elements("nivo_heatmap"):

  heatmap_data = [
    {"id": "php", "Label": "php", "value": 10, "color": "hsl(299, 70%, 50%)"},
    {"id": "java", "Label": "java", "value": 20, "color": "hsl(28, 70%, 50%)"},
    {"id": "python", "Label": "Python", "value": 60, "color": "hsl(8, 70%, 50%)"}
    # Add more data points here
  ]
  
  with mui.Box(sx={"height": 500}):

    nivo.Pie(
      data=heatmap_data,
      #colors={ "theme": "accent" },
      
    )



      
      
    
  




