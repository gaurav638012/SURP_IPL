from matplotlib import pyplot as plt
import numpy as np
from statistics import *

names = ["V Kohli", "SK Raina", "RG Sharma", "JC Buttler", "KS Williamson", "DA Warner"]
match_runs = {}
match_balls = {}

data = open("IPL Ball-by-Ball 2008-2020.csv", 'r')

for line in data:
	l = line.split(",")
	id = l[0]
	n = l[4][1:-1]

	if id not in list(match_runs.keys())+['"id"']:
		match_runs[id] = {}
		match_balls[id] = {}

	if n in names:
		if n not in match_runs[id].keys():
			match_runs[id][n] = 0
			match_balls[id][n] = 0

		match_runs[id][n] += int(l[7])
		if l[15] != '"wides"':
			match_balls[id][n] += 1

scores = {}
balls = {}
strikerates = {}
stats = {}

for n in names:
	scores[n] = []
	balls[n] = []
	strikerates[n] = []
	stats[n] = {"runs":0, "matches":0, "balls faced":0, "runs mean":0, "runs stdev":0, "str":0, "str mean":0, "str stdev":0}

for match, score in match_runs.items():
	for n in names:
		if n in score.keys():
			scores[n] += [score[n]]
			balls[n] += [match_balls[match][n]]
			strikerates[n] += [float("{:.2f}".format(100*score[n]/match_balls[match][n]))]

for n, l in scores.items():
	stats[n]["runs"] = sum(l)
	stats[n]["matches"] = len(l)
	stats[n]["balls faced"] = sum(balls[n])
	stats[n]["str"] = float("{:.2f}".format(100*stats[n]["runs"]/stats[n]["balls faced"]))
	stats[n]["runs mean"] = float("{:.2f}".format(mean(l)))
	stats[n]["runs stdev"] = float("{:.2f}".format(stdev(l)))

	arr = np.array(l)
	plt.hist(arr, bins = 20)
	plt.title("Histogram of runs scored by "+n)
	plt.xlabel("Runs")
	plt.ylabel("Frequency")
	plt.savefig(n+"-runs.png")
	plt.show()

for n, l in strikerates.items():
	stats[n]["str mean"] = float("{:.2f}".format(mean(l)))
	stats[n]["str stdev"] = float("{:.2f}".format(stdev(l)))

	arr = np.array(l)
	plt.hist(arr, bins = 20)
	plt.title("Histogram of strikerate of "+n)
	plt.xlabel("Strikerate")
	plt.ylabel("Frequency")
	plt.savefig(n+"-str.png")
	plt.show()

print()
print("Statistics of players")
print()

for n, d in stats.items(): print(n+":", d)
print()

data.close()