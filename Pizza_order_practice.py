#---------------------------------------------------------------------------------------------------------------------#
# Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
#---------------------------------------------------------------------------------------------------------------------#


large_pizza = 25
medium_pizza = 20
small_pizza = 15
control = True

def sides(size):
    side_total = 0
    add_pepp = input('Do you want to add pepperoni? (y/n): ')
    extra_cheese = input('Do you want extra cheese? (y/n): ')
    
    if size.lower() == 's':
        if add_pepp.lower() == 'y':
            side_total += 2
        if extra_cheese.lower() == 'y':
            side_total += 1

    else: # Fine with just assuming anything else is large or medium for price purposes.
        if add_pepp.lower() == 'y':
            side_total += 3
        if extra_cheese.lower() == 'y':
            side_total += 1

    return side_total

def make_total(side_cost, pizza_cost):
    '''
    to make the output formatting/calculation across menu items easier i made it a function
    '''
    total = side_cost + pizza_cost
    print(f'Your total is ${total:.2f}\n')


while control:
    print('What size pizza would you like?\nEnter q to quit: ')
    size = input('(l)arge: $25\n(m)edium: $20\n(s)mall: $15\nEnter your selection: ')
    if size.lower() == 's':
        side_cost = sides(size)
        make_total(side_cost, small_pizza)
    elif size.lower() == 'm':
        side_cost = sides(size)
        make_total(side_cost, medium_pizza)
    elif size.lower() == 'l':
        side_cost = sides(size)
        make_total(side_cost, large_pizza)
    elif size.lower() == 'q':
        control = False


    




