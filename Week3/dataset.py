import pandas as pd
from stats import *

dict = {'Batting Innings': [], 'Batting Position': [], 'Runs Scored': [], 'Balls Faced': [], 'Batting Strikerate': [], 'Out/NotOut': [], '4s': [], '6s': [], '50s': [], '100s': [], 'Runs in Powerplay': [], 'Runs in Middle Overs': [], 'Runs in Death Overs': [], 'Strikerate in first 20 balls': [], 'Strikerate in 20 to 30 balls': [], 'Strikerate after 30 balls': [], 'Bowling Innings': [], 'Runs Given': [], 'Balls Bowled': [], 'Wickets Taken': [], 'Economy Rate': [], 'Bowling Strikerate': [], '3 wicket hauls': [], '5 wicket hauls': [], 'Wickets in Powerplay': [], 'Wickets in Middle Overs': [], 'Wickets in Death Overs': [], 'Economy in Powerplay': [], 'Economy in Middle Overs': [], 'Economy in Death Overs': [], 'Catches or Runouts as Fielder': [], 'Match Result': [], 'Man of the match':[]}

df = pd.DataFrame(dict)

data1 = open("data.csv", 'r')

for line in data1:
	name = line.split(",")[0]
	if name == "": continue

	content = stats(name)

	for match, l in content.items(): df.loc[len(df.index)] = [l[0][0], l[0][1], l[0][2], l[0][3], l[0][4], l[0][5], l[0][15], l[0][16], l[0][6], l[0][7], l[0][8], l[0][9], l[0][10], l[0][12], l[0][13], l[0][14], l[1][0], l[1][1], l[1][2], l[1][3], l[1][4], l[1][5], l[1][6], l[1][7], l[1][11], l[1][12], l[1][13], l[1][14], l[1][15], l[1][16], l[2][0], l[0][11], l[3][0]]

	print(name)

df.to_csv("dataset.csv", index = False)