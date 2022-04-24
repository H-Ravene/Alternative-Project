#!/usr/bin/env python
# coding: utf-8

# In[4]:


#In this project, we are given a text file with chess tournament results where the information has some structure. We are going to create a Jupyter Notebook that generates a .CSV file with the following information for all of the chess players: Player’s Name, Player’s State, Total Number of Points, Player’s Pre-Rating, and Average Pre Tournament Chess Rating of Opponents
import pandas as pd
import re
import sys
import numpy as np
#Reading the text file into jupyter
textfile = open('tournamentinfo.txt')
#Seperating the lines by stripping them and storing them in a list 
text_table = [line.strip() for line in textfile.readlines()]
text_table
#Creating a few lists to store some of the data
player_state = []
player_number = []
id_data = []
name_data = []
state = '([A-Z]{2})'
number = '([0-9]{1})'
dash = '^-'
#Using a for-loop to parse through the table
for line in text_table:
    if not re.search(dash, line):
        if re.search(state, line) and not re.search(dash, line):
            text =  line.replace('/', '').replace('-','').replace('>','').replace(':','') 
            state_num = text.strip().replace('|', ',')[:3].strip(',')
            if re.search(state, state_num):
                player_state.append(state_num)
                id_data.append(text[5:].strip('').replace('|',','))
            elif re.search(number, state_num):
                name_data.append(text[4:].strip().replace('|',','))
                player_number.append(state_num)
#Creating a list of columns to store these values.               
player_names = []
rounds = []
uscf_id = []
ratings = []
total_points = []

for item in name_data:
    total_points.append(float(item[33:36]))
    player_names.append(item[:28].split())
    rounds.append(item[39:].replace(' ', '' ).strip(',').split(','))


pd.options.display.max_rows = 70
games_df = pd.DataFrame(rounds, columns = ['Round1','Round2','Round3','Round4','Round5','Round6','Round7'], 
                   index = [player for player in player_number])

for item in id_data:
    uscf_id.append(item.replace('R', '').replace('P', ' ')[:8])
    ratings.append(item.replace('R', '').replace('P', ' ')[11:16])
#Adding the columns that the DataFrame using index and list comprehension for each particular one
games_df['Ratings'] = [rate for rate in ratings]
games_df['Total_Points'] = [n for n in total_points]
games_df['Player_ID'] = [n for n in player_number]
games_df['State'] = [state for state in player_state]
games_df['Player_Names'] = [player for player in player_names]
#Using indexing and mapping of cells containting letters and removing them using map function and lambdas.
games_df['Round1'] = games_df['Round1'].map(lambda x: x.lstrip('W')).map(lambda x: x.lstrip('U'))
games_df['Round1'] = games_df['Round1'].map(lambda x: x.lstrip('D')).map(lambda x: x.lstrip('L'))
games_df['Round1'] = games_df['Round1'].map(lambda x: x.lstrip('H')).map(lambda x: x.lstrip('B'))
games_df['Round1'] = games_df['Round1'].map(lambda x: x.lstrip('X'))

games_df['Round2'] = games_df['Round2'].map(lambda x: x.lstrip('W')).map(lambda x: x.lstrip('U'))
games_df['Round2'] = games_df['Round2'].map(lambda x: x.lstrip('D')).map(lambda x: x.lstrip('L'))
games_df['Round2'] = games_df['Round2'].map(lambda x: x.lstrip('H')).map(lambda x: x.lstrip('B'))
games_df['Round2'] = games_df['Round2'].map(lambda x: x.lstrip('X'))

games_df['Round3'] = games_df['Round3'].map(lambda x: x.lstrip('W')).map(lambda x: x.lstrip('U'))
games_df['Round3'] = games_df['Round3'].map(lambda x: x.lstrip('D')).map(lambda x: x.lstrip('L'))
games_df['Round3'] = games_df['Round3'].map(lambda x: x.lstrip('H')).map(lambda x: x.lstrip('B'))
games_df['Round3'] = games_df['Round3'].map(lambda x: x.lstrip('X'))

games_df['Round4'] = games_df['Round4'].map(lambda x: x.lstrip('W')).map(lambda x: x.lstrip('U'))
games_df['Round4'] = games_df['Round4'].map(lambda x: x.lstrip('D')).map(lambda x: x.lstrip('L'))
games_df['Round4'] = games_df['Round4'].map(lambda x: x.lstrip('H')).map(lambda x: x.lstrip('B'))
games_df['Round4'] = games_df['Round4'].map(lambda x: x.lstrip('X'))

games_df['Round5'] = games_df['Round5'].map(lambda x: x.lstrip('W')).map(lambda x: x.lstrip('U'))
games_df['Round5'] = games_df['Round5'].map(lambda x: x.lstrip('D')).map(lambda x: x.lstrip('L'))
games_df['Round5'] = games_df['Round5'].map(lambda x: x.lstrip('H')).map(lambda x: x.lstrip('B'))
games_df['Round5'] = games_df['Round5'].map(lambda x: x.lstrip('X'))

games_df['Round6'] = games_df['Round6'].map(lambda x: x.lstrip('W')).map(lambda x: x.lstrip('U'))
games_df['Round6'] = games_df['Round6'].map(lambda x: x.lstrip('D')).map(lambda x: x.lstrip('L'))
games_df['Round6'] = games_df['Round6'].map(lambda x: x.lstrip('H')).map(lambda x: x.lstrip('B'))
games_df['Round6'] = games_df['Round6'].map(lambda x: x.lstrip('X'))

games_df['Round7'] = games_df['Round7'].map(lambda x: x.lstrip('W')).map(lambda x: x.lstrip('U'))
games_df['Round7'] = games_df['Round7'].map(lambda x: x.lstrip('D')).map(lambda x: x.lstrip('L'))
games_df['Round7'] = games_df['Round7'].map(lambda x: x.lstrip('H')).map(lambda x: x.lstrip('B'))
games_df['Round7'] = games_df['Round7'].map(lambda x: x.lstrip('X'))
#Replacing the empty string values with get.nan 
games_df['Round1'].replace('', 0, inplace=True)
games_df['Round2'].replace('', 0, inplace=True)
games_df['Round3'].replace('', 0, inplace=True)
games_df['Round4'].replace('', 0, inplace=True)
games_df['Round5'].replace('', 0, inplace=True)
games_df['Round6'].replace('', 0, inplace=True)
games_df['Round7'].replace('', 0, inplace=True)
#We will index to the Player Names to compare the data better to the original table.
games_df.set_index(['Player_Names'])
#We are creating a series of the data that we will be analyzing further
games_df.set_index(['Round1', 'Round2', 'Round3', 'Round4', 'Round5', 'Round6', 'Round7'])['Ratings']
#This function is indexing the cells in the columns to their respective indexed players rating and replacing them, after this replacement is made all the data is then computed and divided by the number of games played which returns a column with the players Average Pre Tournament Chess Rating of Opponents.
def parse_series(series):
    player_mapping = {}
    average_rating = []
    for index, row in series.iterrows():
        player_mapping[int(row['Player_ID'])] = int(row['Ratings'])
    for index, row in series.iterrows():
        
        if row[0] is not None:
            try:
                key1 = int(row.Round1)
                row.Round1 = player_mapping[key1]

                key2 = int(row.Round2)
                row.Round2 = player_mapping[key2]

                key3 = int(row.Round3)
                row.Round3 = player_mapping[key3]

                key4 = int(row.Round4)
                row.Round4 = player_mapping[key4]

                key5 = int(row.Round5)
                row.Round5 = player_mapping[key5]

                key6 = int(row.Round6)
                row.Round6 = player_mapping[key6]

                key7 = int(row.Round7)
                row.Round7 = player_mapping[key7]

                total = row.Round1 + row.Round2 + row.Round3 + row.Round4 + row.Round5 + row.Round6 + row.Round7
                games = len([row.Round1, row.Round2, row.Round3, row.Round4, row.Round5, row.Round6, row.Round7])
                average_rating.append(total/games)
            except KeyError:
                total = int(row.Round1) + int(row.Round2) + int(row.Round3) + int(row.Round4) + int(row.Round5) + int(row.Round6) + int(row.Round7)
                games = len([row.Round1, row.Round2, row.Round3, row.Round4, row.Round5, row.Round6, row.Round7])
                average_rating.append(total/games)
    return average_rating
#Creating an object that will process the parse_series function and return its list values
average_rate = parse_series(games_df)
#Adding the column Average_Rating to the games_df DataFrame object.
games_df['Average_Rating'] = [n for n in average_rate]
games_df.head()
games_df.tail()
#creating and sending the data to CSV File using the to_csv method.
games_df.to_csv('Project_2_results', sep=',', encoding='utf-8')




# In[ ]:




