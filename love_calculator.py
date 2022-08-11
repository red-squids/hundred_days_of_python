# Instructions
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:


name1 = input("enter name 1: ")
name2 = input('enter name 2: ')

name_combine = name1 + name2
name = name_combine.lower()
total1 = sum(name.count(x) for x in ("t", "r", "u","e"))
total2 = sum(name.count(y) for y in ("l", "o", "v","e"))
score = str(total1) + str(total2)
score_int = int(score)
 
if score_int < 10 or score_int > 90: 
  print(f"Your score is {score_int}, you go together like coke and mentos.")
elif score_int >= 40 and score_int <= 50:
  print(f"Your score is {score_int}, you are alright together.")
else:
  print(f"Your score is {score_int}.")



