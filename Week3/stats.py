import pandas as pd

#This function will take player name as input and output is dict in the form -
#{match_id: [innings, batting position, runs scored, balls faced, strikerate, out/notout, 50, 100, runs in powerplay, runs in middle overs, runs in death overs, result of match, str in first 20, str in next 10, str after 30, number of 4s, number of 6s],
#[innings, runs given, balls bowled, wickets taken, economy rate, strikerate, 3w, 5w, runs in pow, runs in mid, runs in death, w in pow, w in mid, w in death, eco in pow, eco in mid, eco in death], [catches or runouts as fielder], [man of the match], [team]}
#strikerates are -1 where not applicable

def stats(name):
	data = open("clean.csv", 'r')
	matches = pd.read_csv("IPL Matches 2008-2020.csv")
	content = {}

	prev_id = 0
	prev_inn = 0

	for line in data:
		l = line[:-1].split(",")
		id = l[0]
		if id == "id": continue
		id = int(id)

		if prev_id != id or prev_inn != l[1]: count = 0    #count is for batting position

		if l[4] == name:
			if id not in content.keys():
				content[id] = [[int(l[1]), count, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [(2*int(l[1]))%3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0], [0], [l[16]]]
				
			content[id][0][2] += int(l[7])   #runs scored

			if int(l[2]) < 6: content[id][0][8] += int(l[7])    #runs scored in powerplay
			elif int(l[2]) > 15: content[id][0][10] += int(l[7])    #runs scored in death overs
			else: content[id][0][9] += int(l[7])    #runs scored in middle overs

			if l[15] != "wides": content[id][0][3] += 1   #balls faced

			if content[id][0][3] <= 20: content[id][0][12] += int(l[7])
			elif content[id][0][3] <= 30: content[id][0][13] += int(l[7])
			else: content[id][0][14] += int(l[7])

			if int(l[7]) == 4 and l[10] == "0": content[id][0][15] += 1
			if int(l[7]) == 6 and l[10] == "0": content[id][0][16] += 1

		if l[13] == name:
			if id not in content.keys():
				content[id] = [[int(l[1]), count, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [(2*int(l[1]))%3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0], [0], [l[16]]]
			content[id][0][5] = 1    #0 -> not out, 1 -> out

		if l[11] == "1": count += 1    #number of players out before batsman came to bat

		prev_id = id
		prev_inn = l[1]

		if l[6] == name:
			if id not in content.keys():
				content[id] = [[(2*int(l[1]))%3, count, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [int(l[1]), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0], [0], l[17]]
				
			if l[15] != "legbyes" or l[15] != "byes":
				content[id][1][1] += int(l[9])
				if int(l[2]) < 6: content[id][1][8] += int(l[9])
				elif int(l[2]) > 15: content[id][1][9] += int(l[9])
				else: content[id][1][10] += int(l[9])

			if l[15] != "wides" or l[15] != "noballs":
				content[id][1][2] += 1
				if int(l[2]) < 6: content[id][1][14] += 1
				elif int(l[2]) > 15: content[id][1][15] += 1
				else: content[id][1][16] += 1

			if l[11] == "1" and l[12] != "run out":
				content[id][1][3] += 1
				if int(l[2]) < 6: content[id][1][11] += 1
				elif int(l[2]) > 15: content[id][1][12] += 1
				else: content[id][1][13] += 1

		if l[14] == name:
			if id not in content.keys():
				content[id] = [[(2*int(l[1]))%3, count, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [int(l[1]), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0], [0], l[17]]

			content[id][2][0] += 1

	data.close()

	for id in content.keys():
		if content[id][0][3] > 0: content[id][0][4] = float("{:.2f}".format(100*content[id][0][2]/content[id][0][3]))
		else: content[id][0][4] = -1

		if content[id][0][2] >= 100: content[id][0][7] = 1
		elif content[id][0][2] >= 50: content[id][0][6] = 1

		if content[id][0][3] > 0: content[id][0][12] = float("{:.2f}".format(100*content[id][0][12]/max(content[id][0][3], 20)))
		else: content[id][0][12] = -1

		if content[id][0][3] > 20: content[id][0][13] = float("{:.2f}".format(100*content[id][0][13]/max(content[id][0][3]-20, 10)))
		else: content[id][0][13] = -1

		if content[id][0][3] > 30: content[id][0][14] = float("{:.2f}".format(100*content[id][0][14]/(content[id][0][3]-30)))
		else: content[id][0][14] = -1

		if content[id][1][2] > 0: content[id][1][4] = float("{:.2f}".format(6*content[id][1][1]/content[id][1][2]))
		else: content[id][1][4] = -1

		if content[id][1][3] > 0: content[id][1][5] = float("{:.2f}".format(content[id][1][2]/content[id][1][3]))
		else: content[id][1][5] = -1

		if content[id][1][3] >= 5: content[id][1][7] = 1
		elif content[id][1][3] >= 3: content[id][1][6] = 1

		if content[id][1][14] > 0: content[id][1][14] = float("{:.2f}".format(6*content[id][1][8]/content[id][1][14]))
		else: content[id][1][14] = -1

		if content[id][1][15] > 0: content[id][1][15] = float("{:.2f}".format(6*content[id][1][9]/content[id][1][15]))
		else: content[id][1][15] = -1

		if content[id][1][16] > 0: content[id][1][16] = float("{:.2f}".format(6*content[id][1][10]/content[id][1][16]))
		else: content[id][1][16] = -1

		if list(matches.loc[matches['id'] == id]['player_of_match'])[0] == name: content[id][3][0] = 1

		if list(matches.loc[matches['id'] == id]['winner'])[0] == content[id][4][0]: content[id][0][11] = 1    #0 -> loss, 1 -> win

	return content