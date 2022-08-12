import random
rock = '''
Rock!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper!
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors!
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
control = True

while control:
    computerChoice = random.randint(0, 2)
    print('\n')
    playerChoice = int(input("- Type 0 for rock\n- Type 1 for Paper\n- Type 2 for Scissors!\n- Type any other number to quit\nWhat do you choose?: "))
    print('\n')
    if playerChoice == 0:
        print('Player chooses', rock)
    elif playerChoice == 1:
        print('Player chooses', paper)
    elif playerChoice == 2:
        print('Player chooses', scissors)

    if playerChoice == 0: # rock
        if computerChoice > 1: # scissors
            print('Computer chooses', scissors)
            print('Player wins!')
        elif computerChoice == 0:
            print('Computer chooses', rock)# paper
            print('Draw!')
        else:
            print('Computer chooses', paper)
            print('Player loses!')
    if playerChoice == 1: # paper
        if computerChoice < 1:
            print('Computer chooses', rock)
            print('Player wins!')
        elif computerChoice == 1: # paper
            print('Computer chooses', paper)
            print('Draw!')
        else:
            print('Computer chooses', scissors)        
            print('Player loses!') # scissors
    if playerChoice == 2:
        if computerChoice == 1:
            print('Computer chooses', paper)
            print('Player wins!')
        elif computerChoice == 2:
            print('Computer chooses', scissors)
            print('Draw!')
        else:
            print('Computer chooses', rock)
            print('Player loses!')
    if playerChoice >= 3:
        control = False


    
