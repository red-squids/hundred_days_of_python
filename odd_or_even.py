# Write a program that works out whether if a given number is an odd or even number
number = True
def mod(number):
    '''
    evaluates if a number is odd or even
    '''
    if number % 2 == False: # Basically 1 = True, 0 = False => 10 % 10 = False, 10 % 9 = True
        print(f'{number} is even!') # number has no remainder
    else:
        print(f'{number} is odd!') # number has a remainder of 1



control = True
while control:
    print('Enter a number to see if its odd or even.\nEnter 0 to quit!')
    number = int(input('What number do you choose: '))
    if number == 0:
        control = False
        print('Goodbye!')
    else:
        mod(number)

