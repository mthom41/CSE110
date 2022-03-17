#set up some veriables?
min_exp = 0
max_exp = 0
with open("life_expectancy.csv") as datta:
    header=next(datta)
    