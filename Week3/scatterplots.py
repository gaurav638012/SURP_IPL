from matplotlib import pyplot as plt
import numpy as np
from statistics import *

names = ["V Kohli", "DA Warner", "AB de Villiers", "JC Buttler"]
match_runs = {}
match_balls = {}
match_team = {}
match_pos = {}

prev_id = 0
prev_inn = 0

data = open("clean.csv", 'r')

for line in data:
	l = line.split(",")
	id = l[0]
	n = l[4]

	if prev_id != id or prev_inn != l[1]: count = 0

	if id not in list(match_runs.keys())+["id"]:
		match_runs[id] = {}
		match_balls[id] = {}
		match_team[id] = {}
		match_pos[id] = {}

	if n in names:
		if n not in match_runs[id].keys():
			match_runs[id][n] = 0
			match_balls[id][n] = 0
			match_team[id][n] = l[16]
			match_pos[id][n] = count

		match_runs[id][n] += int(l[7])
		if l[15] != "wides": match_balls[id][n] += 1
	if l[11] == "1": count += 1

	prev_id = id
	prev_inn = l[1]

data.close()

data = open("IPL Matches 2008-2020.csv", 'r')

match_winners = {}

for line in data:
	l = line.split(",")
	match_winners[l[0]] = l[10]

data.close()

scores = {}
result = {}
position = {}
balls = {}
strikerates = {}

for n in names:
	scores[n] = []
	result[n] = []
	position[n] = []
	balls[n] = []
	strikerates[n] = []

for match, score in match_runs.items():
	for n in names:
		if n in score.keys():
			scores[n] += [score[n]]

			if match_team[match][n] == match_winners[match]: result[n] += [1]
			else: result[n] += [0]

			position[n] += [match_pos[match][n]]

			balls[n] += [match_balls[match][n]]
			strikerates[n] += [float("{:.2f}".format(100*score[n]/match_balls[match][n]))]

for n in names:
	for pos in range(max(position[n])+1):	
		sc0 = []
		sc1 = []
		str0 = []
		str1 = []
		for ind, runs in enumerate(scores[n]):
			if position[n][ind] == pos:
				if result[n][ind] == 0:
					sc0 += [runs]
					str0 += [strikerates[n][ind]]
				else:
					sc1 += [runs]
					str1 += [strikerates[n][ind]]

		plt.scatter(sc1, str1, color = 'lime')
		plt.scatter(sc0, str0, color = 'tomato')
		plt.xlabel("Scores")
		plt.ylabel("Strikerates")
		plt.legend(["Won", "Lost"])
		plt.title("Scatter Plot for "+n+" in position "+str(pos))
		plt.show()

for n in names:
	for pos in range(max(position[n])+1):	
		bf0 = []
		bf1 = []
		str0 = []
		str1 = []
		for ind, bf in enumerate(balls[n]):
			if position[n][ind] == pos:
				if result[n][ind] == 0:
					bf0 += [bf]
					str0 += [strikerates[n][ind]]
				else:
					bf1 += [bf]
					str1 += [strikerates[n][ind]]

		plt.scatter(bf1, str1, color = 'lime')
		plt.scatter(bf0, str0, color = 'tomato')
		plt.xlabel("Balls Faced")
		plt.ylabel("Strikerates")
		plt.legend(["Won", "Lost"])
		plt.title("Scatter Plot for "+n+" in position "+str(pos))
		plt.show()