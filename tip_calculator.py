# Primitive tip calculator
# Greeting > ask total bill > ask how many splits > % tip?

print("Welcome to the tip calculator.")
totalBill = float(input('What was the total bill?: '))
numSplits = int(input('How many people to split the bill?: '))
percentTip = int(input('what percentage tip would you like to give?: '))
perPerson = (totalBill // numSplits)
persTip = perPerson (percentTip / 100)
eaTotal = perPerson + persTip