import pandas as pd

df = pd.read_csv("IPL Ball-by-Ball 2008-2020.csv")

df.sort_values(['id', 'inning', 'over', 'ball'], ascending=[True, True, True, True], inplace=True)

df.to_csv("clean.csv", na_rep = 'NA', index=False)