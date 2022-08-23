#!/usr/bin/env python
# coding: utf-8

# # Packages 

# In[4]:


import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# In[5]:


playerdata = pd.read_csv("D:\Internet Downloads\EPL_DS_Challenge\epl_players.csv")
playerdata.head(100)


# In[6]:


playeravg = playerdata.groupby("player_id")
playeravg.mean()


# In[7]:


playerdata.columns


# In[22]:


playeravg = playerdata.groupby(["player_id",'birthday', 'height', 'weight','preferred_foot'])
df1 = playeravg.mean()


# In[23]:


df1


# In[10]:


df1.describe()


# In[11]:


df1.quantile(0.90)


# In[12]:


df1['type'] = df1['gk_diving'] + df1['gk_reflexes']


# In[13]:


df1['type'].head()


# ## Goal Keepers

# In[24]:


df1.loc[(df1['gk_diving']>=78.07) & (df1['gk_handling']>=74.71) & (df1['gk_kicking']>=75.68) & (df1['gk_positioning']>=75.40) & (df1['gk_reflexes']>=80.01), 'type'] = 'Goal Keeper'
# df1.loc[df1['gk_diving']>=69.96, 'type'] = 'Goal Keeper'
# df1.loc[df1['gk_diving']>=69.96 and df1['gk_handling']>=67.2, 'type'] = 'Goal Keeper'
df1[df1['type']=='Goal Keeper'].head(100)


# In[15]:


df1.quantile(0.1)


# In[16]:


df1.loc[(df1['gk_diving']<=6.16) & (df1['gk_handling']<=8.08) & (df1['gk_kicking']<=10) & (df1['gk_positioning']<=8.02) & (df1['gk_reflexes']<=7.85), 'type'] = 'Least Goal Keeper'
df1[df1['type']=='Least Goal Keeper'].head(100)


# In[17]:


df1.loc[(df1['sprint_speed']>=78.07) & (df1['gk_handling']>=74.71) & (df1['gk_kicking']>=75.68) & (df1['gk_positioning']>=75.40) & (df1['gk_reflexes']>=80.01), 'type'] = 'Goal Keeper'
df2 = pd.read_csv("D:\Internet Downloads\EPL_DS_Challenge\epl_goals.csv")

playervisegoals = df2.groupby(["player1_id"])
playergoals = playervisegoals.sum()
playergoals.head(100)


# In[18]:


player2visegoals = df2.groupby(["player2_id"])
player2goals = player2visegoals.sum()
player2goals.head(100)


# In[19]:


df1.loc[(df1['free_kick_accuracy']>=23.81) & (df1['dribbling']>=31.49) & (df1['long_passing']>=39.15) & (df1['long_shots']>=24.22) & (df1['sprint_speed']>=53.98) & (df1['aggression']>=41.32), 'type'] = 'Fielder'
# heading_accuracy      85.250087
# free_kick_accuracy    23.814035
# dribbling             31.494444
# long_passing          39.155769
# long_shots            24.225103
# sprint_speed          53.984615
# aggression            41.328261

# crossing              78.506536
# finishing             78.066154
# heading_accuracy      80.694444
# short_passing         80.831250
# volleys               77.569730
# dribbling             82.298485
# curve                 79.611182
# free_kick_accuracy    76.797241
# long_passing          76.936000
# ball_control          82.782801
# acceleration          86.725439
# sprint_speed          85.951429
# agility               84.132500
# reactions             80.213333
# balance               82.000000
# shot_power            82.770330
# jumping               82.300811
# stamina               83.794286
# strength              85.586667
# long_shots            78.459211
# aggression            83.825926
# interceptions         78.663866
# positioning           79.066387
# vision                80.500000
# penalties             78.075000
# marking               77.500000
# standing_tackle       79.869333
# sliding_tackle        78.621615

df1[df1['type']=='Fielder'].head(100)


# ## Least valuable

# In[20]:


df1.loc[(df1['free_kick_accuracy']<=23.81) & (df1['dribbling']<=31.49) & (df1['long_passing']<=39.15) & (df1['long_shots']<=24.22) & (df1['sprint_speed']<=53.98) & (df1['aggression']<=41.32), 'type'] = 'Least Fielder'
# crossing              27.960000
# finishing             22.573313
# heading_accuracy      36.147619
# short_passing         47.883908
# volleys               22.612364
# dribbling             31.494444
# curve                 25.000000
# free_kick_accuracy    23.814035
# long_passing          39.155769
# ball_control          49.473103
# acceleration          52.125000
# sprint_speed          53.984615
# agility               50.000000
# reactions             58.000000
# balance               52.028000
# shot_power            38.000000
# jumping               55.000000
# stamina               55.189881
# strength              56.347059
# long_shots            24.225103
# aggression            41.328261
# interceptions         29.424675
# positioning           35.200000
# vision                40.669231
# penalties             39.405049
# marking               20.000000
# standing_tackle       21.317538
# sliding_tackle        19.517500
# gk_diving              6.166667
# gk_handling            8.082667
# gk_kicking            10.000000
# gk_positioning         8.021622
# gk_reflexes            7.854945
df1[df1['type']=='Least Fielder'].head(100)


# In[25]:


df1.loc[(df1['free_kick_accuracy']>=72.50) & (df1['dribbling']>=79.59) & (df1['long_passing']>=73.5) & (df1['long_shots']>=74.54) & (df1['sprint_speed']>=82.69) & (df1['aggression']>=80.74), 'type'] = 'Fielder'

# crossing              75.407500
# finishing             75.068182
# heading_accuracy      77.825397
# short_passing         78.451667
# volleys               74.425889
# dribbling             79.599043
# curve                 75.344138
# free_kick_accuracy    72.502703
# long_passing          73.500000
# ball_control          79.521212
# acceleration          83.010000
# sprint_speed          82.694587
# agility               81.000000
# reactions             77.701667
# balance               79.000000
# shot_power            80.000000
# jumping               79.683621
# stamina               81.008333
# strength              82.200000
# long_shots            74.548571
# aggression            80.745378
# interceptions         75.923577
# positioning           76.795833
# vision                77.026279
# penalties             75.090196
# marking               74.255556
# standing_tackle       77.154327
# sliding_tackle        76.000000
# gk_diving             14.712381
# gk_handling           21.000000
# gk_kicking            59.761905
# gk_positioning        21.000000
# gk_reflexes           21.000000
df1[df1['type']=='Fielder'].head(100)


# # EPL Results

# In[61]:


matches = pd.read_csv("D:\Internet Downloads\EPL_DS_Challenge\epl_matches_train.csv")
matches.head(100)


# In[62]:


matches['result'] = matches['stage'] + matches['stage']
matches.loc[(matches['home_team_goal']>matches['away_team_goal']), 'result'] = 'Win'
matches.loc[(matches['home_team_goal']==matches['away_team_goal']), 'result'] = 'Draw'
matches.loc[(matches['home_team_goal']<matches['away_team_goal']), 'result'] = 'Lose'
matches.fillna(0)
matches.head(100)


# In[63]:


matches_test = pd.read_csv("D:\Internet Downloads\EPL_DS_Challenge\epl_matches_test.csv")
matches_test.fillna(0)
matches_test.head()


# In[51]:


matches_test.columns


# In[52]:


matches.columns


# In[40]:


# X_train = matches['home_team_id']


# In[65]:


X_train = matches[['home_team_id', 'away_team_id',
       'home_player_X1', 'home_player_X2', 'home_player_X3', 'home_player_X4',
       'home_player_X5', 'home_player_X6', 'home_player_X7', 'home_player_X8',
       'home_player_X9', 'home_player_X10', 'home_player_X11',
       'away_player_X1', 'away_player_X2', 'away_player_X3', 'away_player_X4',
       'away_player_X5', 'away_player_X6', 'away_player_X7', 'away_player_X8',
       'away_player_X9', 'away_player_X10', 'away_player_X11',
       'home_player_Y1', 'home_player_Y2', 'home_player_Y3', 'home_player_Y4',
       'home_player_Y5', 'home_player_Y6', 'home_player_Y7', 'home_player_Y8',
       'home_player_Y9', 'home_player_Y10', 'home_player_Y11',
       'away_player_Y1', 'away_player_Y2', 'away_player_Y3', 'away_player_Y4',
       'away_player_Y5', 'away_player_Y6', 'away_player_Y7', 'away_player_Y8',
       'away_player_Y9', 'away_player_Y10', 'away_player_Y11', 'home_player_1',
       'home_player_2', 'home_player_3', 'home_player_4', 'home_player_5',
       'home_player_6', 'home_player_7', 'home_player_8', 'home_player_9',
       'home_player_10', 'home_player_11', 'away_player_1', 'away_player_2',
       'away_player_3', 'away_player_4', 'away_player_5', 'away_player_6',
       'away_player_7', 'away_player_8', 'away_player_9', 'away_player_10',
       'away_player_11']]
y_train = matches['result']
X_test = matches_test[['home_team_id', 'away_team_id',
       'home_player_X1', 'home_player_X2', 'home_player_X3', 'home_player_X4',
       'home_player_X5', 'home_player_X6', 'home_player_X7', 'home_player_X8',
       'home_player_X9', 'home_player_X10', 'home_player_X11',
       'away_player_X1', 'away_player_X2', 'away_player_X3', 'away_player_X4',
       'away_player_X5', 'away_player_X6', 'away_player_X7', 'away_player_X8',
       'away_player_X9', 'away_player_X10', 'away_player_X11',
       'home_player_Y1', 'home_player_Y2', 'home_player_Y3', 'home_player_Y4',
       'home_player_Y5', 'home_player_Y6', 'home_player_Y7', 'home_player_Y8',
       'home_player_Y9', 'home_player_Y10', 'home_player_Y11',
       'away_player_Y1', 'away_player_Y2', 'away_player_Y3', 'away_player_Y4',
       'away_player_Y5', 'away_player_Y6', 'away_player_Y7', 'away_player_Y8',
       'away_player_Y9', 'away_player_Y10', 'away_player_Y11', 'home_player_1',
       'home_player_2', 'home_player_3', 'home_player_4', 'home_player_5',
       'home_player_6', 'home_player_7', 'home_player_8', 'home_player_9',
       'home_player_10', 'home_player_11', 'away_player_1', 'away_player_2',
       'away_player_3', 'away_player_4', 'away_player_5', 'away_player_6',
       'away_player_7', 'away_player_8', 'away_player_9', 'away_player_10',
       'away_player_11']]

# from sklearn.linear_model import LogisticRegression
# logisticRegr = LogisticRegression()
# logisticRegr.fit(X_train, y_train)
# predictions = logisticRegr.predict(X_test)
# predictions.head(100)


# In[70]:


X_train = X_train.fillna(0)
y_train = y_train.fillna(0)
X_test = X_test.fillna(0)


# In[74]:


# X_test.isnull().sum()


# In[77]:


from sklearn.linear_model import LogisticRegression
logisticRegr = LogisticRegression()
logisticRegr.fit(X_train, y_train)
predictions = logisticRegr.predict(X_test)
# predictions.head(100)
predictions

