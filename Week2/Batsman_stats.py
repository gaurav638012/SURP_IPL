#!/usr/bin/env python
# coding: utf-8

# In[134]:


from matplotlib import pyplot as plt
import numpy as np
from statistics import *
import pandas as pd
from stats import *


# In[135]:


df = pd.read_csv("clean.csv")
#df.head()


# In[136]:


from collections import defaultdict
x = list(df["batsman"])
y = list(df["batsman_runs"])
res = defaultdict(list)

for key, value in zip(x, y):
    res[key].append(value)

runs = res.values()  
op = list(runs)
final = []
balls_f = []
n = len(op)
i = 0
while i<n:
    final.append(sum(op[i]))
    balls_f.append(len(op[i]))
    i = i+1

bat = list(df.batsman.unique())

n = len(op)
boundaries = np.zeros(n)
sixes = np.zeros(n)
j = 0
while j<n:
    for run in op[j]:
        if run==4 or run==5:
            boundaries[j] = boundaries[j] +1
        elif run==6:
            sixes[j] = sixes[j] + 1
    j = j+1
    

#required :

scores = {bat[i]: int(final[i]) for i in range(len(bat))}
balls_faced = {bat[i]: int(balls_f[i]) for i in range(len(bat))}
strike_rate = {bat[i]: float("{:.2f}".format((final[i]/balls_f[i])*100)) for i in range(len(bat))}
boundary = {bat[i]: int(boundaries[i]) for i in range(len(bat))}
six = {bat[i]: int(sixes[i]) for i in range(len(bat))}


# In[137]:


sc = pd.DataFrame(scores, index=[0])
d1 = sc.T
bf = pd.DataFrame(balls_faced, index=[0])
d2 = bf.T
sr = pd.DataFrame(strike_rate, index=[0])
d3 = sr.T
b = pd.DataFrame(boundary, index=[0])
d4 = b.T
s = pd.DataFrame(six, index=[0])
d5 = s.T

p1 = pd.merge(d1, d2, left_index=True, right_index=True)
p2 = pd.merge(p1, d3, left_index=True, right_index=True)
p3 = pd.merge(p2, d4, left_index=True, right_index=True)
p4 = pd.merge(p3, d5, left_index=True, right_index=True)
p4.columns = ['Runs Scored','Balls Played','Strike Rate','Boundaries','Sixes']

#p4.head()
#data.close()

matches = []
fifties = []
hundreds = []
dismissals = []
runs1 = []
runs2 = []
runs3 = []
wins = []

players = list(p4.index)

for name in players:
    d = stats(name)
    data = pd.DataFrame.from_dict(d, orient ='index')
    data1 = data.sum(axis = 0)
    matches.append(len(d))
    fifties.append(int(data1[6]))
    hundreds.append(int(data1[7]))
    dismissals.append(int(data1[5]))
    runs1.append(int(data1[8]))
    runs2.append(int(data1[9]))
    runs3.append(int(data1[10]))
    wins.append(int(data1[11]))

p4['Matches Played'] = np.array(matches)
p4['Dismissals'] = np.array(dismissals)
p4['50s'] = np.array(fifties)
p4['100s'] = np.array(hundreds)
p4['Wins Contributed'] = np.array(wins)
p4['Runs in Powerplay'] = np.array(runs1)
p4['Runs in Middle Overs'] = np.array(runs2)
p4['Runs in Death Overs'] = np.array(runs3)

p4.to_csv("data.csv")