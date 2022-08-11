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


def cost(size):
    add_pepp = input('Do you want to add pepperoni? (y/n): ')
    extra_cheese = input('Do you want extra cheese? (y/n): ')
    side_total = 0 # to avoid weird "used before assigned" issues.

    if size.lower() == 's':
        if add_pepp.lower() == 'y':
            side_total += 2
        if extra_cheese.lower() == 'y':
            side_total += 1
        total = side_total + small_pizza
        

    elif size.lower() == 'm':
        if add_pepp.lower() == 'y':
            side_total += 3
        if extra_cheese.lower() == 'y':
            side_total += 1
        total = side_total + medium_pizza

    elif size.lower() == 'l':
        if add_pepp.lower() == 'y':
            side_total += 3
        if extra_cheese.lower() == 'y':
            side_total += 1
        total = side_total + large_pizza

    print(f'Your total is ${total:.2f}\n')
    


while control:
    print('What size pizza would you like?\nEnter q to quit: ')
    size = input('(l)arge: $25\n(m)edium: $20\n(s)mall: $15\nEnter your selection: ')
    if size.lower() == 'q':
        print('Goodbye!\n')
        control = False
    else:
        cost(size)
