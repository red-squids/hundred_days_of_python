print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

player_move = input("Move left or right?\nleft/right: ")
if player_move.lower() == 'left':
    player_move = input("You have encountered a river, swim across or wait for a ferry?\n(swim/wait): ")
    if player_move.lower() == 'wait':
        player_move = input("A ferry arrives, and you are dropped off at a mysterious building's dock. There are three doors ahead, which do you choose?\n(red/yellow/blue): ")
        if player_move.lower() == 'red':
            print('Upon opening the red door, intense fire lashed out and consumed you!\nGame Over!')
        elif player_move.lower() == 'blue':
            print('Upon opening the blue door, an enraged beast seizes you and tears you limb from limb!\nGame Over!')
        elif player_move.lower() == 'yellow':
            print('Upon opening the yellow door, you are nearly blinded by the sun shining off the piles of gold which await you!\nYou win!')

    else:
        print('While swimming across, you were mauled to death by a flock of hungry trout.\nGame Over!')
else:
    print('In a tragic twist of fate, while walking the shoreline you were swallowed by a massive sinkhole hidden beneath some sand.\nGame Over!')