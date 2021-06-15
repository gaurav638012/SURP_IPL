from stats import *

virat = stats("V Kohli")
rohit = stats("RG Sharma")
sraina = stats("SK Raina")
kanew = stats("KS Williamson")

#Virat Kholi scores more than 20 runs, win percentage 
virwins = []
for match, l in virat.items():
	if l[2] >= 20: virwins.append(l[11])
print("Win Percentage when Virat Kohli scores more than 20 runs is", float("{:.2f}".format(100*sum(virwins)/len(virwins))))

#Virat playing in pos1 vs pos3 win percentage 
virpos1wins = []
virpos3wins = []
for match, l in virat.items():
	if l[1] == 0: virpos1wins.append(l[11])
	if l[1] == 1: virpos3wins.append(l[11])
print("Win Percentage when Virat Kohli comes opening is", float("{:.2f}".format(100*sum(virpos1wins)/len(virpos1wins))))
print("Win Percentage when Virat Kohli comes 1 down is", float("{:.2f}".format(100*sum(virpos3wins)/len(virpos3wins))))

#Rohit faces more tha 12 balls win vs lose percentage 
rowins = []
for match, l in rohit.items():
	if l[3] >= 12: rowins.append(l[11])
print("Win Percentage when Rohit Sharma bats for more than 12 balls is", float("{:.2f}".format(100*sum(rowins)/len(rowins))))

#Jos butler face more than 12 balls, team run rate increases significantly 
#How do we show this?

#Suresh Raina strike rate more or equal to 150 in first 6 balls he faces, win percentages
raiwins = []
for match, l in sraina.items():
	if l[12] >= 150: raiwins.append(l[11])
print("Win Percentage when Suresh Raina bats at more than 150 strikerate for the first 20 balls is", float("{:.2f}".format(100*sum(raiwins)/len(raiwins))))

#Virat vs Williamson run contribution is more than 10 runs to team , win percentage
kanewins = []
virwins1 = []
for match, l in virat.items():
	if l[2] >= 10: virwins1.append(l[11])
for match, l in kanew.items():
	if l[2] >= 10: kanewins.append(l[11])
print("Win Percentage when Virat Kohli and Kane Williamson scores more than 10 runs is", float("{:.2f}".format(100*sum(virwins1)/len(virwins1))), "and", float("{:.2f}".format(100*sum(kanewins)/len(kanewins))), "respectively")

#Virat/Rohit/warner score percentage when playing in Home vs away ipl
#We need team total score for this

#Virat/Rohit/Warner win percentage as captain home vs away in ipl
#We dont have captaincy details